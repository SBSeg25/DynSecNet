## Documentação básica:

### Principais funções da aplicação:

#### `svc_deploy(request)`
Trata eventos do tipo 'model' == 'service' via POST do Webhook do SSoT, recendo 'id' do serviço como parâmetro.
Aciona a função `svc_deploy_task` passando o 'id' do serviço e o tipo de evento como parâmetro.

#### `svc_deploy_task(service_id,service_event,request_data)`
Caso o evento seja 'created', aciona a função `add_one_rule_service(service_id)`
Caso o evento seja 'deleted', aciona a função `del_one_rule_service(service_id)`
Caso o evento seja 'updated', aciona a função `del_one_rule_service(service_id)` e em seguida a função `add_one_rule_service(service_id)`

#### `add_one_rule_service(service_id)`
Busca no SSoT as informações do serviço por 'id' e os serviços existentes do device através de consulta pela função `device_services(device_id)`, retornando nome, portas, protocolo, endereço ip, tag, origem, descrição e comentários, renderizando o template ansible de criação de regra de firewall com base nas informações obtidas e aplicando no inventory cujo endereço ip é do dispositivo em questão.

#### `del_one_rule_service(service_id)`
Busca no SSoT as informações do snapshot do estado anterior do serviço por 'id' e os serviços existentes do device através de consulta pela função `device_services(device_id)`, retornando nome, portas, protocolo, endereço ip, tag, origem, descrição e comentários, renderizando o template ansible de remoção de regra de firewall com base nas informações obtidas e aplicando no inventory cujo endereço ip é do dispositivo em questão.

#### `device_services(device_id)`
Busca no SSoT os serviços existentes e aplicados em um device através de consulta pelo 'device_id', retornando o objeto completo do device em questão.

#### `svc_server_up(request)`
Busca serviços por 'id' cuja tag não seja DROP e aplica a tag ACCEPT. Esta ação aciona o webhook do SSoT com evento do tipo 'updated', desencadeando as funções `del_one_rule_service` e `add_one_rule_service`, aplicando a regra do tipo ACCEPT no SSoT, renderizando o template ansible de criação de regra de firewall com base nas informações recebidas.

#### `svc_ddos(request)`
Recebe informações pelo sensor (porta, protocolo e endereço IP do atacante), busca no SSoT informações do device em questão com base no endereço IP de quem acionou a API, cria serviço no SSoT com tag do tipo DROP com as informações recebidas, atrelando ao device acionador, renderizando o template ansible de criação de regra de firewall com base nas informações recebidas.
