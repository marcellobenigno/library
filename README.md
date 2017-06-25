# Biblioteca Django Bootstrap

**Biblioteca Django** é um projeto que visa experimentar, explorar e colocar em práticas os 
recursos do  Django com o Twitter Bootstrap.

## Como desenvolver?

* Clone o repositório.
* Crie um Banco de Dados no PostgreSQL
* Crie um virtualenv com Python 3.5.0
* Ative o virtualenv.
* Instale as dependências.
* Configure a instância com o `.env`.
* Execute as migrações no banco de dados.
* Execute os testes.

```console
mkdir library_src && cd library_src
git clone https://github.com/marcellobenigno/library.git
createdb library
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements/dev.txt
python contrib/env_gen.py
python manage.py makemigrations
python manage.py migrate
python manage.py test
```