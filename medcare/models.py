FREQUENCIAS_VALIDAS = ["diaria", "semanal", "mensal"]


def criar_medicamento(
    nome, paciente, horario, frequencia, estoque, observacoes=None, id=None
):
    return {
        "id": id,
        "nome": nome,
        "paciente": paciente,
        "horario": horario,
        "frequencia": frequencia,
        "estoque": estoque,
        "observacoes": observacoes,
    }


def estoque_baixo(medicamento, limite=5):
    return medicamento["estoque"] < limite
