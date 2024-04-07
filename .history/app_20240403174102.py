from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from functools import wraps

app = Flask(__name__) 
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'
db = SQLAlchemy(app)

@app.route('/create_admin', methods=['POST'])
def create_admin():
    dados = request.json
    new_password = dados.get('new_password')

    global ADMIN_PASSWORD
    ADMIN_PASSWORD = new_password

    return jsonify({'mensagem': 'Credenciais de administrador criadas com sucesso'}), 200
class Dados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    whatsapp = db.Column(db.String(12))
    dia = db.Column(db.String(10))
    horario = db.Column(db.String(10))
    tipo_cilio = db.Column(db.String(20))

ADMIN_PASSWORD = "sua_senha_administrativa"

def autenticar(password):
    return password == ADMIN_PASSWORD

@app.route('/login', methods=['POST'])
def login():
    dados = request.json
    username = dados.get('username')
password = dados.get('password')
    
    if username == 'admin' and password == ADMIN_PASSWORD:
        token = 'seu_token_de_autenticacao'
        return token, 200
    else:
        return jsonify({'mensagem': 'Credenciais inválidas'}), 401
def require_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')

        if token != 'seu_token_de_autenticacao':
            return jsonify({'mensagem': 'Acesso não autorizado'}), 401

        return func(*args, **kwargs)

    return wrapper

@app.route('/dados', methods=['GET'])
@require_token
def mostrar_dados_protegido():
    return jsonify({'mensagem': 'Esses são os dados protegidos'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(host='192.168.10.20', port=8000)
def require_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        print(token)  # Adicionar essa linha para imprimir o token recebido

        if token != 'seu_token_de_autenticacao':
            return jsonify({'mensagem': 'Acesso não autorizado'}), 401

        return func(*args, **kwargs)

    return wrapper