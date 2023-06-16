import random

def numero_de_lixeiras_invalido(linhas, colunas):
    return linhas < 3 or linhas > 6 or colunas < 3 or colunas > 6

def renderizaLixeiras(linhas, colunas, palpitesFalhos):
    lixeiras = ""

    for i in range(1, linhas * colunas + 1):
        if i in palpitesFalhos:
            lixeiras += "❌ "
        else:
            lixeiras += "🗑️ "

        if i % colunas == 0:
            lixeiras += "\n"

    return lixeiras

def renderizaLixeirasNoAcerto(linhas, colunas, segundaLixeira, palpitesFalhos):
    lixeiras = ""

    for i in range(1, linhas * colunas + 1):
        if i == segundaLixeira:
            lixeiras += "-> 🗑️ <- "
        elif i in palpitesFalhos:
            lixeiras += "❌ "
        else:
            lixeiras += "🗑️ "

        if i % colunas == 0:
            lixeiras += "\n"

    return lixeiras

jogando = True

while jogando:
    print("\n------------------------------------------------------------")
    print("Bem-vindo ao ginásio da cidade de Vermilion, dos pokémon do tipo elétrico, jovem aventureiro!\n")
    print("Antes de enfrentar o líder, Tenente Surge, e seu temível Raichu, você precisará solucionar este enigma.")
    print("Encontre as duas lixeiras que possuem os botões para desligar a barreira elétrica no meio do ginásio.")
    print("O primeiro botão estará em qualquer lugar. O segundo estará ou na lixeira imediatamente acima, ou na abaixo, ou na da esquerda ou na da direita do primeiro. Boa sorte.")
    print("\n------------------------------------------------------------")
    decifrarOuDesistir = int(input("Escolha uma opção:\n1: Decifrar o enigma\n2: Desistir\n"))

    if decifrarOuDesistir == 1:
        linhas = int(input("Quantas linhas de lixeiras há? (Número de 3 a 6.)\n"))
        colunas = int(input("Quantas colunas de lixeiras há? (Número de 3 a 6.)\n"))

        if numero_de_lixeiras_invalido(linhas, colunas):
            print("Número de lixeiras inválido. Tente novamente.")
            continue

        primeiraLixeira = random.randint(1, linhas * colunas)
        palpitesFalhos = []

        while True:
            print("\nPrimeira lixeira:")
            print(renderizaLixeiras(linhas, colunas, palpitesFalhos))
            palpite = int(input("Qual das lixeiras você acha que possui o primeiro botão?\n"))

            if palpite == primeiraLixeira:
                print("ACERTOU A PRIMEIRA!")
                break
            elif palpite in palpitesFalhos:
                print("Você chutou uma lixeira que já foi verificada. Tente novamente.")
            elif palpite < 1 or palpite > linhas * colunas:
                print("Você chutou uma lixeira fora dos limites. Tente novamente.")
            else:
                palpitesFalhos.append(palpite)
                print("Palpite incorreto. Tente novamente.")

        if primeiraLixeira in palpitesFalhos:
            palpitesFalhos.remove(primeiraLixeira)

        segundaLixeira = 0
        segundaLixeiraPossiveis = []

        if primeiraLixeira % colunas != 1 and (primeiraLixeira - 1) not in palpitesFalhos:
            segundaLixeiraPossiveis.append(primeiraLixeira - 1)
        if primeiraLixeira % colunas != 0 and (primeiraLixeira + 1) not in palpitesFalhos:
            segundaLixeiraPossiveis.append(primeiraLixeira + 1)
        if primeiraLixeira > colunas and (primeiraLixeira - colunas) not in palpitesFalhos:
            segundaLixeiraPossiveis.append(primeiraLixeira - colunas)
        if primeiraLixeira <= (linhas - 1) * colunas and (primeiraLixeira + colunas) not in palpitesFalhos:
            segundaLixeiraPossiveis.append(primeiraLixeira + colunas)

        while True:
            print("\nSegunda lixeira:")
            print(renderizaLixeirasNoAcerto(linhas, colunas, segundaLixeira, palpitesFalhos))
            palpite = int(input("Qual das lixeiras adjacentes você acha que possui o segundo botão?\nEscolha um número correspondente à posição:\n1: Cima, 2: Baixo, 3: Esquerda, 4: Direita\n"))

            if palpite == 1 and primeiraLixeira > colunas and (primeiraLixeira - colunas) in segundaLixeiraPossiveis:
                segundaLixeira = primeiraLixeira - colunas
                print("ACERTOU A SEGUNDA!")
                break
            elif palpite == 2 and primeiraLixeira <= (linhas - 1) * colunas and (primeiraLixeira + colunas) in segundaLixeiraPossiveis:
                segundaLixeira = primeiraLixeira + colunas
                print("ACERTOU A SEGUNDA!")
                break
            elif palpite == 3 and primeiraLixeira % colunas != 1 and (primeiraLixeira - 1) in segundaLixeiraPossiveis:
                segundaLixeira = primeiraLixeira - 1
                print("ACERTOU A SEGUNDA!")
                break
            elif palpite == 4 and primeiraLixeira % colunas != 0 and (primeiraLixeira + 1) in segundaLixeiraPossiveis:
                segundaLixeira = primeiraLixeira + 1
                print("ACERTOU A SEGUNDA!")
                break
            else:
                print("Palpite incorreto. Tente novamente.")

        print(renderizaLixeirasNoAcerto(linhas, colunas, segundaLixeira, palpitesFalhos))
        print("\nVocê desativou a barreira elétrica e está pronto para enfrentar o Tenente Surge.")

        jogarNovamente = int(input("Deseja jogar novamente?\n1: Sim, 2: Não\n"))
        if jogarNovamente != 1:
            print("Obrigado por jogar!")
            jogando = False
    else:
        print("Obrigado por jogar!")
        jogando = False