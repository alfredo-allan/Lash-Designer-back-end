from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'
db = SQLAlchemy(app)

class Dados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    whatsapp = db.Column(db.String(12))
    dia = db.Column(db.String(10))
    horario = db.Column(db.String(10))
    tipo_cilio = db.Column(db.String(20))

@app.route('/dados', methods=['POST'])
def receber_dados():
    with app.app_context():
        if request.method == 'POST':
            dados = request.json
            print(dados)  # Imprime os dados recebidos do JSON

            nome = dados.get('nome')
            whatsapp = dados.get('whatsapp')
            dia = dados.get('dia')
            horario = dados.get('horario')
            tipo_cilio = dados.get('tipo_cilio')

            print(nome, whatsapp, dia, horario, tipo_cilio)  # Imprime os dados extraídos do JSON

            novo_dado = Dados(nome=nome, whatsapp=whatsapp, dia=dia, horario=horario, tipo_cilio=tipo_cilio)
            db.session.add(novo_dado)
            db.session.commit()

            return 'Dados recebidos e salvos com sucesso!'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(host='192.168.10.20', port=8000)
