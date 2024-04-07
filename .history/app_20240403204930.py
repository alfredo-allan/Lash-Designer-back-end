from flask import Flask, request, jsonify

app = Flask(__name__)
dados = []

def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response


@app.route('/dados', methods=['GET', 'OPTIONS'])
def get_dados():
    response = jsonify(dados)
    return add_cors_headers(response)

@app.route('/dados', methods=['POST', 'OPTIONS'])
def save_dados():
    novo_dado = request.json
    dados.append(novo_dado)
    response = jsonify({"message": "Dados salvos com sucesso"})
    return add_cors_headers(response), 201
def options_response():
    
    response = make_response()
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response

@app.route('/dados/<int:index>', methods=['DELETE', 'OPTIONS'])
def delete_dados(index):
    if index < len(dados):
        del dados[index]
        response = jsonify({"message": "Dado deletado com sucesso"})
        return add_cors_headers(response), 200
    else:
        response = jsonify({"message": "Índice fora do range"})
        return add_cors_headers(response), 404

@app.route('/dados/<int:index>', methods=['PUT', 'OPTIONS'])
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
