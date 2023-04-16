from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    numero_cupom_gabriel = 0
    return render_template('index.html', numero_cupom_gabriel=numero_cupom_gabriel)

@app.route('/cupom', methods=['POST'])
def atualizar_cupom():
    nome_cupom = request.form.get('nome_cupom')
    if nome_cupom == 'gabriel':
        numero_cupom_gabriel += 1
    return jsonify({'mensagem': 'Cupom atualizado com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)
