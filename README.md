# Desafio de Data Engineer - EMD

Repositório de instrução para o desafio técnico para vaga de Pessoa Engenheira de Dados no Escritório de Dados do Rio de Janeiro

## Descrição do desafio

Neste desafio você deverá capturar, estruturar, armazenar e transformar dados de uma API instantânea. A API consiste nos dados de GPS do BRT que são gerados na hora da consulta com o último sinal transmitido por cada veículo.

Para o desafio, será necessário construir uma pipeline que captura os dados minuto a minuto e gera um arquivo no formato CSV. O arquivo gerado deverá conter no mínimo 10 minutos de dados capturados (estruture os dados da maneira que achar mais conveniente), então carregue os dados para uma tabela no Postgres. Por fim, crie uma tabela derivada usando o DBT. A tabela derivada deverá conter o ID do onibus, posição e sua a velocidade.

A pipeline deverá ser construída subindo uma instância local do Prefect (em Python). Utilize a versão *0.15.9* do Prefect.


## Configuração de ambiente para desenvolvimento
### Requisitos
* [Docker](https://docs.docker.com/get-docker/) </br>
* [Docker Compose](https://docs.docker.com/compose/install/)

## Procedimentos
* Clonar o repositório
```bash
git clone https://github.com/ptk-trindade/emd-desafio-data-eng.git
```
* Em um terminal, ir até a pasta raiz do projeto (eg. `cd emd-desafio-data-eng`)
* Subir o ambiente com o docker-compose
```bash
docker-compose up --build
```
* Pronto! O ambiente já está subindo. </br>

## Execução
Quando o ambiente terminar de subir, ele comçará a executar a pipeline. </br>
O fluxo irá rodar 10 vezes, uma a cada minuto, gerando um arquivo `app/csv_files/brt_data.csv`. (ps. Esse arquivo será gerado _dentro_ do container) </br>

Os dados também serão carregados em um banco Postgres, que pode ser acessado localmente com as seguintes credenciais: </br>
```cr
Host: localhost
Port: 54320
Database: brt_db
Username: username
Password: secret
```