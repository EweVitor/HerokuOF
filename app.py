from flask import Flask, render_template
TEMPLATE = './templates'
STATIC = './static'

app = Flask(__name__, template_folder=TEMPLATE, static_folder=STATIC)

@app.route('/')
def olaMundo():
    return 'ola mundo'

@app.route('/index')
def index():
    nome = 'ewerton'
    lista = ['https://www.youtube.com/embed/9y9HQu25k6c']
    return render_template('index.html', nome = nome, lista = lista)

app.run(host='0.0.0.0', port=5000)