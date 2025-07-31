# Gerenciamento Integrado e Adaptativo de Firewalls baseado na Fonte Única de Verdade (SSoT) da Rede
[![Licença](https://img.shields.io/badge/License-GNU%20GPL-blue)](https://opensource.org/licenses/GNU)

### Objetivo do Artefato:
Este artefato tem como objetivo exemplificar o funcionamento prático de um cenário real de aplicação do **DynSecNet**, em que duas reivindicações são simuladas e a execução destas são demonstradas.

**No primeiro cenário**, quando um servidor web é iniciado e fica pronto para aceitar requisições, um mecanismo interno no servidor aciona a API do **DynSecNet**, que processa a informação e cria um serviço do tipo ACCEPT na SSoT, que por sua vez aciona de volta a API e desencadeia a criação de uma regra de **iptables** para liberação de porta 80 no servidor, permitindo que ele seja acessado.

**No segundo cenário**, o servidor web possui um monitor de acessos por segundo e, ao detectar uma anomalia no número de requisições, um mecanismo interno no servidor aciona a API do **DynSecNet**, que processa a informação e cria um serviço do tipo DROP na SSoT com _source_ sendo o endereço IP do atacante, que por sua vez aciona de volta a API e desencadeia a criação de uma regra de **iptables** para o imediato bloqueio do IP do atacante, interrompendo o ataque.

### Resumo do Artigo:
_A gestão de firewalls em ambientes heterogêneos é crítica para a cibersegurança organizacional considerandos aspectos como configuraçõoes inconsistentes e respostas lentas a incidentes. Este trabalho apresenta a DynSecNet, uma ferramenta de código aberto que unifica políticas de segurança em uma fonte central, permitindo tradução automatizada para múltiplos fabricantes, resposta adaptativa a eventos (e.g., bloqueio de IPs maliciosos em <2s) e rastreabilidade integral. Avaliações experimentais demonstram sua eficácia na mitigação proativa de ataques e na redução de erros operacionais._

---

# Estrutura do README.md

Este README.md está organizado nas seguintes seções:

1.  **Título, Objetivo e Resumo:** Título do projeto, objetivo do artefato e resumo do artigo.
2.  **Estrutura do README.md:** A presente estrutura.
3.  **Selos considerados:** Lista dos Selos a serem considerados no processo de avaliação.
4.  **Informações básicas:** Descrição dos componentes e requisitos mínimos para a execução do experimento.
5.  **Dependências:** Informação sobre as dependências necessárias.
6.  **Preocupações com segurança:** Lista das considerações e preocupações com a segurança.
7.  **Instalação:** Relação de opções para a realização do experimento, bem como as instruções individuais de cada opção.
8.  **Teste mínimo:** Instruções para a execução das simulações.
9.  **Experimentos:** Informações de replicação das reivindicações.
10. **Documentação:** Documentação básica da aplicação.
11. **Ambiente de teste:** Ambientes que foram usados em testes.
12.  **Licença:** Informações sobre a licença do projeto.

---

# Selos considerados

Os selos considerados são:
- Artefatos Disponíveis (SeloD)
- Artefatos Funcionais (SeloF)
- Artefatos Sustentáveis (SeloS)
- Experimentos Reprodutíveis (SeloR)

---

# Informações básicas

#### O experimento possui duas opções disponíveis para execução, sendo:

 1. **Opção 1:** Imagem de **VirtualBox** com ambiente auto-contido já preparado para o experimento (testado em Sistema Operacional Microsoft Windows 10 ou superior e distribuições Linux baseada em Ubuntu versão 20.04 ou mais recente: Ubuntu, Kubuntu, Xubuntu e variantes) - o ambiente tem como usuário e senha **experimento/experimento**; ou
 2. **Opção 2:** Download de todos os contêineres envolvidos e execução destes, localmente em um desktop ou laptop (testado em Sistema Operacional não virtualizado, bare metal, baseado em Ubuntu versão 20.04 ou mais recente: Ubuntu, Kubuntu, Xubuntu e variantes, instalado).
 
#### Requisitos de software e hardware para cada Opção de execução:

 1. **Opção 1:** Nesta opção, deve ser feito o download e importação de um Appliance Virtual (arquivo .ova) e execução do ambiente virtualizado utilizando VirtualBox. Para tanto, são necessários: Sistema Operacional Microsoft Windows 10 ou superior e distribuições Linux baseada em Ubuntu versão 20.04 ou mais recente: Ubuntu, Kubuntu, Xubuntu e variantes), processador 64 bits com no mínimo 4 núcleos e flag de virtualzação VT-x ativada na BIOS, 4GB de memória RAM para uso exclusivo no experimento, VirtualBox 7.1 ou superior com Extension Pack correspondente à versão do VirtualBox; ou
 2. **Opção 2:** Nesta opção, todo experimento será executado em ambiente local através do download e execução automatizada de todos os componentes utilizando Docker. Para isto, são necessários: Sistema Operacional Linux, bare metal, baseado em Ubuntu versão 20.04 ou mais recente: Ubuntu, Kubuntu, Xubuntu e variantes), processador 64 bits com no mínimo 4 núcleos, 4GB de memória RAM para uso exclusivo no experimento, Docker Engine versão 26 ou superior e alguns pacotes disponíveis no repositório oficial (ver dependências).

Resumo dos requisitos de hardware e sistema operacional:

| Opção | Sistema Operacional     											                                              	     | Memória RAM |  Requisito              |
|-------|----------------------------------------------------------------------------------------|-------------|-------------------------|
| 1     | Microsoft Windows 10 ou superior, Linux baseado em Ubuntu versão 20.04 ou mais recente | 4GB         | VirtualBox 7+ e ExtPack |
| 2     | Ubuntu bare metal versão 20.04 ou mais recente: Ubuntu, Kubuntu, Xubuntu e variantes   | 4GB         | Docker Engine 26+       |
 
---

# Dependências

#### O experimento possui duas opções disponíveis para execução, tendo cada uma delas as seguintes dependências:

 1. **Opção 1:** Cumpridos os requisitos descritos na seção anterior, referentes a **Opção 1**, esta opção não possui dependências.
 2. **Opção 2:** Cumpridos os requisitos descritos na seção anterior, referentes a **Opção 2**, é necessário certificar-se que o Docker Engine versão 26 ou superior esteja instalado conforme descrito na [página oficial da ferramenta](https://docs.docker.com/engine/install/ubuntu/), bem como a seção [postinstall](https://docs.docker.com/engine/install/linux-postinstall/), além dos pacotes __curl__, __rsync__, __wget__ e __git__ instalados.

Resumo dos pacotes adicionais necessários (dependências):

| Opção   | Pacotes adicionais necessários          |
|---------|-----------------------------------------|
| 1       | Nenhum pacote adicional                 |
| 2       | Pacotes `curl`, `rsync`, `wget` e `git` |

A instalação das dependências, caso necessário, ocorrerá automaticamente durante a execução do processo de execução do ambiente, bastando seguir as instruções exibidas em tela.

---

# Preocupações com segurança

#### O experimento possui duas opções disponíveis para execução, tendo cada uma delas as seguintes preocupações com segurança:

 1. **Opção 1:** Por tratar-se de execução de Appliance pronta e virtualizada em ambiente auto contido, não há considerações quanto a preocupações de segurança nesta opção.
 2. **Opção 2:** Durante a execução do conjunto de contêineres envolvidos, dependendo das configurações do dispositivo que estiver hospedando o experimento, as portas **3000**, **8000** e **8080** poderão estar abertas para a rede local, dependendo das configurações de firewall, encaminhamento de portas e perfil de segurança das interfaces de rede. 

#### Preocupações adicionais a com segurança

Cabe ressaltar que todas as senhas, chaves de API e outros elementos secretos dos componentes foram gerados para apenas para a demonstração do experimento, de tal forma que sua força de segurança foram propositalmente baixadas para facilitar o experimento. As senhas, chaves de API e chaves RSA do SSH utilizada são descartáveis e servem apenas ao propósito do experimento.

---

# Instalação

#### O experimento possui duas opções disponíveis para execução, tendo cada uma delas as seguintes etapas de instalação:

### **Opção 1: Appliance de VirtualBox**

1. Baixe o appliance (arquivo .ova) do experimento que está disponível através do [link](https://drive.google.com/file/d/1cvb88FobXy66zM1J7XIz2Kpz3fUTMz5F/view?usp=sharing).
2. Importe o arquivo __exp-sf-sbseg2025.ova__ baixado no VirtualBox:
   
<img src="https://github.com/SBSeg25/DynSecNet/blob/main/app/doc/contrib/Screenshot_20250516_122234.png" alt="Import 01" style="float: left; width: 50%; height: auto;">

<img src="https://github.com/SBSeg25/DynSecNet/blob/main/app/doc/contrib/Screenshot_20250516_122409.png" alt="Import 02" style="float: left; width: 50%; height: auto;">

3. Clique em _Finalizar_ e aguarde o processo de importação.

4. Execute a VM recém importada.

<img src="https://github.com/SBSeg25/DynSecNet/blob/main/app/doc/contrib/Screenshot_20250525_141518.png" alt="Import 03" style="float: left; width: 50%; height: auto;">

**4.1. Caso seja exibida uma mensagem de erro do VirtualBox referente a interface de rede, isto é porque a nomenclatura do dispositivo de rede local é diferente daquela existente no computador onde a imagem foi gerada. Basta selecionar a opção "Alterar as opções de rede" e salvar.**

<img src="https://github.com/SBSeg25/DynSecNet/blob/main/app/doc/contrib/Screenshot_20250615_145822.png" alt="Import 43" style="float: left; width: 30%; height: auto;">

5. Após a inicialização da VM, abra o terminal (atalho no desktop) e execute:

<img src="https://github.com/SBSeg25/DynSecNet/blob/main/app/doc/contrib/Screenshot_20250512_153235.png" alt="Import 33" style="float: left; width: 10%; height: auto;">

```bash
iniciar-experimento
```

6. Aguarde a conclusão da preparação do ambiente. Informações do andamento da preparação serão exibidas, bem como informações da básicas da operação do experimento serão exibidas ao término do procedimento.

<img src="https://github.com/SBSeg25/DynSecNet/blob/main/app/doc/contrib/Screenshot_20250621_123331.png" alt="Import 63" style="float: left; width: 100%; height: auto;">

### **Opção 2: Execução de contêineres localmente**

1. Em um terminal do Linux local, executar:
```bash
wget "https://github.com/SBSeg25/DynSecNet/raw/refs/heads/main/experimento-sf-install.sh" -O "/tmp/experimento-sf-install.sh" ; chmod +x "/tmp/experimento-sf-install.sh" ; /tmp/experimento-sf-install.sh
```
2. Aguarde o término do processo de criação do ambiente.

_(Caso alguma dependência ou requisito anteriormente descrito não tenham sido cumpridos, o script de instalação apresentará em tela as opções de resolução dos elementos faltantes)_

3. Ao término do processo de instalação, serão exibidas informações em tela com instruções básicas da operação do experimento.

<img src="https://github.com/SBSeg25/DynSecNet/blob/main/app/doc/contrib/Screenshot_20250621_124003.png" alt="Import 63" style="float: left; width: 100%; height: auto;">

---

# Teste mínimo

#### O experimento possui duas opções disponíveis para execução, tendo cada uma delas os seguintes testes mínimos:

### **Opção 1: Appliance de VirtualBox**

Estando na máquina virtual recém importada, certificar-se de que a máquina virtual possui conexão com a internet e o Docker Engine esteja pronto:

```bash
ping -c 3 github.com
```
<img src="https://github.com/SBSeg25/DynSecNet/blob/main/app/doc/contrib/Screenshot_20250525_143939.png" alt="Import 05" style="float: left; width: 50%; height: auto;">

Caso o retorno seja similar, a máquina virtual possui conexão com a internet.

```bash
docker ps -a
```
Caso o retorno seja uma lista vazia similar ao exemplo acima, o Docker Engine estará pronto para a execução do experimento.

<img src="https://github.com/SBSeg25/DynSecNet/blob/main/app/doc/contrib/Screenshot_20250525_142859.png" alt="Import 04" style="float: left; width: 50%; height: auto;">

### **Opção 2: Execução de contêineres localmente**

Certificar-se de que localmente há conexão com a internet e o Docker Engine está pronto:
Abra um terminal local e execute:

```bash
ping -c 3 github.com
```
<img src="https://github.com/SBSeg25/DynSecNet/blob/main/app/doc/contrib/Screenshot_20250525_143939.png" alt="Import 05" style="float: left; width: 50%; height: auto;">

Caso o retorno seja similar, o dispositivo local possui conexão com a internet.

```bash
docker ps -a
```
Caso o retorno seja uma lista vazia, o Docker Engine local estará pronto para a execução do experimento.

<img src="https://github.com/SBSeg25/DynSecNet/blob/main/app/doc/contrib/Screenshot_20250525_143226.png" alt="Import 06" style="float: left; width: 50%; height: auto;">

* No intuito de evitar quaisquer conflitos entre contêiners existentes no computador (caso o retorno anterior não seja uma lista vazia), sugere-se **parar** todos os contêiners que possam estar rodando localmente, para isso, execute em um terminal:
```bash
while read CID; do docker stop "${CID}"; done < <( docker ps -a | grep -v 'CONTAINER ID' | awk '{print $1}' )
```

---

# Experimentos

#### Demonstração do Experimento utilizando o ambiente VirtualBox (Opção 1)

[![Demonstracao Youtube](https://github.com/SBSeg25/DynSecNet/blob/main/app/doc/contrib/Screenshot_20250528_163204.jpg)](https://www.youtube.com/watch?v=R_sTcDdsZNg)

#### O experimento possui duas opções disponíveis para execução, tendo cada uma delas os seguintes etapas para a obtenção das reivindicações:

## Reivindicações: Cenário 1 - Liberação automatizada de porta quando serviço estiver pronto

#### **Opção 1: No Appliance de VirtualBox**

Com o Ambiente já iniciado na máquina virtual, abrir um terminal e executar o alias que verifica o estado do iptables do servidor:

```bash
verificar-firewall-servidor
```

#### **Opção 2: Na execução de contêineres localmente**

Abrir o terminal e executar o comando para inspecionar o estado do iptables do servidor:

```bash
docker exec -it ubuntu-server iptables -nL
```

Observar a implantação da regra de firewall permitindo o acesso à porta 80 tão logo o contêiner do servidor _nginx_ subiu e ficou pronto para aceitar requisições.

<img src="https://github.com/SBSeg25/DynSecNet/blob/main/app/doc/contrib/Screenshot_20250525_150925.png" alt="Import 09" style="float: left; width: 50%; height: auto;">


## Reivindicações: Cenário 2 - Mitigação automatizada de ataque DoS

#### **Opção 1: Appliance de VirtualBox**

1. Abrir no navegador **da máquina virtual** o [Netbox](http://localhost:8080/ipam/services/) e o [Grafana](http://localhost:3000/public-dashboards/7d7b1678f7e94829a1816723c251e934?refresh=auto)

#### **Opção 2: Execução de contêineres localmente**

1. Abrir no navegador do host que está executando os contêineres o [Netbox](http://localhost:8080/ipam/services/) e o [Grafana](http://localhost:3000/public-dashboards/7d7b1678f7e94829a1816723c251e934?refresh=auto)

Note que em ambos casos o Netbox tem como usuário e senha **admin/admin**

2. No Netbox, verifique que há um serviço HTTP para o _device_ container-nginx. Este serviço foi aplicado como regra de firewall assim que o nginx ficou disponível.

<img src="https://github.com/SBSeg25/DynSecNet/blob/main/app/doc/contrib/Screenshot_20250525_152105.png" alt="Import 10" style="float: left; width: 50%; height: auto;">

3. No Grafana, observar a baixa contagem de acessos. Os contêineres ubuntu-client e ubuntu-rogue possuem scripts que acessam o contêiner ubuntu-server aleatoriamente de 1 a 9 vezes por segundo, simulando acessos considerados normais, demonstrando que o contêiner com o servidor nginx encontra-se acessível.

<img src="https://github.com/SBSeg25/DynSecNet/blob/main/app/doc/contrib/Screenshot_20250525_152616.png" alt="Import 11" style="float: left; width: 50%; height: auto;">

#### **Opção 1: Appliance de VirtualBox**

4. Abrir um novo terminal e executar o alias para simular um ataque:

```bash
iniciar-ataque
```

#### **Opção 2: Execução de contêineres localmente**

4. Abrir um novo terminal e executar o comando para simular um ataque:

```bash
docker exec -it ubuntu-rogue /usr/local/bin/dos.sh
```

5. No Grafana, observar a anomalia no número de acessos. O contêiner ubuntu-rogue dispara uma rajada aleatória entre 100 e 150 acessos por segundo contra o contêiner ubuntu-server, simulando um ataque.

<img src="https://github.com/SBSeg25/DynSecNet/blob/main/app/doc/contrib/Screenshot_20250525_153002.png" alt="Import 12" style="float: left; width: 50%; height: auto;">

_Note que poucos segundos após o início do ataque, o mesmo foi interrompido. Tão logo o monitoramento percebeu a anomalia no número de acessos, houve a implantação da regra de firewall bloqueando o acesso do IP do atacante._

6. No Netbox, recarregue a página e verifique que há um novo serviço para o _device_ container-nginx. Este serviço foi aplicado como regra de firewall com _source_ do IP do atacante assim que o ataque foi identificado.

<img src="https://github.com/SBSeg25/DynSecNet/blob/main/app/doc/contrib/Screenshot_20250525_153354.png" alt="Import 13" style="float: left; width: 50%; height: auto;">

#### **Opção 1: Appliance de VirtualBox**

7. Para reiniciar o experimento, pressione Ctrl+C no terminal do comando executado anteriormente (_iniciar-ataque_) e delete o serviço _DoS_ no Netbox. A remoção do serviço fará o deploy da remoção da regra de bloqueio no firewall do servidor nginx.

#### **Opção 2: Execução de contêineres localmente**

7. Para reiniciar o experimento, pressione Ctrl+C no terminal do comando executado anteriormente (_docker exec -it ubuntu-rogue /usr/local/bin/dos.sh_) e delete o serviço _DoS_ no Netbox. A remoção do serviço fará o deploy da remoção da regra de bloqueio no firewall do servidor nginx.

---

## Documentação básica:

### Principais funções da aplicação:

#### `svc_deploy(request)`
Trata eventos do tipo 'model' == 'service' via POST do Webhook do SSoT, recebendo 'id' do serviço como parâmetro.
Aciona a função `svc_deploy_task` passando o 'id' do serviço e o tipo de evento como parâmetro.

#### `svc_deploy_task(service_id,service_event,request_data)`
Caso o evento seja 'created', aciona a função `add_one_rule_service(service_id)`
Caso o evento seja 'deleted', aciona a função `del_one_rule_service(service_id)`
Caso o evento seja 'updated', aciona a função `del_one_rule_service(service_id)` e em seguida a função `add_one_rule_service(service_id)`

#### `add_one_rule_service(service_id)`
Busca no SSoT as informações do serviço por 'id' e os serviços existentes do device através de consulta pela função `device_services(device_id)`, retornando nome, portas, protocolo, endereço ip, tag, origem, descrição e comentários, renderizando o template Ansible de criação de regra de firewall com base nas informações obtidas e aplicando no inventory cujo endereço ip é do dispositivo em questão.

#### `del_one_rule_service(service_id)`
Busca no SSoT as informações do snapshot do estado anterior do serviço por 'id' e os serviços existentes do device através de consulta pela função `device_services(device_id)`, retornando nome, portas, protocolo, endereço ip, tag, origem, descrição e comentários, renderizando o template Ansible de remoção de regra de firewall com base nas informações obtidas e aplicando no inventory cujo endereço ip é do dispositivo em questão.

#### `device_services(device_id)`
Busca no SSoT os serviços existentes e aplicados em um device através de consulta pelo 'device_id', retornando o objeto completo do device em questão.

#### `svc_server_up(request)`
Busca serviços por 'id' cuja tag não seja DROP e aplica a tag ACCEPT. Esta ação aciona o webhook do SSoT com evento do tipo 'updated', desencadeando as funções `del_one_rule_service` e `add_one_rule_service`, aplicando a regra do tipo ACCEPT no SSoT, renderizando o template Ansible de criação de regra de firewall com base nas informações recebidas.

#### `svc_ddos(request)`
Recebe informações pelo sensor (porta, protocolo e endereço IP do atacante), busca no SSoT informações do device em questão com base no endereço IP de quem acionou a API, cria serviço no SSoT com tag do tipo DROP com as informações recebidas, atrelando ao device acionador, renderizando o template Ansible de criação de regra de firewall com base nas informações recebidas.

# Ambientes de testes
Para garantir a compatibilidade e o desempenho ideais, os testes foram realizados no seguinte ambiente:
Hardware

Ambiente de teste 1:
 * Notebook: Dell G15 (Modelo 2023/2024, com RTX 4050)
   * Processador: Intel Core i7-13650HX 
   * Memória RAM: 16GB DDR5 @ 4800MHz (ou superior)
   * Placa de Vídeo: NVIDIA GeForce RTX 4050 Laptop GPU
   * Armazenamento: SSD NVMe de 512GB (ou superior)

Software: 
 * Sistema Operacional: Windows 11 Home
   * Virtual box 7.0
 * Sistema Operacional: 24.04 LTS
   * Docker Engine 28.3.0

Ambiente de teste 2:
 * Desktop: 
   * Processador: AMD Ryzen 5 5500
   * Memória RAM: 8GB DDR4

Software:
 * Sistema Operacional: Windows 11 Home
   * Virtual box 7.0
 * Sistema Operacional: 24.04 LTS
   * Docker Engine 28.3.0

# LICENSE

Este projeto está licenciado sob a Licença GNU - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
