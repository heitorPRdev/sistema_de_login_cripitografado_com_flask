from flask import Flask,render_template, request,flash,redirect
from hashlib import sha256

app = Flask(__name__,template_folder='template')
app.secret_key = b'senha_secreta'
@app.route('/')
def index():
    """Ele mostra o arquivo index.html"""
    
    return render_template('index.html')
@app.route('/cript_login', methods=['POST'])
def login_cripit():
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    senha_cript = sha256(senha.encode()).hexdigest()
    if nome == 'user' and senha_cript == '13493fcc23af5fd609781df0f33e3f19f0cad8149aa3a40f775d415ce11c7c57':#senha == user senha
       return redirect('/profile/')
    else:
        flash('Desculpe, senha ou nome errado(senha = user senha e nome = user)')
        return redirect('/')
@app.route('/profile/')
def profile():
     return render_template('profile.html')
if __name__ == '__main__':
    app.run(debug=True)