# Kronos
Este projeto é uma base para a criação de um projeto Django usando Docker e PostgreSQL. O objetivo é fornecer uma estrutura inicial para quem deseja criar um projeto Django de forma rápida e eficiente utilizando contêineres, e com o layout do bootstrap 5.

# Tecnologias Utilizadas
Linguagem de Programação: Python
Framework Web: Django
Banco de Dados: PostgreSQL
Containerização: Docker, Docker Compose


# Instruções de Instalação
Pré-requisitos
Certifique-se de ter o Docker e o Docker Compose instalados na sua máquina.

Instalação do Dokcer:
<https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04>

Passos para Instalação
Clone este repositório:

```git
git clone https://github.com/lauf8/django-base.git
```
```bash
cd kronos-2
```

Renomei o arquivo .env copy para suas preferências, como por exemplo

```.env
DEBUG=True
SECRET_KEY=x$_$t$-nv1m%2r%%gvmue#t87uejk!vh-^ajm=94%&w&+l47a^
DB_NAME=kronos
DB_USERNAME=postgres
DB_PASS=2Vyv#%IF7A'0|onOc#OX2d2mk4
DB_PORT=5432
DB_HOST=db
```

Execute o Docker Compose para iniciar os containers:

```dockerfile
docker-compose up --force-recreate 
```


A aplicação estará disponível em http://localhost:8000.

# Instruções de Uso
Acesse a aplicação no navegador através do endereço http://localhost:8000.
O projeto tem as páginas de auth do django já feitas, e um layout moderno para criação de aplicações usando o django templates.

# Licença
Este projeto está licenciado sob a MIT License.
