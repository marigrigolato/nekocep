import requests


def buscar_cep(cep):

  r = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
  r.raise_for_status()

  dados = r.json()

  return f"{dados['logradouro']} {dados['bairro']} {dados['localidade']} {dados['uf']} {dados ['cep']}"