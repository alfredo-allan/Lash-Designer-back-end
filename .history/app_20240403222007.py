from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# Criar uma conexão com o banco de dados
conn = sqlite3.connect('dados.db', check_same_thread=False)
c = conn.cursor()

# Criar a tabela se ela não existir
c.execute('''CREATE TABLE IF NOT EXISTS dados (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, idade INTEGER)''')

@app.route('/dados', methods=['GET'])
def get_dados():
    c.execute('SELECT * FROM dados')
    rows = c.fetchall()
    return jsonify(rows), 200

@app.route('/dados', methods=['POST'])
def save_dados():
    novo_dado = request.json
    c.execute("INSERT INTO dados (nome) VALUES (?, ?)", (novo_dado['nome'])))
    conn.commit()
    response = jsonify({"message": "Dados salvos com sucesso"})
    return response, 201

@app.route('/dados/<int:index>', methods=['DELETE'])
def delete_dados(index):
    c.execute("DELETE FROM dados WHERE id=?", (index,))
    conn.commit()
    response = jsonify({"message": "Dado deletado com sucesso"})
    return response, 200

@app.route('/dados/<int:index>', methods=['PUT'])
def update_dados(index):
    novo_dado = request.json
    c.execute("UPDATE dados SET nome=?, idade=? WHERE id=?", (novo_dado['nome'], novo_dado['idade'], index))
    conn.commit()
    response = jsonify({"message": "Dado atualizado com sucesso"})
    return response, 200

if __name__ == '__main__':
    app.run(host='192.168.10.20', port=8000)
