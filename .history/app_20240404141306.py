from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# Criar uma conexão com o banco de dados
conn = sqlite3.connect('dados.db', check_same_thread=False)
c = conn.cursor()

# Criar a tabela se ela não existir
c.execute('''CREATE TABLE IF NOT EXISTS dados (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(50),
    whatsapp VARCHAR(12),
    dia VARCHAR(10),
    horario VARCHAR(10),
    tipo_cilio VARCHAR(20)
)''')

@app.route('/dados', methods=['GET'])
def get_dados():
    c.execute('SELECT * FROM dados')
    rows = c.fetchall()
    
    # Adicionar um ID antes do número
    dados_formatados = []
    for row in rows:
        id = row[0]
        dados = list(row[1:])
        dados.insert(0, id)
        
        dados_dict = {
            "id": dados[0],
            "nome": dados[1],
            "whatsapp": dados[2],
            "data": dados[3],
            "hora": dados[4],
            "modelo do cilio": dados[5]
        }
        
        dados_formatados.append(dados_dict)
    
    return jsonify(dados_formatados), 200


@app.route('/dados', methods=['POST'])
def save_dados():
    novo_dado = request.json
    c.execute("INSERT INTO dados (nome, whatsapp, dia, horario, tipo_cilio) VALUES (?, ?, ?, ?, ?)",
              (novo_dado['nome'], novo_dado['whatsapp'], novo_dado['dia'], novo_dado['horario'], novo_dado['tipo_cilio']))
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
    c.execute("UPDATE dados SET nome=?, whatsapp=?, dia=?, horario=?, tipo_cilio=? WHERE id=?",
              (novo_dado['nome'], novo_dado['whatsapp'], novo_dado['dia'], novo_dado['horario'], novo_dado['tipo_cilio'], index))
    conn.commit()
    response = jsonify({"message": "Dado atualizado com sucesso"})
    return response, 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
