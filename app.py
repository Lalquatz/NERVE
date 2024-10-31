#importando a biblioteca do flask para fazer um si
from flask import Flask, render_template, request, redirect, url_for

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
def cadastroj():
    return render_template('cadastroj.html')

@app.route('/cadastroe')
def cadastroe():
    return render_template('cadastroe.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/inicioj')
def inicioj():
    return render_template('inicioj.html')

@app.route('/inicioe')
def inicioe():
    return render_template('inicioe.html')

@app.route('/jogadorerro')
def jogadorerro():
    return render_template('jogadorerro.html')

@app.route('/espectadorerro')
def espectadorerro():
    return render_template('espectadorerro.html')

@app.route('/verificar-loginj', methods=['POST'])
def verificar_loginj():
    username = request.form['username']
    password = request.form['password']

    if username in usuarios and usuarios[username] == password:
        return redirect(url_for("inicioj"))
    else:
        return redirect(url_for("jogadorerro"))
    
@app.route('/verificar-logine', methods=['POST'])
def verificar_logine():
    username = request.form['username']
    password = request.form['password']

    if username in usuarios and usuarios[username] == password:
        return redirect(url_for("inicioe"))
    else:
        return redirect(url_for("espectadorerro"))

#parte principal do programa em python
if __name__ == '__main__':
    app.run(debug=True)