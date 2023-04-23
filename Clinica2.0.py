class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.animais = []

class Animal:
    def __init__(self, nome, especie, raca, idade, dono, matricula):
        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.idade = idade
        self.dono = dono
        self.matricula = matricula        

class Agendamento:
    def __init__(self, data, hora, animal, sintoma):
        self.data = data
        self.hora = hora
        self.animal = animal
        self.sintoma = sintoma

class Exame:
    def __init__(self, animal, diagnostico):
        self.animal = animal
        self.diagnostico = diagnostico
    
class Clinica:
    def __init__(self):
        self.clientes = []
        self.animais = []
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

    if cpf in clinica.clientes:        
        print(f"\nCliente já cadastrado.")
        return    

    cliente = Cliente(nome, cpf)
    clinica.cadastrar_cliente(cliente)    
    print(f"\nCliente {cliente.nome} com CPF {cliente.cpf}, cadastro realizado com sucesso.")

def listar_clientes(clinica):    
    if len(clinica.clientes) == 0:
        print("\nNenhum cliente cadastrado até o momento.")
    else:
        print('\n{:=^110}'.format(' CLIENTES CADASTRADOS '))        
        for cliente in clinica.clientes:
            print(f"Nome: {cliente.nome} | CPF: {cliente.cpf}")
        print('{:=^110}'.format(''))

def cadastrar_animal(clinica):
    nome = str(input("\nInforme o nome do animal: "))
    especie = str(input("Informe a espécie do animal: "))
    raca = str(input("Informe a raça do animal: "))
    idade = int(input("Informe a idade do animal em meses: "))
    dono = str(input("Informe o nome do dono do animal: "))

    cliente = None
    for c in clinica.clientes:
        if c.nome == dono:
            cliente = c
            break
    
    if cliente is None:
        print(f"\nCliente {dono} não encontrado. Por favor, cadastre o cliente antes de associar o animal.")
        return
    
    animal = Animal(nome, especie, raca, idade, dono, matricula = len(clinica.animais) + 1)
    clinica.cadastrar_animal(animal)
    cliente.animais.append(animal)
    print(f"\nAnimal {animal.nome} cadastrado com sucesso.")

def listar_animais(self):
        if len(self.animais) == 0:
            print("\nNenhum animal cadastrado até o momento.")
        else:
            print('\n{:=^110}'.format(' ANIMAIS CADASTRADOS '))
            for animal in self.animais:
                print(f"Matrícula: {animal.matricula} | Nome: {animal.nome} | Espécie: {animal.especie} | Raça: {animal.raca} | Idade: {animal.idade} meses | Dono: {animal.dono}")
            print('{:=^110}'.format(''))

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
                    print('{:=^110}'.format(' DADOS DO DONO '))                    
                    print(f'Nome: {cliente.nome}')
                    print(f'CPF: {cliente.cpf}')
                    print('{:=^110}'.format(''))
                    return
            print(f'Não foi encontrado animal com o nome {nome}, vinculado ao cliente de {cpf}.')
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
        print(f"\nAnimal com matrícula {matricula_animal} não encontrado. Por favor, cadastre o animal antes de agendar uma consulta.")
        return
    
    data = str(input("Digite a data da consulta (DD/MM/YYYY): "))
    horario = str(input("Digite a hora da consulta (HH:MM): "))
    sintoma = str(input("Digite quaisquer sintomas: "))

    agendamento = Agendamento(data, horario, animal, sintoma)
    clinica.agendar_consulta(agendamento)
    print(f"\nAgendamento para o animal {animal.nome} marcado para o dia {data} às {horario}.")

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
        print(f"\nNão há agendamento previsto de um animal com a matrícula {cancela_matricula}.")
        return

    clinica.cancelar_consulta(consulta)
    print(f"\nAgendamento para {consulta.animal.nome} no dia {consulta.data} às {consulta.hora} cancelado.")            

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
            print(f"Animal: {exame.animal.nome} | Diagnóstico: {exame.diagnostico}")
        print('{:=^110}'.format(''))

while True:
    print('\n{:=^110}'.format(' ESCOLHA UMA OPÇÃO '))
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Cadastrar animal")
    print("4 - Listar animais")
    print("5 - Busca passando o nome do animal e cpf do dono")
    print("6 - Agendar consulta")
    print("7 - Cancelar consulta")
    print("8 - Realizar exame")
    print("9 - Ver resultados dos exames")
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
        listar_clientes(clinica)

    elif opcao == 3:
        cadastrar_animal(clinica)

    elif opcao == 4:
        listar_animais(clinica)

    elif opcao == 5:
        buscar_animal_por_nome_cpf(clinica)

    elif opcao == 6:
        agendar_consulta(clinica)

    elif opcao == 7:
        cancelar_consulta(clinica)

    elif opcao == 8:
        realizar_exame(clinica)

    elif opcao == 9:
        resultados_exames(clinica)    

    else:
        print("Opção inválida. Tente novamente.")
