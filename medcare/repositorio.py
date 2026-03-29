# repositorio.py
import json
import os
from medcare.models import criar_medicamento

arquivo_padrao = "medicamentos.json"


def _carregar_dados(caminho=arquivo_padrao):
    if not os.path.exists(caminho):
        return []
    if os.path.getsize(caminho) == 0:
        return []
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)


def _salvar_dados(lista, caminho=arquivo_padrao):
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=2)


def _proximo_id(lista):
    if not lista:
        return 1
    ids = []
    for med in lista:
        ids.append(med["id"])
    return max(ids) + 1


def adicionar(nome, paciente, horario, frequencia, estoque,
              observacoes=None, caminho=arquivo_padrao):
    lista = _carregar_dados(caminho)
    novo = criar_medicamento(
        id=_proximo_id(lista),
        nome=nome,
        paciente=paciente,
        horario=horario,
        frequencia=frequencia,
        estoque=estoque,
        observacoes=observacoes,
    )

    lista.append(novo)
    _salvar_dados(lista, caminho)
    return novo


def listar(caminho=arquivo_padrao):
    return _carregar_dados(caminho)


def buscar_por_paciente(paciente, caminho=arquivo_padrao):
    lista = _carregar_dados(caminho)
    paciente_lower = paciente.lower()
    resultado = []
    for med in lista:
        if paciente_lower in med["paciente"].lower():
            resultado.append(med)
    return resultado


def buscar_por_id(id_, caminho=arquivo_padrao):
    lista = _carregar_dados(caminho)
    for med in lista:
        if med["id"] == id_:
            return med
    return None


def atualizar_estoque(id_, novo_estoque, caminho=arquivo_padrao):
    lista = _carregar_dados(caminho)
    for med in lista:
        if med["id"] == id_:
            med["estoque"] = novo_estoque
            _salvar_dados(lista, caminho)
            return True
    return False


def remover(id_, caminho=arquivo_padrao):
    lista = _carregar_dados(caminho)
    nova_lista = []
    for med in lista:
        if med["id"] != id_:
            nova_lista.append(med)
    if len(nova_lista) == len(lista):
        return False
    _salvar_dados(nova_lista, caminho)
    return True


def alertas_estoque_baixo(limite=5, caminho=arquivo_padrao):
    lista = _carregar_dados(caminho)
    resultado = []
    for med in lista:
        if med["estoque"] < limite:
            resultado.append(med)
    return resultado
