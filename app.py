from usuario import Usuario
from flask import Flask, render_template, request

from config import db
from usuario import Usuario
TEMPLATE = './templates'
STATIC = './static'

app = Flask(__name__, template_folder=TEMPLATE, static_folder=STATIC)

#@app.route('/')
#def olaMundo():
#   return 'ola mundo'

# configuração de dados 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./dados.db'
db.init_app(app)

with app.app_context():
    db.create_all()

#definição das rotas
@app.route('/')
def cadastrarUsuario(): 
    return  render_template('cadastro.html')

@app.route('/index')
def index():
    nome = 'ewerton'
    lista = ['https://www.youtube.com/embed/9y9HQu25k6c']
    return render_template('index.html', nome = nome, lista = lista)

@app.route('/cadastro' ,methods=['POST'])
def cadastro():

    nome = request.form.get('nome')
    email = request.form.get('email')
    usuarios = Usuario.query.all()
    for u in usuarios:
        if u.email == email: 
            return 'Email ja cadastrado'

    usuario = Usuario(nome,email)
    db.session.add(usuario)
    db.session.commit()
    return 'Usuario cadastrado' 

@app.route('/listaUsuario')
def lista():
    usuarios  = Usuario.query.all()
    return render_template('listaUsuario.html', usuarios = usuarios)

#app.run(host='0.0.0.0', port=5000)