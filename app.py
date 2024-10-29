#importando a biblioteca do flask para fazer um si
from flask import Flask, render_template, request

app =  Flask(__name__)

usuarios = {
    'admin' : 'admin',
    'usuario' : 'senha',
    'leonardo' : '1234',
}

#definindo a rota principal do site
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/jogador')
def jogador():
    return render_template('jogador.html')

@app.route('/espectador')
def espectador():
    return render_template('espectador.html')

@app.route('/cadastroj')
def cadastro():
    return render_template('cadastroj.html')

@app.route('/login')
def login():
    return render_template('login')

@app.route('/verificar-login', methods=['POST'])
def verificar_login():
    return render_template('verificar-login')

#parte principal do programa em python
if __name__ == '__main__':
    app.run(debug=True)