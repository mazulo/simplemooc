simplemooc
==========

Projeto do curso [Python na Web com Django (Python 3)](http://pycursos.com/django/), ministrado pelo [Gileno Filho](https://github.com/gileno).

Como o nome do curso já indica, este projeto foi desenvolvido usando Python 3, e django na sua versão 1.6.

Para preparar sua máquina para rodar o projeto vai ser bem simples.

Primeiramente você terá que criar uma nova env e ativá-la (caso não saiba do que se trata, leia esse [post](blog.dunderlabs.com/criando-seu-ambiente-para-desenvolvimento-web-com-django.html) para mais informações).

Env criada e ativada, vamos instalar as dependências do projeto:

````shell
$ pip install -r requirements.txt
````

Em seguida, crie um arquivo chamado `local_settings.py` no mesmo diretório onde se encontra o `settings.py`, e adicione o seguinte código:

````python
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True

TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)
````

Criado o arquivo, você agora irá criar as tabelas no banco de dados, usando o seguinte comando:

````shell
$ python manage.py syncdb
````

Durante o comando, ele vai não só criar as tabelas, mas também criar um superusuário. Então, forneça as informações que ele pedir (não precisa ser um e-mail válido).

Ao finalizar, basta rodar o servidor local, e acessar no seu navegador:

````shell
$ python manage.py runserver
````

Por padrão, ele vai rodar no endereço 127.0.0.1 na porta 8000. Ou seja, para acessar basta rodar o servidor e acessar http://127.0.0.1:8000/

E é isso. :) Dúvidas só mandar um e-mail ou abrir uma issue neste repositório.
