# ==========================================
# SISTEMA DE MATCH DE EMPREGOS
# Inspirado no funcionamento do Tinder
# ==========================================

# ARMAZENAMENTO DOS DADOS

# Lista que armazena todos os candidatos cadastrados.
candidatos = []

# Lista que armazena todas as empresas cadastradas.
empresas = []

# Registra os interesses demonstrados pelos candidatos.
interesses_candidatos = []

# Registra os interesses demonstrados pelas empresas.
interesses_empresas = []

# Armazena os matches confirmados entre empresas e candidatos.
matches = []

# ==========================================
# 1. CADASTRO DE CANDIDATOS
# ==========================================

def cadastrar_candidato():

    print("\n--- CADASTRO DE CANDIDATO ---")

    # Solicita as informações do candidato.
    nome = input("Nome do candidato: ")
    profissao = input("Profissão: ")
    habilidades = input("Habilidades (separadas por vírgula): ")

    # Cria um dicionário com os dados informados.
    candidato = {
        "nome": nome,
        "profissao": profissao,
        "habilidades": habilidades
    }

    # Adiciona o candidato à lista de cadastrados.
    candidatos.append(candidato)

    print("Candidato cadastrado com sucesso!")

# ==========================================
# 2. CADASTRO DE EMPRESAS E VAGAS
# ==========================================

def cadastrar_empresa():

    print("\n--- CADASTRO DE EMPRESA ---")

    # Solicita os dados da empresa e da oportunidade.
    nome = input("Nome da empresa: ")
    vaga = input("Nome da vaga: ")
    habilidades = input("Habilidades desejadas: ")

    # Cria um dicionário com as informações da empresa.
    empresa = {
        "nome": nome,
        "vaga": vaga,
        "habilidades": habilidades
    }

    # Adiciona a empresa à lista de empresas cadastradas.
    empresas.append(empresa)

    print("Empresa cadastrada com sucesso!")

# ==========================================
# 3. CANDIDATO DEMONSTRA INTERESSE NA VAGA
# ==========================================

def interesse_candidato():

    print("\n--- VAGAS DISPONÍVEIS ---")

    # Verifica se existem vagas cadastradas.
    if not empresas:
        print("Nenhuma vaga cadastrada.")
        return

    # Apresenta todas as empresas e suas vagas.
    for i, empresa in enumerate(empresas):

        print(f"\n{i + 1} - {empresa['nome']}")
        print(f"Vaga: {empresa['vaga']}")
        print(f"Habilidades: {empresa['habilidades']}")

    # Solicita que o candidato escolha uma vaga.
    try:
        escolha = int(input("\nEscolha uma vaga: ")) - 1

        # Verifica se a opção escolhida existe.
        if escolha < 0 or escolha >= len(empresas):
            print("Opção inválida!")
            return

        # Solicita o nome do candidato.
        nome_candidato = input("Digite seu nome: ")

        # Verifica se o candidato está cadastrado.
        if not any(c["nome"] == nome_candidato for c in candidatos):
            print("Candidato não encontrado!")
            return

        # Recupera o nome da empresa escolhida.
        nome_empresa = empresas[escolha]["nome"]

        # Cria um registro do interesse.
        interesse = (nome_candidato, nome_empresa)

        # Verifica se o candidato já demonstrou interesse.
        if interesse in interesses_candidatos:
            print("Você já demonstrou interesse nesta vaga!")
            return

        # Registra o interesse do candidato.
        interesses_candidatos.append(interesse)

        print("Interesse enviado com sucesso!")

        # Verifica se a empresa também demonstrou interesse.
        verificar_match(nome_candidato, nome_empresa)

    except ValueError:
        # Trata erros caso o usuário não digite um número.
        print("Digite um número válido!")

# ==========================================
# 4. EMPRESA DEMONSTRA INTERESSE NO CANDIDATO
# ==========================================

def interesse_empresa():

    print("\n--- CANDIDATOS DISPONÍVEIS ---")

    # Verifica se existem candidatos cadastrados.
    if not candidatos:
        print("Nenhum candidato cadastrado.")
        return

    # Apresenta todos os candidatos disponíveis.
    for i, candidato in enumerate(candidatos):

        print(f"\n{i + 1} - {candidato['nome']}")
        print(f"Profissão: {candidato['profissao']}")
        print(f"Habilidades: {candidato['habilidades']}")

    try:
        # Solicita a escolha de um candidato.
        escolha = int(input("\nEscolha um candidato: ")) - 1

        # Verifica se a escolha é válida.
        if escolha < 0 or escolha >= len(candidatos):
            print("Opção inválida!")
            return

        # Solicita o nome da empresa.
        nome_empresa = input("Digite o nome da empresa: ")

        # Verifica se a empresa está cadastrada.
        if not any(e["nome"] == nome_empresa for e in empresas):
            print("Empresa não encontrada!")
            return

        # Recupera o nome do candidato escolhido.
        nome_candidato = candidatos[escolha]["nome"]

        # Cria o registro do interesse da empresa.
        interesse = (nome_empresa, nome_candidato)

        # Impede que a empresa registre o mesmo interesse duas vezes.
        if interesse in interesses_empresas:
            print("A empresa já demonstrou interesse neste candidato!")
            return

        # Registra o interesse da empresa.
        interesses_empresas.append(interesse)

        print("Interesse registrado com sucesso!")

        # Verifica se o candidato também demonstrou interesse.
        verificar_match(nome_candidato, nome_empresa)

    except ValueError:
        # Trata erros de digitação na escolha do candidato.
        print("Digite um número válido!")

# ==========================================
# 5. VERIFICAÇÃO DE INTERESSE MÚTUO
# ==========================================

def verificar_match(nome_candidato, nome_empresa):

    # Cria o registro de interesse do candidato.
    interesse_candidato = (
        nome_candidato,
        nome_empresa
    )

    # Cria o registro de interesse da empresa.
    # A ordem dos nomes é invertida para diferenciar os registros.
    interesse_empresa = (
        nome_empresa,
        nome_candidato
    )

    # Verifica se o candidato e a empresa demonstraram interesse.
    # O AND exige que as duas condições sejam verdadeiras.
    if (
        interesse_candidato in interesses_candidatos
        and interesse_empresa in interesses_empresas
    ):

        # Cria o registro do match.
        match = (nome_candidato, nome_empresa)

        # Verifica se o match já foi registrado.
        if match not in matches:

            # Adiciona o novo match à lista.
            matches.append(match)

            # Exibe a confirmação do interesse mútuo.
            print("\n********************************")
            print("          É UM MATCH!")
            print("********************************")
            print(f"Candidato: {nome_candidato}")
            print(f"Empresa: {nome_empresa}")
            print("Agora vocês podem iniciar um contato!")
            print("********************************")

# ==========================================
# 6. VISUALIZAÇÃO DOS MATCHES
# ==========================================

def visualizar_matches():

    print("\n--- MATCHES REALIZADOS ---")

    # Verifica se existe algum match registrado.
    if not matches:
        print("Nenhum match realizado ainda.")
        return

    # Percorre todos os matches armazenados.
    for candidato, empresa in matches:

        # Apresenta as informações de cada conexão.
        print(f"\nCandidato: {candidato}")
        print(f"Empresa: {empresa}")
        print("-------------------------")

# ==========================================
# 7. MENU PRINCIPAL DO SISTEMA
# ==========================================

def menu():

    # Mantém o menu funcionando até o usuário sair.
    while True:

        print("\n================================")
        print("       MATCH DE EMPREGOS")
        print("================================")
        print("1 - Cadastrar candidato")
        print("2 - Cadastrar empresa e vaga")
        print("3 - Candidato curtir uma vaga")
        print("4 - Empresa curtir um candidato")
        print("5 - Visualizar matches")
        print("0 - Sair")

        # Recebe a opção escolhida pelo usuário.
        opcao = input("\nEscolha uma opção: ")

        # Executa a função correspondente à opção escolhida.
        if opcao == "1":
            cadastrar_candidato()

        elif opcao == "2":
            cadastrar_empresa()

        elif opcao == "3":
            interesse_candidato()

        elif opcao == "4":
            interesse_empresa()

        elif opcao == "5":
            visualizar_matches()

        # Encerra o programa quando o usuário escolhe 0.
        elif opcao == "0":
            print("Encerrando o sistema...")
            break

        # Informa quando uma opção inválida é digitada.
        else:
            print("Opção inválida! Tente novamente.")

# ==========================================
# 8. INICIALIZAÇÃO DO PROGRAMA
# ==========================================

# Chama o menu principal e inicia o sistema.
menu()
