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
    if request.method == 'POST':
        dados = request.json
        nome = dados.get('nome')
        whatsapp = dados.get('whatsapp')
        dia = dados.get('dia')
        horario = dados.get('horario')
        tipo_cilio = dados.get('tipo_cilio')
        
        novo_dado = Dados(nome=nome, whatsapp=whatsapp, dia=dia, horario=horario, tipo_cilio=tipo_cilio)
        db.session.add(novo_dado)
        db.session.commit()

        return 'Dados recebidos e salvos com sucesso!'

if __name__ == '__main__':
    db.create_all()
    app.run(host='192.168.10.20', port=3001)
