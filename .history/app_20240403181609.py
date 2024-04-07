from flask import Flask, request, jsonify

app = Flask(__name__)
dados = []

# Rota para retornar todos os dados
@app.route('/dados', methods=['GET'])
def get_dados():
    return jsonify(dados)

# Rota para salvar os dados
@app.route('/dados', methods=['POST'])
def save_dados():
    novo_dado = request.json
    dados.append(novo_dado)
    return "Dados salvos com sucesso", 201

# Rota para deletar os dados
@app.route('/dados/<int:index>', methods=['DELETE'])
def delete_dados(index):
    if index < len(dados):
        del dados[index]
        return "Dado deletado com sucesso", 200
    else:
        return "Índice fora do range", 404

# Rota para atualizar os dados
@app.route('/dados/<int:index>', methods=['PUT'])
def update_dados(index):
    if index < len(dados):
        dados[index] = request.json
        return "Dado atualizado com sucesso", 200
    else:
        return "Índice fora do range", 404

if __name__ == '__main__':
    app.run(host='192.168.10.20', port=8000)
