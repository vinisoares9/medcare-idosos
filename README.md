# 💊 MedCare Idosos

![CI](https://github.com/vinisoares9/medcare-idosos/actions/workflows/ci.yml/badge.svg)

## Problema Real

O Brasil possui mais de 32 milhões de idosos, muitos deles com doenças crônicas que exigem o uso contínuo de múltiplos medicamentos. A dificuldade de controlar horários, frequências e estoques de remédios é uma realidade para idosos e seus cuidadores, podendo causar esquecimentos, doses erradas ou falta de medicamentos.

## Proposta da Solução

O **MedCare Idosos** é uma aplicação de linha de comando (CLI) que permite cadastrar, listar, buscar e controlar o estoque de medicamentos de pacientes idosos, emitindo alertas quando o estoque está baixo.

## Público-Alvo

- Cuidadores de idosos
- Familiares responsáveis pelo controle de medicamentos
- Profissionais de saúde em ambientes domiciliares

## Funcionalidades Principais

- Cadastrar medicamentos com nome, paciente, horário, frequência e estoque
- Listar todos os medicamentos cadastrados
- Buscar medicamentos por nome do paciente
- Atualizar estoque de um medicamento
- Remover medicamento cadastrado
- Alertas automáticos para medicamentos com estoque baixo

## Tecnologias Utilizadas

- Python 3.14.2
- JSON (armazenamento de dados)
- pytest (testes automatizados)
- flake8 (lint e análise estática)
- GitHub Actions (CI)

## Instruções de Instalação

**1. Clone o repositório:**
```bash
git clone https://github.com/vinisoares9/medcare-idosos.git
cd medcare-idosos
```

**2. Crie e ative o ambiente virtual:**
```bash
python -m venv .venv

# Windows:
.venv\Scripts\activate

# Mac/Linux:
source .venv/bin/activate
```

**3. Instale as dependências:**
```bash
pip install -r requirements.txt
```

## Instruções de Execução
```bash
python main.py
```

## Instruções para Rodar os Testes
```bash
pytest
```

## Instruções para Rodar o Lint
```bash
flake8 --max-line-length=99 medcare/ tests/ main.py
```

## Versão Atual

`1.0.0`

## Autor

Vinicius Ribeiro Soares

## Repositório

[https://github.com/vinisoares9/medcare-idosos](https://github.com/vinisoares9/medcare-idosos)
