# dev-awari-calculadora-imoveis-may-20
Para o deploy no Heroku, dois arquivos de configuração devem ser adicionados ao repositório:
### `requirements.txt`
Este é o arquivo mais importante pois nele há todos os bibliotecas do Python que devem ser instalados no servidor do Heroku. Nele precisamos colocar todas as importações que foram feitas ao longo do desenvolvimento de nosso código como numpy, scikit-learn e Flask. Todas dependências devem ser mencionadas, algumas serão descobertas por tentativa e erro durante o deploy no Heruku. Para nosso app, o conteúdo do arquivo deverá ser o seguinte:
```
Flask==1.1.1
gunicorn==19.9.0
itsdangerous==1.1.0
Jinja2==2.10.1
MarkupSafe==1.1.1
Werkzeug==0.15.5
numpy>=1.9.2
scipy>=0.15.1
scikit-learn>=0.18
lightgbm
```

### `Procfile`
Irá dizer ao Heroku qual é o nome do primeiro arquivo que deve ser executado. Seu conteúdo será o seguinte:
```
web: gunicorn app:app
```
Vamos entender essa sintaxe. `web: gunicorn` vai chamar a biblioteca `gunicorn` que definimos em `requirements.txt` para ser instalado. O mesmo é um servidor HTTP Python WSGI para UNIX bastante leve e amplamente compatível com várias estruturas da web. O que vem em seguida são referentes ao nome do arquivo (que no nosso caso é `app.py`) e o nome da variável dentro do código na qual Flask foi inicializado, que no nosso casso se chama `app` também (dentro da sintaxe `app = Flask(__name__)`). Se por exemplo o nome do arquivo fosse `calculadora_imoveis.py` e o nome da variável no código fosse `meu_app = Flask(__name__)`, a sintaxe passaria a ser: `web: gunicorn calculadora_imoveis:meu_app`.
