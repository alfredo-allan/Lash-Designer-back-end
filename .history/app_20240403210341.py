from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
dados = []

@app.route('/dados', methods=['POST'])
def save_dados():
    novo_dado = request.json
    dados.append(novo_dado)
    response = jsonify({"message": "Dados salvos com sucesso"})
    return response, 201

@app.route('/dados/<int:index>', methods=['DELETE'])
def delete_dados(index):
    if index < len(dados):
        del dados[index]
        response = jsonify({"message": "Dado deletado com sucesso"})
        return response, 200
    else:
        response = jsonify({"message": "Índice fora do range"})
        return response, 404

@app.route('/dados/<int:index>', methods=['PUT'])
def update_dados(index):
    if index < len(dados):
        dados[index] = request.json
        response = jsonify({"message": "Dado atualizado com sucesso"})
        return response, 200
    else:
        response = jsonify({"message": "Índice fora do range"})
        return response, 404

if __name__ == '__main__':
    app.run(host='192.168.10.20', port=8000)
