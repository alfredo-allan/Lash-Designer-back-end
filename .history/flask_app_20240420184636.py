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
    nomePromotor VARCHAR(50),
    nomeCliente VARCHAR(50),
    enderecoCliente VARCHAR(50),
    ean VARCHAR(50),
    descricaoProduto VARCHAR(50),
    dataVencimento VARCHAR(10),
    quantidadeProdutos INTEGER
)''')

@app.route('/salvar-dados', methods=['POST'])
def save_dados():
    novo_dado = request.json
    c.execute("INSERT INTO dados (nomePromotor, nomeCliente, enderecoCliente, ean, descricaoProduto, dataVencimento, quantidadeProdutos) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (novo_dado['nomePromotor'], novo_dado['nomeCliente'], novo_dado['enderecoCliente'], novo_dado['ean'], novo_dado['descricaoProduto'], novo_dado['dataVencimento'], novo_dado['quantidadeProdutos']))
    conn.commit()
    response = jsonify({"message": "Dados salvos com sucesso"})
    return response, 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
