import os
import tempfile
import pytest

from medcare.models import criar_medicamento, estoque_baixo
from medcare.validacoes import (
    validar_nome,
    validar_horario,
    validar_frequencia,
    validar_estoque,
)
import medcare.repositorio as repositorio


@pytest.fixture
def arquivo_temp():
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        caminho = f.name
    yield caminho
    os.unlink(caminho)


def test_criar_medicamento_basico():
    med = criar_medicamento(
        nome='Losartana',
        paciente='João',
        horario='08:00',
        frequencia='diaria',
        estoque=30,
    )
    assert med['nome'] == 'Losartana'
    assert med['paciente'] == 'João'
    assert med['horario'] == '08:00'
    assert med['frequencia'] == 'diaria'
    assert med['estoque'] == 30


def test_estoque_baixo_true():
    med = criar_medicamento('Med', 'Ana', '08:00', 'diaria', estoque=3)
    assert estoque_baixo(med) is True


def test_estoque_baixo_false():
    med = criar_medicamento('Med', 'Ana', '08:00', 'diaria', estoque=10)
    assert estoque_baixo(med) is False


def test_estoque_no_limite_nao_e_baixo():
    med = criar_medicamento('Med', 'Ana', '08:00', 'diaria', estoque=5)
    assert estoque_baixo(med, limite=5) is False


def test_validar_nome_valido():
    assert validar_nome("  Maria  ") == "Maria"


def test_validar_nome_vazio():
    with pytest.raises(ValueError, match='vazio'):
        validar_nome('')


def test_validar_nome_curto():
    with pytest.raises(ValueError, match='2 caracteres'):
        validar_nome('A')


def test_validar_horario_valido():
    assert validar_horario('8:0') == '08:00'


def test_validar_horario_formato_invalido():
    with pytest.raises(ValueError, match='HH:MM'):
        validar_horario('08-00')


def test_validar_horario_hora_invalida():
    with pytest.raises(ValueError, match='entre 00 e 23'):
        validar_horario('25:00')


def test_validar_frequencia_valida():
    assert validar_frequencia('DIARIA') == 'diaria'


def test_validar_frequencia_invalida():
    with pytest.raises(ValueError, match='Frequência inválida'):
        validar_frequencia('quinzenal')


def test_validar_estoque_negativo():
    with pytest.raises(ValueError, match='negativo'):
        validar_estoque(-1)


def test_validar_estoque_texto():
    with pytest.raises(ValueError, match='inteiro'):
        validar_estoque('abc')


def test_adicionar_e_listar(arquivo_temp):
    repositorio.adicionar(
        nome='Losartana',
        paciente='João',
        horario='08:00',
        frequencia='diaria',
        estoque=30,
        caminho=arquivo_temp,
    )
    lista = repositorio.listar(caminho=arquivo_temp)
    assert len(lista) == 1
    assert lista[0]["nome"] == "Losartana"


def test_remover_medicamento(arquivo_temp):
    med = repositorio.adicionar(
        nome='Dipirona',
        paciente='Maria',
        horario='12:00',
        frequencia='diaria',
        estoque=10,
        caminho=arquivo_temp,
    )
    repositorio.remover(med['id'], caminho=arquivo_temp)
    lista = repositorio.listar(caminho=arquivo_temp)
    assert len(lista) == 0


def test_remover_inexistente(arquivo_temp):
    resultado = repositorio.remover(999, caminho=arquivo_temp)
    assert resultado is False


def test_alertas_estoque_baixo(arquivo_temp):
    repositorio.adicionar('Med A', 'Ana', '08:00', 'diaria', estoque=2, caminho=arquivo_temp)
    repositorio.adicionar('Med B', 'Ana', '08:00', 'diaria', estoque=20, caminho=arquivo_temp)
    alertas = repositorio.alertas_estoque_baixo(caminho=arquivo_temp)
    assert len(alertas)
    assert alertas[0]["nome"] == "Med A"
