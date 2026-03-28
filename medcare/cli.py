import medcare.repositorio as repositorio
from medcare.validacoes import (
    validar_nome,
    validar_horario,
    validar_frequencia,
    validar_estoque,
)

linha = "=" * 55
linha_fina = "-" * 55


def cabecalho():
    print(linha)
    print("  💊  MedCare Idosos - Controle de Medicamentos  💊")
    print(linha)


def menu_principal():
    print('\n' + linha_fina)
    print(' [1] Cadastrar medicamento')
    print(' [2] Listar todos os medicamentos')
    print(' [3] Buscar por paciente')
    print(' [4] Atualizar estoque')
    print(' [5] Remover medicamento')
    print(' [6] Alertas de estoque baixo')
    print(' [0] Sair')
    print(linha_fina)


def exibir_medicamento(med):
    if med["estoque"] < 5:
        alerta = " ⚠️ ESTOQUE BAIXO!"
    else:
        alerta = ''
    print(f'\n ID         : {med['id']}')
    print(f' Nome       : {med['nome']}')
    print(f' Paciente   : {med['paciente']}')
    print(f' Horário    : {med['horario']}')
    print(f' Frequência : {med['frequencia']}')
    print(f' Estoque    : {med['estoque']} unidade(s){alerta}')
    if med['observacoes']:
        print(f' Obs.       : {med['observacoes']}')


def cadastrar():
    print('\n📝 Cadastro de Medicamento')
    print(linha_fina)
    try:
        nome = validar_nome(input(' Nome do medicamento : '))
        paciente = validar_nome(input(' Nome do paciente : '))
        horario = validar_horario(input(' Horário (HH:MM) : '))
        frequencia = validar_frequencia(input(' Frequência (diaria/semanal/mensal): '))
        estoque = validar_estoque(input(' Quantidade em estoque: '))
        obs = input(' Observações (opicional, Enter para pular): ').strip()

        med = repositorio.adicionar(
            nome=nome,
            paciente=paciente,
            horario=horario,
            frequencia=frequencia,
            estoque=estoque,
            observacoes=obs if obs else None,
        )
        print(f'\n✅ Medicamento cadastrado com sucesso! (ID: {med['id']})')

    except ValueError as e:
        print(f'\n❌ Erro: {e}')


def listar():
    medicamentos = repositorio.listar()
    print(f'\n📋 Medicamentos cadastrados ({len(medicamentos)} no total)')
    print(linha_fina)

    if not medicamentos:
        print(' Nenhum medicamento cadastrado ainda.')
        return
    for med in medicamentos:
        exibir_medicamento(med)
        print(linha_fina)


def buscar_paciente():
    nome = input('\n🔍 Nome do paciente para buscar: ').strip()

    if not nome:
        print('❌ Nome não pode ser vazio.')
        return

    resultados = repositorio.buscar_por_paciente(nome)
    print(f'\n {len(resultados)} resultado(s) encontrado(s):')
    print(linha_fina)

    if not resultados:
        print(' Nenhum medicamento encontrado para esse paciente.')
        return
    for med in resultados:
        exibir_medicamento(med)
        print(linha_fina)


def atualizar_estoque():
    print('\n🔄 Atualizar Estoque')
    try:
        id_ = int(input(' ID do medicamento: '))
        med = repositorio.buscar_por_id(id_)

        if not med:
            print(f'❌ Medicamento com ID {id_} não encontrado.')
            return

        print(f' Medicamento: {med['nome']} | Paciente: {med['paciente']}')
        print(f' Estoque atual: {med['estoque']}')

        novo = validar_estoque(input(' Novo estoque: '))
        repositorio.atualizar_estoque(id_, novo)
        print('✅ Estoque atualizado com sucesso!')

    except ValueError as e:
        print(f'❌ Erro: {e}')


def remover():
    print('\n🗑️ Remover Medicamento')
    try:
        id_ = int(input(' ID do medicamento a remover: '))
        med = repositorio.buscar_por_id(id_)

        if not med:
            print(f'❌ Medicamento com ID {id_} não encontrado.')
            return

        print(f' Medicamento: {med['nome']} | Paciente: {med['paciente']}')
        confirma = input(' Confirmar remoção? (s/n): ').strip().lower()

        if confirma == 's':
            repositorio.remover(id_)
            print('✅ Medicamento removido com sucesso!')
        else:
            print(' Operação cancelada.')

    except ValueError:
        print('❌ ID inválido.')


def alertas():
    lista = repositorio.alertas_estoque_baixo()
    print('\n⚠️ Alertas de Estoque Baixo (menos de 5 unidades)')
    print(linha_fina)

    if not lista:
        print(' ✅ Todos os medicamentos estão com estoque adequado.')
        return
    for med in lista:
        exibir_medicamento(med)
        print(linha_fina)


def executar():
    cabecalho()
    while True:
        menu_principal()
        opcao = input(' Escolha uma opção: ').strip()
        if opcao == '1':
            cadastrar()
        elif opcao == '2':
            listar()
        elif opcao == '3':
            buscar_paciente()
        elif opcao == '4':
            atualizar_estoque()
        elif opcao == '5':
            remover()
        elif opcao == '6':
            alertas()
        elif opcao == '0':
            print('\n👋 Até logo! Cuide bem da saúde.\n')
            break
        else:
            print('❌ Opção inválida. Tente novamente.')


if __name__ == "__main__":
    executar()
