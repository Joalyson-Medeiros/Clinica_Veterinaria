
from datetime import datetime

class Usuario:
    def __init__(self, nome, cpf, telefone, email, endereco, data_cadastro):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.data_cadastro = data_cadastro

class Cliente(Usuario):
    def __init__(self, nome, cpf, telefone, email, endereco, data_cadastro):
        super().__init__(nome, cpf, telefone, email, endereco, data_cadastro)
        self.caixa_msgs = []
        self.historico_pagamento = []
        self.animais = []

class Funcionario(Usuario):
    def __init__(self, salario, funcao, horario, escala, login, senha, matricula, nome, cpf, telefone, email, endereco, data_cadastro):
        super().__init__(nome, cpf, telefone, email, endereco, data_cadastro)
        self.salario = salario
        self.funcao = funcao
        self.horario = horario
        self.escala = escala
        self.login = login
        self.senha = senha
        self.matricula = matricula
        self.historico_ferias = []

class Animal:
    def __init__(self, nome, idade, especie, raca, porte, dono_cpf, matricula, vacinacao):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.raca = raca
        self.porte = porte
        self.dono_cpf = dono_cpf
        self.matricula = matricula
        self.vacinacao = vacinacao
        self.vacinas = []
        self.historico_vacina = []

class Pagamento:
    def __init__(self, forma, parcelamento, valor, situacao):
        self.forma = forma
        self.parcelamento = parcelamento
        self.valor = valor
        self.situacao = situacao

class Atendimento:
    def __init__(self, data, hora, animal, tutor, sintoma, pagamento, situacao, ficha):
        self.data = data
        self.hora = hora
        self.animal = animal
        self.tutor = tutor
        self.sintoma = sintoma
        self.pagamento = pagamento
        self.situacao = situacao
        self.ficha = ficha

class Medicamento:
    def __init__(self, nome, fabricante, quantidade, validade, valor):
        self.nome = nome
        self.fabricante = fabricante
        self.quantidade = quantidade
        self.validade = validade
        self.valor = valor

class Vacina(Medicamento):
    def __init__(self, nome, fabricante, quantidade, validade, valor, situacao):
        super().__init__(nome, fabricante, quantidade, validade, valor)
        self.situacao = situacao

class Exame:
    def __init__(self, paciente, responsavel, profissional, sintoma, dataExame, diagnostico, dataDiagnostico, medicacao, situacao):
        self.paciente = paciente
        self.responsavel = responsavel
        self.profissional = profissional
        self.sintoma = sintoma
        self.dataExame = dataExame
        self.diagnostico = diagnostico
        self.dataDiagnostico = dataDiagnostico
        self.medicacao = medicacao
        self.situacao = situacao

class Clinica:
    def __init__(self):
        self.clientes = []
        self.funcionarios = []
        self.consultas = []
        self.exames_realizados = []
        self.animais = []

    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def cadastrar_animal(self, animal):
        self.animais.append(animal)

    def cadastrar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_clientes(self):
        return self.clientes

    def listar_animais(self):
        return self.animais

    def listar_funcionarios(self):
        return self.funcionarios

    def buscar_animais_por_nome_cpf(self):
        self.animais()

    def agendar_consulta(self, consulta):
        self.consultas.append(consulta)

    def cancelar_consulta(self, consulta):
        self.consultas.remove(consulta)

    def realizar_exame(self, exame):
        self.exames_realizados.append(exame)

    def resultados_exames(self):
        return self.exames_realizados

clinica = Clinica()

    # ================= CADASTRO =========================


def cadastrar_cliente(clinica):
    nome = str(input("\nInforme o nome: "))
    cpf = str(input("Informe o CPF: "))
    telefone = str(input("Informe o telefone: "))
    email = str(input("Informe o e-mail: "))
    endereco = str(input("Informe o endereço: "))    

    if any(cliente.cpf == cpf for cliente in clinica.clientes):
        print(f"\nCliente já cadastrado.")
        return

    cliente = Cliente(nome, cpf, telefone, email, endereco, data_cadastro=datetime.today())
    clinica.cadastrar_cliente(cliente)
    print(f"\nCliente {cliente.nome} com CPF {cliente.cpf}, cadastro realizado com sucesso!")


def cadastrar_animal(clinica):
    nome = str(input("\nInforme o nome: "))
    idade = int(input("Informe a idade: "))
    especie = str(input("Informe a espécie: "))
    raca = str(input("Informe a raça: "))
    porte = str(input("Informe o porte do animal: "))
    dono_cpf = str(input("Informe o cpf do dono: "))

    cliente = next((cliente for cliente in clinica.clientes if cliente.cpf == dono_cpf), None)

    if not cliente:
        print(f"\nCliente com o CPF: {dono_cpf} não encontrado. Por favor, cadastre cliente antes de associar o animal.")
        return

    animal = Animal(nome, idade, especie, raca, porte, dono_cpf, matricula=len(cliente.animais) + 1, vacinacao = "Atualizada")
    clinica.cadastrar_animal(animal)
    cliente.animais.append(animal)
    print(f"\nAnimal {animal.nome} cadastrado com sucesso para cliente {cliente.nome} com CPF {cliente.cpf}.")

def cadastrar_funcionario(clinica):
    nome = str(input("\nInforme o nome: "))
    cpf = str(input("Informe o CPF: "))
    telefone = str(input("Informe o telefone: "))
    email = str(input("Informe o e-mail: "))
    endereco = str(input("Informe o endereço: "))
    data_cadastro = str(input("Informe o data: "))
    salario = float(input("Informe o salário: "))
    funcao = str(input("Informe a função: "))
    horario = str(input("Informe o horário: "))
    escala = str(input("Informe a escala: "))
    login = str(input("Informe o login: "))
    senha = str(input("Informe a senha: "))
    if cpf in clinica.funcionarios:
        print(f"\nFuncionário já cadastrado.")
        return
    funcionario = Funcionario(nome, cpf, telefone, email,endereco, data_cadastro, salario, funcao, horario, escala, login,senha, matricula=len(clinica.funcionários)+1)
    clinica.cadastrar_funcionario(funcionario)
    print(f"\nFuncionário {funcionario.nome} com CPF{funcionario.cpf}, cadastro realizado com sucesso!")

def listar_clientes(clinica):
    if len(clinica.clientes) == 0:
        print("\nNenhum cliente cadastrado até o momento.")
        return

    print('\n{:=^110}'.format(' CLIENTES CADASTRADOS '))
    print('\n{:=^110}'.format(''))            
    for cliente in clinica.clientes:
        print(f"Nome: {cliente.nome} | Telefone: {cliente.telefone}")
        print('{:-^110}'.format(' PETS VINCULADOS '))
        if len(cliente.animais) == 0:
            print(f"\nO cliente não possui pets.")
            print('{:=^110}'.format(''))            
            return
        for animal in cliente.animais:            
            print(f"Nome: {animal.nome} | Vacinas: {animal.vacinacao}")
        print('{:=^110}'.format(''))        

def listar_animais(self):
    if len(self.animais) == 0:
        print("\nNenhum animal cadastrado até o momento.")
    else:
        print('\n{:=^110}'.format(' ANIMAIS CADASTRADOS '))
        for animal in self.animais:
            print(f"Matrícula: {animal.matricula} | Nome: {animal.nome} | Espécie: {animal.especie} | Raça: {animal.raca} | Idade: {animal.idade} meses | Porte: {animal.porte} | Dono: {animal.dono}\n")
            print('\n{:-^110}'.format(''))
            print(f"\nVacinas: {animal.vacinas}")
            print('\n{:-^110}'.format(''))
        print('{:=^110}'.format(''))

def listar_funcionarios(clinica):
    if len(clinica.funcionarios) == 0:
        print("\nNenhum funcionário cadastrado até o momento.")
        return
    print('\n{:=^110}'.format(' FUNCONÁRIOS CADASTRADOS '))
    for funcionario in clinica.funcionarios:
        print(f"Matrícula: {funcionario.matricula} | Nome: {funcionario.nome} | CPF: {funcionario.cpf} | Função: {funcionario.funcao}\n")
        print('{:=^110}'.format(''))

def buscar_animal_por_nome_cpf(clinica):
    cpf = input("Informe o CPF do dono do animal: ")
    nome = input("Informe o nome do animal: ")

    for animal in clinica.animais:
        if animal.nome == nome and animal.cpf_dono == cpf:
            return animal

    print(f"Não foi possível localizar o animal com os dados inseridos, se certifique que pelo menos um dos dados sejam correspondentes.\n")

    # for cliente in clinica.clientes:
    #     if cliente.cpf == cpf:
    #         for animal in cliente.animais:
    #             if animal.nome == nome:
    #                 print('\n{:=^110}'.format(' DADOS DO ANIMAL '))
    #                 print(f'Nome: {animal.nome}')
    #                 print(f'Idade: {animal.idade}')
    #                 print(f'Espécie: {animal.especie}')
    #                 print(f'Raça: {animal.raca}')
    #                 print(f'Porte: {animal.porte}')
    #                 print('{:=^110}'.format(' DADOS DO DONO '))
    #                 print(f'Nome: {cliente.nome}')
    #                 print(f'CPF: {cliente.cpf}')
    #                 print('{:=^110}'.format(''))
    #                 return
    #         print(
    #             f'Não foi encontrado animal com o nome {nome}, vinculado ao cliente de {cpf}.')
    #         return
    # print(f'Não foi encontrado nenhum cliente com CPF: {cpf}.')

def realizar_agendamento(clinica):
    matricula_animal = int(input("\nInforme a matrícula do animal: "))
    animal = None
    for a in clinica.animais:
        if a.matricula == matricula_animal:
            animal = a
            break
    if animal is None:
        print(
            f"\nAnimal com matrícula {matricula_animal} não encontrado. Por favor, cadastre o animal antes de agendar uma consulta.")
        return
    data = str(input("Digite a data da consulta (DD/MM/YYYY): "))
    hora = str(input("Digite a hora da consulta (HH:MM): "))
    animal_matricula = int(input("Digite a matricula do paciente: "))
    dono_cpf = str(input("Digite o CPF do tutor: "))
    sintoma = str(input("Digite quaisquer sintomas: "))
    pagamento = float(input("Digite a pagamento: "))
    atendimento = Atendimento(data, hora, animal_matricula, dono_cpf,
                            sintoma, pagamento, situacao=False, ficha=len(clinica.consultas)+1)
    clinica.agendar_consulta(atendimento)
    print(
        f"\nAgendamento para o animal {animal.nome} marcado para o dia {data} às {hora}.")

def cancelar_agendamento(clinica):
    cancela_matricula = int(input("\nInforme a matrícula do animal: "))
    cancela_data = str(input("O agendamento está para que dia (DD/MM/YYYY)? "))
    cancela_horario = str(input("E que horas (HH:MM)? "))
    consulta = None
    for c in clinica.consultas:
        if c.animal.matricula == cancela_matricula and c.hora == cancela_horario and c.data == cancela_data:
            consulta = c
            break
    if consulta is None:
        print(
            f"\nNão há agendamento previsto de um animal com a matrícula {cancela_matricula}.")
        return
    print(
        f"\nAgendamento para {c.animal.nome} no dia {c.data} às {c.hora} cancelado.")
    clinica.cancelar_consulta(consulta)


def realizar_exames(clinica):
    matricula_animal = int(input("\nDigite a matrícula do animal: "))
    animal = None
    for a in clinica.animais:
        if a.matricula == matricula_animal:
            animal = a
            break
    if animal is None:
        print(f"\nAnimal com matrícula {matricula_animal} não encontrado.")
        return
    diagnostico = str(input(f"Informe o diagnostico do exame: "))
    exame = Exame(animal, diagnostico)
    clinica.realizar_exame(exame)
    print(f"\nExame do animal {animal.nome} realizado com sucesso.")


def resultados_exames(clinica):
    if len(clinica.exames_realizados) == 0:
        print("\nNenhum exame foi realizado.")
    else:
        print('\n{:=^110}'.format(' RESULTADOS DOS EXAMES REALIZADOS '))
        for exame in clinica.exames_realizados:
            print(
                f"Animal: {exame.animal.nome} | Diagnóstico: {exame.diagnostico}")
        print('{:=^110}'.format(''))



while True:
    print('\n{:=^110}'.format(' ESCOLHA UMA OPÇÃO '))
    print("1 - Cadastrar cliente")
    print("2 - Cadastrar animal")
    print("3 - Cadastrar funcionário")
    print("4 - Listar clientes")
    print("5 - Listar animais")
    print("6 - Listar funcionarios")
    print("7 - Busca animais por nome e cpf do tutor)")
    print("8 - Realizar agendamento")
    print("9 - Cancelar agendamento")
    print("10 - Realizar exame")
    print("11 - Resultados de exames")
    print("12 - Consultar pagamento")
    print("0 - Sair")
    print('{:=^110}'.format(''))
    opcao = int(input("Escolhida uma opção: "))
    print('{:=^110}'.format(''))
    if opcao == 1:
        cadastrar_cliente(clinica)
    elif opcao == 2:
        cadastrar_animal(clinica)
    elif opcao == 3:
        cadastrar_funcionario(clinica)
    elif opcao == 4:
        listar_clientes(clinica)
    elif opcao == 5:
        listar_animais(clinica)
    elif opcao == 6:
        listar_funcionarios(clinica)
    elif opcao == 7:
        buscar_animal_por_nome_cpf(clinica)
    elif opcao == 8:
        realizar_agendamento(clinica)
    elif opcao == 9:
        cancelar_agendamento(clinica)
    elif opcao == 10:
        realizar_exames(clinica)
    elif opcao == 11:
        resultados_exames(clinica)
    elif opcao == 12:
        consultar_pagamento(clinica)
    elif opcao == 0:
        print("\nEncerrando o programa...\n")
        break
    else:
        print("Opção inválida. Tente novamente.")
        continue
