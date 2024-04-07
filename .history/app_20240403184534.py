from flask import Flask, request, jsonify

app = Flask(__name__)
dados = []

# Função para adicionar cabeçalhos CORS às respostas
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

# Rota para retornar todos os dados
@app.route('/dados', methods=['GET'])
def get_dados():
    response = jsonify(dados)
    return add_cors_headers(response)

# Rota para salvar os dados
@app.route('/dados', methods=['POST'])
def save_dados():
    novo_dado = request.json
    dados.append(novo_dado)
    response = jsonify({"message": "Dados salvos com sucesso"})
    return add_cors_headers(response), 201

# Rota para deletar os dados
@app.route('/dados/<int:index>', methods=['DELETE'])
def delete_dados(index):
    if index < len(dados):
        del dados[index]
        response = jsonify({"message": "Dado deletado com sucesso"})
        return add_cors_headers(response), 200
    else:
        response = jsonify({"message": "Índice fora do range"})
        return add_cors_headers(response), 404

# Rota para atualizar os dados
@app.route('/dados/<int:index>', methods=['PUT'])
def update_dados(index):
    if index < len(dados):
        dados[index] = request.json
        response = jsonify({"message": "Dado atualizado com sucesso"})
        return add_cors_headers(response), 200
    else:
        response = jsonify({"message": "Índice fora do range"})
        return add_cors_headers(response), 404

if __name__ == '__main__':
    app.run(host='192.168.10.20', port=8000)
