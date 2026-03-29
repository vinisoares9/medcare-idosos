# validacoes.py
from medcare.models import frequencias_validas


def validar_nome(nome):
    nome = nome.strip()
    if not nome:
        raise ValueError("O nome não pode ser vazio.")
    if len(nome) < 2:
        raise ValueError("O nome deve ter pelo menos 2 caracteres.")
    if len(nome) > 100:
        raise ValueError("O nome não pode ter mais de 100 caracteres.")
    return nome


def validar_horario(horario):
    horario = horario.strip()
    if not horario:
        raise ValueError("O horário não pode ser vazio.")
    partes = horario.split(":")
    if len(partes) != 2:
        raise ValueError("Horário deve estar no formato HH:MM (ex: 08:00).")
    try:
        hora = int(partes[0])
        minuto = int(partes[1])
    except ValueError:
        raise ValueError("Horário deve conter apenas números no formato HH:MM")
    if not (0 <= hora <= 23):
        raise ValueError("Hora deve estar entre 00 e 23.")
    if not (0 <= minuto <= 59):
        raise ValueError("Minuto deve estar entre 00 e 59.")
    return f"{hora:02d}:{minuto:02d}"


def validar_frequencia(frequencia):
    frequencia = frequencia.strip().lower()
    if frequencia not in frequencias_validas:
        raise ValueError(
            f"Frequência inválida. Valores aceitos: {', '.join(frequencias_validas)}."
        )
    return frequencia


def validar_estoque(estoque):
    try:
        estoque = int(estoque)
    except (TypeError, ValueError):
        raise ValueError("Estoque deve ser um número inteiro.")
    if estoque < 0:
        raise ValueError("Estoque não pode ser negativo.")
    return estoque
