import urllib.request
import json


def buscar_cep(cep):
    cep = cep.replace('-', '').strip()
    if len(cep) != 8 or not cep.isdigit():
        return None
    url = f'https://viacep.com.br/ws/{cep}/json/'
    try:
        with urllib.request.urlopen(url, timeout=5) as resposta:
            dados = json.loads(resposta.read().decode())
        if 'erro' in dados:
            return None
        return {
            'cep': dados.get('cep', ''),
            'cidade': dados.get('localidade', ''),
            'estado': dados.get('uf', ''),
        }
    except Exception:
        return None
