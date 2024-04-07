from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from functools import wraps

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'
db = SQLAlchemy(app)

class Dados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    whatsapp = db.Column(db.String(12))
    dia = db.Column(db.String(10))
    horario = db.Column(db.String(10))
    tipo_cilio = db.Column(db.String(20))

ADMIN_PASSWORD = "190216"

def autenticar(password):
    return password == ADMIN_PASSWORD

@app.route('/login', methods=['POST'])
def login():
    dados = request.json
    password = dados.get('password')

    if autenticar(password):
        token = 'seu_token_de_autenticacao'
        return jsonify({'token': token}), 200
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
