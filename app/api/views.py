import pynetbox
import pprint
import logging
import json
from django.http import JsonResponse
from api.tasks import add, svc_deploy_task, sw_deploy_task, interface_deploy_task, device_services, device_persistent_services, apply_device_persistent_services
from api.models import Sot
from rest_framework.decorators import api_view
from rest_framework.response import Response

logger = logging.getLogger(__name__)

@api_view(['POST','GET'])
def request_dump(request, format=None):
    content = {}

    content['request'] = request.data
    soma = add(2,2)
    pprint.pprint(content)
    print(soma)

    return Response(content)


@api_view(['GET'])
def sot_populate(request, format=None):
    content = {}

    content['message'] = "Sot criada: " + sot.name
    sot = Sot.objects.create()
    sot.save()
    logger.info("Sot criada: " + sot.name)

    return Response(content)

@api_view(['POST'])
def svc_deploy(request, format=None):
    
    sot = Sot.objects.get(name="netbox-lab")

    netbox_url = "http://" + sot.hostname + ":" + str(sot.port) + "/"
    netbox_token = sot.token

    netbox = pynetbox.api(
        netbox_url,
        token=netbox_token
    )
    
    content = {}
    pprint.pprint(request.data)

    if request.data['model'] == 'service':
        request_data = request.data
        service_id = request.data['data']['id']
        service_event = request.data['event']
        logger.info("Abrindo tarefa do Service: " + str(service_id))
        task = svc_deploy_task.delay(service_id,service_event,request_data)
    
    return Response('')

# Reaplica as regras de iptables de todos os serviços
@api_view(['GET'])
def svc_get_all(request, device_id):
    content = {}
    get_device_services = device_services(device_id)
    for svc in get_device_services:
        task = svc_deploy_task.delay(svc,'created','')
    return Response(content)

@api_view(['GET'])
def svc_persist(request, device_id):
    content = {}
    get_device_services = device_services(device_id)
    for svc in get_device_services:
        rule = device_persistent_services(device_id, svc)
    task = apply_device_persistent_services.delay(device_id)

@api_view(['POST'])
def svc_server_up(request):

    sot = Sot.objects.get(name="netbox-lab")

    netbox_url = "http://" + sot.hostname + ":" + str(sot.port) + "/"
    netbox_token = sot.token

    netbox = pynetbox.api(
        netbox_url,
        token=netbox_token
    )

    if request.content_type == 'application/json':
        data = json.loads(request.body.decode('utf-8'))
        ip = data['server_ip']
        netbox_device = netbox.ipam.ip_addresses.get(address=ip).assigned_object.device.id
        netbox_service = netbox.ipam.services.get(device_id=netbox_device,tag__n='drop')
        netbox_service.tags.append({"id": "1"})
        netbox_service.save()
        data = {}
        
    return Response('UP')

@api_view(['POST'])
def svc_ddos(request):

    sot = Sot.objects.get(name="netbox-lab")

    netbox_url = "http://" + sot.hostname + ":" + str(sot.port) + "/"
    netbox_token = sot.token

    netbox = pynetbox.api(
        netbox_url,
        token=netbox_token
    )

    if request.content_type == 'application/json':
        data = json.loads(request.body.decode('utf-8'))
        ip = data['server_ip']
        netbox_ip = netbox.ipam.ip_addresses.get(address=ip)
        ip_id = int(netbox_ip.id)
        netbox_device = netbox_ip.assigned_object.device.id
        source = data['source']
        port = data['port']
        proto = str(data['proto'].lower())
        payload = {
            'ports': [port],
            'name': 'DoS',
            'parent_object_id': netbox_device,
            'parent_object_type': 'dcim.device',
            'custom_fields': { 'source': str(source + '/32') },
            'protocol': proto,
            'ipaddresses': [ ip_id ],
            'description': 'DynSecNet - DoS',
            'comments': 'DynSecNet - DoS',
            'tags': [ { 'id': 2 } ]
        }
        create_svc_ddos = netbox.ipam.services.create(payload)
        print(create_svc_ddos)
    return Response('DoS')
