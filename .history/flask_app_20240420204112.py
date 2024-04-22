from flask import Flask, request

app = Flask(__name__)

@app.route('/salvar-dados', methods=['POST'])
def salvar_dados():
    data = request.json
    # Faça o processamento dos dados recebidos do front-end aqui
    # Por exemplo, salvar os dados no banco de dados

    return "Dados recebidos com sucesso!"

if __name__ == '__main__':
    app.run()