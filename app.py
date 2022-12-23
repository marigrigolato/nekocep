import requests
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/", methods=['GET'])
def buscar_cep():

  cep = request.args.get('cep', None)

  address = {}

  if cep:
    r = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

    dados = r.json()

    address = {
      'logradouro': dados['logradouro'],
      'bairro': dados['bairro'],
      'localidade': dados['localidade'],
      'uf': dados['uf'],
      'cep': dados['cep']
    }

  else: 
    address = None

  return render_template("index.html", cep=cep, address=address)
