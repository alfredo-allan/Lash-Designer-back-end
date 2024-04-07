from flask import Flask, request

app = Flask(__name)

@app.route('/dados', methods=['POST'])
def receber_dados():
    if request.method == 'POST':
        dados = request.json
        nome = dados.get('nome')
        whatsapp = dados.get('whatsapp')
        dia = dados.get('dia')
        horario = dados.get('horario')
        tipo_cilio = dados.get('tipo_cilio')

        # Aqui você pode fazer o que quiser com esses dados, como salvá-los em um banco de dados, por exemplo

        return 'Dados recebidos com sucesso!'

if __name__ == '__main__':
    app.run()
