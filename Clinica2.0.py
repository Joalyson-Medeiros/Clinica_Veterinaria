class Usuario:
    def __init__(self, nome: str, telefone: str, email: str, cpf: str, endereco: str, data_cadastro: str):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cpf = cpf
        self.endereco = endereco
        self.data_cadastro = data_cadastro

class Cliente(Usuario):
    def __init__(self, pets: list, caixa_msgs: list, histrico_pagamento: list):
        super().__init__(nome="", telefone="", email="", cpf="", endereco="", data_cadastro="")
        self.pets = pets
        self.caixa_msgs = caixa_msgs
        self.historico_pagamento = historico_pagamento

class Funcionario(Usuario):
    def __init__(self, salario: float, funcao: str, horario: str, escala: str, login: str, senha: str, historico_ferias: list, matricula: int):
        super().__init__(nome="", telefone="", email="", cpf="", endereco="", data_cadastro="")
        self.salario = salario
        self.funcao = funcao
        self.horario = horario
        self.escala = escala
        self.login = login
        self.senha = senha
        self.historico_ferias = historico_ferias
        self.matricula = matricula

class Animal:
    def __init__(self, nome: str, idade: int, especie: str, raca: str, porte: str, vacinas: list, historico: list, dono: str, matricula: int):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.raca = raca
        self.porte = porte
        self.dono = dono
        self.vacinas = vacinas  # list<vacina>
        self.historico = historico  # list<atendimento>
        self.matricula = matricula

class Pagamento:
    def _init_(self, forma: str, parcelamento: int, valor: float, situacao: bool):
        self.forma = forma
        self.parcelamento = parcelamento
        self.valor = valor
        self.situacao = situacao

class Atendimento:
    def __init__(self, data: str, hora: str, animal: Animal, tutor: Cliente, sintoma: str, tipo: str, pagamento: Pagamento, situacao: bool):
        self.data = data
        self.hora = hora
        self.animal = animal
        self.tutor = tutor
        self.sintoma = sintoma
        self.tipo = tipo
        self.pagamento = pagamento  # classe pagamento
        self.situacao = situacao

class Medicamento:
    def __init__(self, nome: str, fabricante: str, quantidade: int, validade: str, valor: float):
        self.nome = nome
        self.fabricante = fabricante
        self.quantidade = quantidade
        self.validade = validade
        self.valor = valor

class Vacina(Medicamento):
    def __init__(self, situacao: bool):
        super().__init__(nome="", fabricante="", validade="", valor="")
        self.situacao = situacao

class Exame:
    def __init__(self, paciente: Animal(), responsavel: Cliente(), profissional: Funcionario(), sintoma: str, dataExame: str, diagnostico: str, dataDiagnostico: str, medicacao: Medicamento(), situacao: bool):
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
        self.animais = []
        self.funcionarios = []
        self.consultas = []
        self.exames_realizados = []

    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def cadastrar_animal(self, animal):
        self.animais.append(animal)

    def agendar_consulta(self, consulta):
        self.consultas.append(consulta)

    def cancelar_consulta(self, consulta):
        self.consultas.remove(consulta)

    def realizar_exame(self, exame):
        self.exames_realizados.append(exame)

    def resultados_exames(self):
        self.exames_realizados()

clinica = Clinica()

def cadastrar_cliente(clinica):
    nome = input("\nInforme o nome do cliente: ")
    cpf = input("Informe o CPF do cliente: ")
    telefone = input("Informe o telefone do cliente: ")
    email = input("Informe o e-mail do cliente: ")
    endereco = input("Informe o endereco do cliente: ")
    data_cadastro = dt.Today()

    if cpf in clinica.clientes:
        print(f"\nCliente já cadastrado.")
        return

    cliente = Cliente(nome, cpf, telefone, email, endereco, data_cadastro)
    clinica.cadastrar_cliente(cliente)
    print(f"\nCliente {cliente.nome} com CPF {cliente.cpf}, cadastro realizado com sucesso!")

def listar_clientes(clinica):
    if len(clinica.clientes) == 0:
        print("\nNenhum cliente cadastrado até o momento.")
    else:
        print('\n{:=^110}'.format(' CLIENTES CADASTRADOS '))
        for cliente in clinica.clientes:
            print(f"Nome: {cliente.nome} | Telefone: {cliente.telefone} | Pets: {clinica.animais.nome} - Vacinação: {clinica.animais.vacinas.situacao}")
        print('{:=^110}'.format(''))

def cadastrar_animal(clinica):
    nome = input("\nInforme o nome do animal: ")
    idade = input("Informe a idade do animal em meses: ")    
    especie = input("Informe a espécie do animal: ")
    raca = input("Informe a raça do animal: ")
    porte = input("Informe o porte do animal: ")
    dono = input("Informe o nome do dono do animal: ")

    cliente = None
    for c in clinica.clientes:
        if c.nome == dono:
            cliente = c
            break

    if cliente is None:
        print(f"\nCliente {dono} não encontrado. Por favor, cadastre o cliente antes de associar o animal.")
        return

    animal = Animal(nome, idade, especie, raca, porte, dono, matricula=len(clinica.animais) + 1)
    clinica.cadastrar_animal(animal)
    cliente.pets.append(animal)
    print(f"\nAnimal {animal.nome} cadastrado com sucesso.")

def listar_animais(self):
    if len(self.animais) == 0:
        print("\nNenhum animal cadastrado até o momento.")
    else:
        print('\n{:=^110}'.format(' ANIMAIS CADASTRADOS '))
        for animal in self.animais:
            print(f"Matrícula: {animal.matricula} | Nome: {animal.nome} | Espécie: {animal.especie} | Raça: {animal.raca} | Idade: {animal.idade} meses | Porte: {animal.porte} | Dono: {animal.dono} \nVacinas: {animal.vacinas}\n")
        print('{:=^110}'.format(''))

def cadastrar_funcionario(clinica):
    nome = input("\nInforme o nome: ")
    cpf = input("Informe o CPF: ")
    telefone = input("Informe o telefone: ")
    email = input("Informe o e-mail: ")
    endereco = input("Informe o endereço: ")
    salario = input("Informe o salário: ")
    funcao = input("Informe o funcao: ")
    horario = input("Informe o horario: ")
    escala = input("Informe a escala: ")
    login = input("Informe o login: ")
    senha = input("Informe a senha: ")

    funcionario = None
    for f in clinica.funcionarios:
        if f.cpf == cpf:
            print(f"\nO CPF {clinica.funcionarios.cpf}, pertencente ao funcionário {clinica.funcionarios.nome}, já cadastrado no sistema. Por favor, insira um CPF válido.")
            return

    funcionario = Funcionario(nome, cpf, telefone, email, endereco, salario, funcao, horario, escala, login, senha, data_cadastro = dt.Today(), matricula=len(clinica.funcionarios) + 1)
    clinica.cadastrar_funcionario(funcionario)
    clinica.fucionarios.append(funcionario)
    print(f"\nFuncionário {funcionario.nome} cadastrado com sucesso! Seja bem-vindo à nossa Empresa!")

def buscar_animal_por_nome_cpf(clinica):
    cpf = input("Informe o CPF do dono do animal: ")
    nome = input("Informe o nome do animal: ")

    for cliente in clinica.clientes:
        if cliente.cpf == cpf:
            for animal in cliente.animais:
                if animal.nome == nome:
                    print('\n{:=^110}'.format(' DADOS DO ANIMAL '))
                    print(f'Nome: {animal.nome}')
                    print(f'Idade: {animal.idade}')
                    print(f'Espécie: {animal.especie}')
                    print(f'Raça: {animal.raca}')
                    print(f'Porte: {animal.porte}')
                    print('{:=^110}'.format(' DADOS DO DONO '))
                    print(f'Nome: {cliente.nome}')
                    print(f'CPF: {cliente.cpf}')
                    print('{:=^110}'.format(''))
                    return
            print(
                f'Não foi encontrado animal com o nome {nome}, vinculado ao cliente de {cpf}.')
            return
    print(f'Não foi encontrado nenhum cliente com CPF: {cpf}.')

def agendar_consulta(clinica):
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
    horario = str(input("Digite a hora da consulta (HH:MM): "))
    sintoma = str(input("Digite quaisquer sintomas: "))

    agendamento = Agendamento(data, horario, animal, sintoma)
    clinica.agendar_consulta(agendamento)
    print(
        f"\nAgendamento para o animal {animal.nome} marcado para o dia {data} às {horario}.")


def cancelar_consulta(clinica):
    cancela_matricula = int(input("\nInforme a matrícula do animal: "))
    cancela_data = str(input("Digite a data da consulta (DD/MM/YYYY): "))
    cancela_horario = str(input("Digite a hora da consulta (HH:MM): "))

    consulta = None
    for c in clinica.consultas:
        if c.animal.matricula == cancela_matricula and c.hora == cancela_horario and c.data == cancela_data:
            consulta = c
            break

    if consulta is None:
        print(
            f"\nNão há agendamento previsto de um animal com a matrícula {cancela_matricula}.")
        return

    clinica.cancelar_consulta(consulta)
    print(
        f"\nAgendamento para {consulta.animal.nome} no dia {consulta.data} às {consulta.hora} cancelado.")


def realizar_exame(clinica):
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
    print("4 - Listar clientes") #nome, telefone, animais que possui, status de vacinação. (Atualizadas! ou citar as que estão em atraso)
    print("5 - Listar animais")
    print("6 - Listar funcionários")
    print("7 - Busca alternativa (passando o nome do animal e cpf do dono)")
    print("8 - Realizar agendamento") #Colocar uma ordem de controle de agendamento
    print("9 - Cancelar agendamento")
    print("10 - Realizar exame") #Cadastrar prescrições
    print("11 - Ver resultados dos exames") #Listar prescrições
    print("12 - Consultar pagamento") #Visualisa histórico e se houver algum pendente Realizar pagamento de atendimento
    print("0 - Sair")
    print('{:=^110}'.format(''))
    opcao = int(input("Opção escolhida: "))
    print('{:=^110}'.format(''))

    if opcao == 0:
        print("\nEncerrando o programa...\n")
        break

    elif opcao == 1:
        cadastrar_cliente(clinica)
    elif opcao == 2:
        cadastrar_animal(clinica)
    elif opcao == 3:
        cadastrar_funcionario(clinica)
    elif opcao == 4:
        listar_clientes(clinica)
    elif opcao == 5:
        listar_animais(clinica)
    # elif opcao == 6:
        # listar_funcionarios(clinica)
    elif opcao == 7:
        buscar_animal_por_nome_cpf(clinica)
    # elif opcao == 8:
        # realizar_agendamento(clinica)
    # elif opcao == 9:
        # cancelar_agendamento(clinica)
    elif opcao == 10:
        realizar_exame(clinica)
    elif opcao == 11:
        resultados_exames(clinica)
    # elif opcao == 12:
        # consultar_pagamento(clinica)

    else:
        print("Opção inválida. Tente novamente.")
