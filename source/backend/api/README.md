# Minha API - componente D

Este API é a parte backend da entrega do MVP para o terceiro (3º) sprint do  **Curso de Pós Graduação em Engenharia de software** 

Serviço que tem o contexto de negocio de gravar informações de operação do estacionamento

## Documentos importantes
    Arquivo com o diagrama de componentes com o nome de "Diagrama-componentes-MVP-Sprint-03.pdf".
    Encontra-se na raiz do repositório.

## Instruções gerais
---
01)Git e Python instalado no desktop e/ou notebook   

02)Clonar o repositório https://github.com/Etyonamine/puc-rio-mvp-sprint-3-componente-D.git

03)Para a execução deve ser utilizado um dos modos de execução abaixo:


## Instruções - Instalação , execução o servidor 

As principais tecnologias que serão utilizadas aqui é o:
 - [Flask](https://flask.palletsprojects.com/en/2.3.x/)
 - [SQLAlchemy](https://www.sqlalchemy.org/)
 - [OpenAPI3](https://swagger.io/specification/)
 - [SQLite](https://www.sqlite.org/index.html)

---
### Instalação


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

---
### Modo de execução via servidor


Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5001
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5001 --reload
```

---
### Acesso no browser

1) Abra o [http://localhost:5001/#/](http://localhost:5001/#/) no navegador para verificar o status da API em execução.
2) Selecione uma das opções : swagger / redoc / rapiDoc para visualizar via interface os serviços e métodos.

---
## Modo de execução via Docker

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal.
Execute **como administrador** o seguinte comando que encontra-se entre as aspas duplas para construir a imagem Docker:

```
$ "docker build -t componente-d ."
```

Uma vez criada a imagem, para executar o container basta executar, **como administrador**, seguinte o comando:

```
$ docker run -p 5001:5001 componente-d
```

Uma vez executando, para acessar a API, basta abrir o [http://localhost:5001/#/](http://localhost:5001/#/) no navegador.

### Comandos Docker

>**Para verificar se a imagem foi criada** você pode executar o seguinte comando:
>
>```
>$ docker images
>```
>
> Caso queira **remover uma imagem**, basta executar o comando:
>```
>$ docker rmi <IMAGE ID>
>```
>Subistituindo o `IMAGE ID` pelo código da imagem
>
>**Para verificar se o container está em exceução** você pode executar o seguinte comando:
>
>```
>$ docker container ls --all
>```
>
> Caso queira **parar um container**, basta executar o comando:
>```
>$ docker stop <CONTAINER ID>
>```
>Subistituindo o `CONTAINER ID` pelo ID do conatiner
>
>
> Caso queira **destruir um conatiner**, basta executar o comando:
>```
>$ docker rm <CONTAINER ID>
>```
>Para mais comandos, veja a [documentação do docker](https://docs.docker.com/engine/reference/run/).