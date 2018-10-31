from flask import Flask, jsonify, render_template
from pymongo import MongoClient
import requests

con = MongoClient()
db = con['projeto']

app = Flask(__name__)

@app.route('/')
def index():
    mensagem = {'mensagem': "minha primeira api rest"}
    return jsonify(mensagem)

@app.route('/usuarios')
def usuarios():
    for x in db.usuarios.find():
        usuarios.append(x)
    return jsonify(usuarios)

@app.route('/cep/<busca>')
def clonaapi(busca):
    date = requests.get('https://viacep.com.br/ws/{}/json/'.format(busca))
    return jsonify(date.json())

@app.route('/exemplo')
def exemplohtml():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

#. veenv bin activate