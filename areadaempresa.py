# =====================================================
# SISTEMA DE MATCH DE EMPREGOS
# Aplicativo de conexão entre empresas e candidatos
# =====================================================

# DICIONÁRIOS E CONJUNTOS PARA ARMAZENAR OS DADOS

# Armazena os candidatos cadastrados e suas informações.
candidatos = {}

# Armazena as empresas cadastradas e suas respectivas vagas.
empresas = {}

# Registra os interesses demonstrados pelos candidatos.
# Cada registro contém: candidato, empresa e vaga.
interesses_candidatos = set()

# Registra os interesses demonstrados pelas empresas.
# Cada registro contém: empresa, candidato e vaga.
interesses_empresas = set()

# Armazena os matches confirmados entre candidatos e empresas.
matches = set()

# =====================================================
# 1. CADASTRO DE CANDIDATOS
# =====================================================

def cadastrar_candidato():

    print("\n--- CADASTRO DE CANDIDATO ---")

    # Solicita as informações pessoais e profissionais.
    nome = input("Nome: ")
    profissao = input("Profissão: ")
    habilidades = input("Habilidades: ")

    # Salva as informações no dicionário de candidatos.
    # O nome será utilizado como identificador do candidato.
    candidatos[nome] = {
        "profissao": profissao,
        "habilidades": habilidades
    }

    print("\nCandidato cadastrado com sucesso!")

# =====================================================
# 2. CADASTRO DE EMPRESAS
# =====================================================

def cadastrar_empresa():

    print("\n--- CADASTRO DE EMPRESA ---")

    # Solicita o nome da empresa.
    nome = input("Nome da empresa: ")

    # Verifica se a empresa já existe no sistema.
    if nome in empresas:
        print("Empresa já cadastrada!")
        return

    # Cria o perfil da empresa.
    # O campo "vagas" armazenará todas as suas oportunidades.
    empresas[nome] = {
        "vagas": {}
    }

    print("Empresa cadastrada com sucesso!")

# =====================================================
# 3. CADASTRO DE VAGAS
# =====================================================

def cadastrar_vaga():

    # Solicita o nome da empresa responsável pela vaga.
    nome_empresa = input("Nome da empresa: ")

    # Verifica se a empresa está cadastrada.
    if nome_empresa not in empresas:
        print("Empresa não encontrada!")
        return

    # Solicita as informações da oportunidade.
    vaga = input("Nome da vaga: ")
    requisitos = input("Requisitos da vaga: ")

    # Verifica se a empresa já cadastrou uma vaga com esse nome.
    if vaga in empresas[nome_empresa]["vagas"]:
        print("Essa vaga já está cadastrada!")
        return

    # Armazena a vaga dentro do cadastro da empresa.
    empresas[nome_empresa]["vagas"][vaga] = {
        "requisitos": requisitos
    }

    print("Vaga cadastrada com sucesso!")

# =====================================================
# 4. CANDIDATO DEMONSTRA INTERESSE EM UMA VAGA
# =====================================================

def candidato_interesse():

    # Verifica se existem candidatos e empresas cadastrados.
    if not candidatos or not empresas:
        print("Cadastre candidatos e empresas primeiro!")
        return

    print("\n--- VAGAS DISPONÍVEIS ---")

    # Cria uma lista para reunir todas as vagas disponíveis.
    vagas = []

    # Percorre todas as empresas cadastradas.
    for empresa, dados in empresas.items():

        # Percorre todas as vagas de cada empresa.
        for vaga in dados["vagas"]:

            # Adiciona o nome da empresa e da vaga à lista.
            vagas.append((empresa, vaga))

    # Verifica se existe alguma vaga cadastrada.
    if not vagas:
        print("Nenhuma vaga disponível!")
        return

    # Apresenta todas as vagas disponíveis.
    for i, (empresa, vaga) in enumerate(vagas):
        print(f"\n{i + 1} - {empresa}")
        print(f"Vaga: {vaga}")

    try:

        # Solicita que o candidato escolha uma vaga.
        escolha = int(input("\nEscolha uma vaga: ")) - 1

        # Verifica se a opção escolhida é válida.
        if escolha < 0 or escolha >= len(vagas):
            print("Opção inválida!")
            return

        # Solicita o nome do candidato.
        nome_candidato = input("Nome do candidato: ")

        # Verifica se o candidato está cadastrado.
        if nome_candidato not in candidatos:
            print("Candidato não encontrado!")
            return

        # Recupera a empresa e a vaga escolhidas.
        empresa, vaga = vagas[escolha]

        # Cria um registro do interesse do candidato.
        interesse = (nome_candidato, empresa, vaga)

        # Impede que o mesmo candidato curta a mesma vaga
        # mais de uma vez.
        if interesse in interesses_candidatos:
            print("Interesse já registrado!")
            return

        # Salva o interesse no conjunto de candidatos.
        interesses_candidatos.add(interesse)

        print("\nInteresse registrado com sucesso!")

        # Após registrar o interesse, verifica se já existe MATCH.
        verificar_match(nome_candidato, empresa, vaga)

    except ValueError:

        # Impede que o programa seja interrompido
        # caso o usuário digite algo diferente de um número.
        print("Digite um número válido!")

# =====================================================
# 5. EMPRESA VISUALIZA OS CANDIDATOS INTERESSADOS
# =====================================================

def visualizar_interessados():

    # Solicita o nome da empresa que deseja consultar os interessados.
    nome_empresa = input("\nNome da empresa: ")

    # Verifica se a empresa está cadastrada.
    if nome_empresa not in empresas:
        print("Empresa não encontrada!")
        return

    print("\n--- VAGAS DA EMPRESA ---")

    # Recupera todas as vagas cadastradas pela empresa.
    lista_vagas = list(empresas[nome_empresa]["vagas"].keys())

    # Verifica se a empresa possui vagas.
    if not lista_vagas:
        print("Essa empresa não possui vagas cadastradas!")
        return

    # Apresenta as vagas para a empresa escolher.
    for i, vaga in enumerate(lista_vagas):
        print(f"{i + 1} - {vaga}")

    try:

        # Solicita a escolha da vaga.
        escolha = int(input("\nEscolha uma vaga: ")) - 1

        # Verifica se a escolha é válida.
        if escolha < 0 or escolha >= len(lista_vagas):
            print("Opção inválida!")
            return

        # Recupera o nome da vaga selecionada.
        vaga_escolhida = lista_vagas[escolha]

        print("\n================================")
        print("      CANDIDATOS INTERESSADOS")
        print("================================")

        # Contador para registrar quantos candidatos
        # demonstraram interesse na vaga.
        encontrados = 0

        # Percorre todos os interesses registrados.
        for candidato, empresa, vaga in interesses_candidatos:

            # Verifica se o interesse pertence à empresa
            # e à vaga selecionadas.
            if empresa == nome_empresa and vaga == vaga_escolhida:

                # Exibe as informações do candidato interessado.
                print(f"\nNome: {candidato}")

                print(
                    "Profissão:",
                    candidatos[candidato]["profissao"]
                )

                print(
                    "Habilidades:",
                    candidatos[candidato]["habilidades"]
                )

                # Aumenta o contador de interessados.
                encontrados += 1

        # Caso ninguém tenha demonstrado interesse,
        # apresenta uma mensagem informativa.
        if encontrados == 0:
            print("Nenhum candidato demonstrou interesse ainda!")

        # Exibe a quantidade total de interessados.
        print("\nTotal de interessados:", encontrados)

    except ValueError:

        # Trata erros caso o usuário não digite um número.
        print("Digite um número válido!")

# =====================================================
# 6. EMPRESA DEMONSTRA INTERESSE EM UM CANDIDATO
# =====================================================

def empresa_interesse():

    # Solicita o nome da empresa.
    nome_empresa = input("\nNome da empresa: ")

    # Verifica se a empresa existe.
    if nome_empresa not in empresas:
        print("Empresa não encontrada!")
        return

    print("\n--- ESCOLHA UMA VAGA ---")

    # Recupera as vagas cadastradas pela empresa.
    lista_vagas = list(empresas[nome_empresa]["vagas"].keys())

    if not lista_vagas:
        print("Nenhuma vaga cadastrada!")
        return

    # Apresenta as vagas disponíveis.
    for i, vaga in enumerate(lista_vagas):
        print(f"{i + 1} - {vaga}")

    try:

        # A empresa seleciona a vaga.
        escolha = int(input("Escolha a vaga: ")) - 1

        if escolha < 0 or escolha >= len(lista_vagas):
            print("Opção inválida!")
            return

        vaga_escolhida = lista_vagas[escolha]

        print("\n--- CANDIDATOS INTERESSADOS ---")

        # Cria uma lista para armazenar os candidatos
        # que demonstraram interesse nessa vaga.
        interessados = []

        # Percorre os interesses dos candidatos.
        for candidato, empresa, vaga in interesses_candidatos:

            # Seleciona somente candidatos interessados
            # na vaga escolhida e pertencente à empresa.
            if empresa == nome_empresa and vaga == vaga_escolhida:
                interessados.append(candidato)

        # Verifica se existem candidatos interessados.
        if not interessados:
            print("Nenhum candidato interessado nessa vaga!")
            return

        # Apresenta os candidatos para a empresa.
        for i, candidato in enumerate(interessados):
            print(f"\n{i + 1} - {candidato}")
            print("Profissão:", candidatos[candidato]["profissao"])

        # A empresa escolhe um candidato.
        escolha_candidato = int(
            input("\nEscolha um candidato: ")
        ) - 1

        # Verifica se a escolha é válida.
        if escolha_candidato < 0 or escolha_candidato >= len(interessados):
            print("Opção inválida!")
            return

        candidato_escolhido = interessados[escolha_candidato]

        # Registra o interesse da empresa.
        interesse = (
            nome_empresa,
            candidato_escolhido,
            vaga_escolhida
        )

        # Evita registrar o mesmo interesse duas vezes.
        if interesse in interesses_empresas:
            print("A empresa já demonstrou interesse!")
            return

        # Armazena o interesse no conjunto de empresas.
        interesses_empresas.add(interesse)

        print("\nInteresse da empresa registrado!")

        # Verifica se o candidato também demonstrou interesse.
        verificar_match(
            candidato_escolhido,
            nome_empresa,
            vaga_escolhida
        )

    except ValueError:

        print("Digite um número válido!")

# =====================================================
# 7. VERIFICAÇÃO DE MATCH
# =====================================================

def verificar_match(candidato, empresa, vaga):

    # Cria o registro do interesse do candidato.
    interesse_candidato = (candidato, empresa, vaga)

    # Cria o registro do interesse da empresa.
    interesse_empresa = (empresa, candidato, vaga)

    # Verifica se os dois lados demonstraram interesse.
    # O operador AND exige que ambas as condições sejam verdadeiras.
    if (
        interesse_candidato in interesses_candidatos
        and interesse_empresa in interesses_empresas
    ):

        # Cria o registro do MATCH.
        match = (candidato, empresa, vaga)

        # Verifica se esse MATCH ainda não foi registrado.
        if match not in matches:

            # Salva o MATCH confirmado.
            matches.add(match)

            # Apresenta a confirmação na tela.
            print("\n==============================")
            print("          NOVO MATCH!")
            print("==============================")
            print("Candidato:", candidato)
            print("Empresa:", empresa)
            print("Vaga:", vaga)
            print("Interesse mútuo confirmado!")
            print("==============================")

# =====================================================
# 8. CONSULTA DE MATCHES
# =====================================================

def consultar_matches():

    print("\n--- MATCHES REALIZADOS ---")

    # Verifica se existe algum MATCH registrado.
    if not matches:
        print("Nenhum match encontrado!")
        return

    # Percorre todos os matches armazenados.
    for candidato, empresa, vaga in sorted(matches):

        # Apresenta os dados de cada conexão confirmada.
        print("\n------------------------------")
        print("Candidato:", candidato)
        print("Empresa:", empresa)
        print("Vaga:", vaga)
        print("Status: MATCH CONFIRMADO")

# =====================================================
# 9. MENU PRINCIPAL
# =====================================================

def menu():

    # Mantém o menu funcionando até o usuário decidir sair.
    while True:

        print("\n================================")
        print("       MATCH DE EMPREGOS")
        print("================================")
        print("1 - Cadastrar candidato")
        print("2 - Cadastrar empresa")
        print("3 - Cadastrar vaga")
        print("4 - Candidato demonstrar interesse")
        print("5 - Empresa visualizar interessados")
        print("6 - Empresa demonstrar interesse")
        print("7 - Consultar matches")
        print("0 - Sair")
        print("================================")

        # Recebe a opção escolhida pelo usuário.
        opcao = input("Escolha uma opção: ")

        # Direciona o usuário para a funcionalidade escolhida.
        if opcao == "1":
            cadastrar_candidato()

        elif opcao == "2":
            cadastrar_empresa()

        elif opcao == "3":
            cadastrar_vaga()

        elif opcao == "4":
            candidato_interesse()

        elif opcao == "5":
            visualizar_interessados()

        elif opcao == "6":
            empresa_interesse()

        elif opcao == "7":
            consultar_matches()

        # Encerra o programa.
        elif opcao == "0":
            print("Encerrando aplicativo...")
            break

        # Informa quando o usuário escolhe uma opção inexistente.
        else:
            print("Opção inválida!")

# =====================================================
# 10. INICIALIZAÇÃO DO PROGRAMA
# =====================================================

# Chama a função menu para iniciar o aplicativo.
menu()
