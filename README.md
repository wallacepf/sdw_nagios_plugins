# Citrix SD-WAN Nagios Monitor

Este projeto tem o objetivo de criar monitores do tipo Nagios Plugins, para monitorar arquiteturas baseadas na solução Citric SD-WAN

## Inicio

Abaixo você encontrará os detalhes para fazer o setup dos monitores em seu ambiente.

### Pré-Requisitos

Dependencias

Instalar Python 3

CentOS/RH:
```
yum install python3
```
Debian/Ubuntu:
```
apt-get install python3
```
Instalar as dependencias dos monitores

CentOS/RH:
```
yum install gcc python-devel

pip3 install easysnmp
```

Debian/Ubuntu:

```
apt-get install gcc python-dev

pip3 install easysnmp
```

## Executando os monitores

Durante a fase inicial, temos somente 5 monitores disponíveis retornando apenas o estado de saúde dos objetos. Os monitores que possuem 'v3' no nome foram escritos para trabalhar com SNMPv3.

check_sdwan_health.py: Checa a saúde do serviço SD-WAN
Parâmetros: '-H': IP do Destino; '-U': Username para uso da API; '-P': Password para uso da API

Exemplo
```
./check_sdwan_health.py -H 10.0.100.10 -U testeapi -P testeapi
```
check_wanlink.py: Checa a saúde dos links WAN
Parâmetros: '-H': IP do Destino; '-C': Nome da Community SNMP; '-O': Número do Link*
Parâmetros 'v3': '-H': IP do Destino; '-U': Nome do usuário; '-P': Senha do usuário; '-O': Número do Link

Exemplo
```
./check_wanlink.py -H 10.0.100.10 -C public -L 1
./check_wanlink_v3.py -H 10.0.100.10 -U testesnmp -P testesnmp -O 1
```
*O número do link é uma forma de voce diferenciar os links dentro do equipamento destino. Basicamente, se você possui dois links em uma localidade
voce deve criar dois serviços utilizando o parametro '-O 1' para o primeiro link e '-O 2' para o segundo link. Caso não haja conhecimento da quantidade
de links na localidade remota, voce pode rodar o script diretamente sem o parametro '-O' para retornar todos os links existentes.

check_vpath.py: Checa a saúde do Virtual Path

Parâmetros: '-H': IP do Destino; '-C': Nome da Community; '-O': Número do Virtual Path*
Parâmetros 'v3': '-H': IP do Destino; '-U': Nome do usuário; '-P': Senha do usuário; '-O': Número do Link

Exemplo
```
./check_vpath.py -H 10.0.100.10 -C public -O 1
./check_vpath_v3.py -H 10.0.100.10 -U testesnmp -P testesnmp -O 1
```

*O número do virtual path segue a mesma lógica do número do link. Possuindo também, a opção de retornar todos os virtual paths existentes quando
a opção '-O' é omitida.

## Troubleshooting e Informações adicionais

- Exemplos de configurações do Nagios podem ser encontrados na pasta 'nagios' dentro deste projeto

- Usuários com permissão de Guest são permitidos para execução da API

- Caso haja algum problema de permissionamento de execução dos arquivos, adicionar a permissão de executável nos scripts

Exemplo
```
chmod +x <nome do script>
```

- Erros de "Bad Interpreter"
 são corrigidos usando o comando dos2unix para ajustar o End of Line dos arquivos

Exemplo
```
dos2unix script.py
```

- A versão do SNMP utilizada nos scripts é a versão 2