"""
Disciplina Raciocinio Computacional
Baseado no jogo de tabuleiro Zombie Dice da empresa Galapagos.
"""

import random    # Função em que escolhe de formas aleatórias
import sys       # Função para não pular linha

# Função para mostrar o título mostra o Título do jogo
def titulo():
    print(
        f'\n{" "*10}{" O":7}{"-" * 15}{"O//":>7}\n{" "*10}{" |= ":6}|{"ZOMBIE DICE":^15}|{"|":>4}\n{" "*10}{"/ / ":6} {"-" * 15} {"/ / ":>6}\n')
    print(f'{" "*10}{"UM JOGO PARA TODA FAMÍLIA":^30}')

# Função para delimitar (Visual)
def separador():
    print(f'\n {"-" * 100} \n')

# função de Validação respostas sim ou não, retornando verdadeiro ou falso
def validacao(a):
    while True:
        if a == "S":
            a = "s"
        elif a == "N":
            a = "n"
        elif a == "R":
            a = "r"
        if a == "s":
            return True
        elif a == "r":
            regras()
            return False
        elif a == "n":
            return True
        else:
            print("Opção Inválida")
            return False


# Função para mostrar as regras
def regras():
    print(f'{"-" * 130}\n|{"*** REGRAS ZOMBIE DICE ***":^128}|\n|{" " * 128}|\n'
          f'|{"  Mínimo de 2 jogadores, o limite é você quem diz, Zombie Dice é um jogo para família toda"}{" " * 38}|\n'
          f'|{"  São 13 dados de 6 faces, sendo eles: "}{" " * 89}|\n'
          f'|{"  6 dados VERDES (fácil) contém 3 cerébros, 2 passos, 1 tiros."}{" " * 66}|\n'
          f'|{"  4 dados AMARELO (intermediário) contém 2 cerébros, 2 passos, 2 tiros."}{" " * 57}|\n'
          f'|{"  3 dados VERMELHO (difícil) contém 1 cerébros, 2 passos, 3 tiros."}{" " * 62}|\n|{" " * 128}|\n'
          f'|{"  O objetivo do jogo é conseguir comer 13 cérebros, em caso de empate teremos morte súbita"}{" " * 38}|\n'
          f'|{"  Em um rodada, cada jogador tem um turno para jogar."}{" " * 75}|\n'
          f'|{"  No turno, o jogador deve pegar 3 dados do tubo aleatoriamente e lançar, sempre os três dados juntos."}{" " * 26}|\n'
          f'|{"  Quando a face do dado cair virada com símbolo para CEREBRO, é porque o jogador comeu um cérebro."}{" " * 30}|\n'
          f'|{"  Caso a face do dado cair virada com o símbolo para PASSOS, a vítima fugiu,"}{" " * 52}|\n'
          f'|{"  se o jogador decidir continuar a lançar os dados em seu turno,"}{" " * 64}|\n'
          f'|{"  os dados que caíram com a face para PASSOS deverão ser lançados novamente,"}{" " * 52}|\n'
          f'|{"  para lançar novamente os três dados o jogador completa a quantidade retirando outros dados do tubo,"}{" " * 27}|\n'
          f'|{"  sempre lançando os três dados. O objetivo é comer 13 cérebros para vencer o jogo,"}{" " * 45}|\n'
          f'|{"  no entanto existem os tiros de espingarda, se por acaso o jogador levar três tiros de espingarda "}{" " * 29}|\n'
          f'|{"  ele perde e sai do jogo. No seu turno após lançar os dados o jogador pode decidir parar ou continuar a jogar."}{" " * 17}|\n'
          f'|{"  Caso decida parar você contabiliza os cérebros para próxima jogada, já os dados de tiro são zerados para próxima rodada."}{" " * 6}|\n{"-" * 130}')
    continuar = input("ENTER para continuar...\n")


# cria uma lista contendo o placar do jogo. o indice é a quantidade de jogadores(quantJog)
def showPlacar(a):
    print(f'\n{"-" * 45}')
    for l in range(a+1):
        sys.stdout.write("|")
        for c in range(4):
            sys.stdout.write(f'{jogadores[l][c]:^10}|')
        print(f'\n{"-" * 45}')
    print("")


"""
Funções que envolvem os jogadores
"""

# Função para verificar o jogador que será inserido e para continuar o jogo, a = jogador, b = jogadores, c = quantJog
def verifica_jogador(a,b,c):
    while True:
        c += 1
        passe = True
        while passe == True:
            for l in range(c):
                if l == c - 1:
                    passe = False
                if a == b[l][0]:
                    print("Jogador existente")
                    a = input("Insira outro nome: ")
                    passe = True
                    continue
        if a == "ok":
             while True:
                if quantJog < 2:  # Verifica se tem menos de 2 jogadores
                    print("Insira no mínimo dois jogadores: ")
                    a = input("Insira " + str(quantJog + 1) + "º Jogador: ")
                    if a != "ok" and quantJog <= 2:
                        c -= 1
                        break
                    elif a != "ok":
                        return a
                else:
                    return a
        elif a == "":
            while True:
                print("Não foi inserido um nome!")
                a = input("Insira " + str(quantJog + 1) + "º Jogador: ")
                if a != "" and (len(b)) == 1:
                    return a
                else:
                    c -= 1
                    break
            else:
                return a
        else:
            return a


# Insere o jogador com seus atributos
def insere_jogadores(a):
    b = []
    if a == "inicio123":
        b.append("NOME")
        b.append("CEREBROS")
        b.append("RODADA")
        b.append("VITÓRIAS")
        return b
    else:
        b.append(a)  # Nome
        b.append(0)  # CEREBROS
        b.append(0)  # RODADA
        b.append(0)  # VITÓRIAS
        return b


# Função para alterar o jogador indice a = gamer/jogador, b = quantidade de jogadores, c = lista de finalistas
def muda_jogador(a,b,c):
    if len(c) == 1:
        a += 1
        if a > b:
            a = 1
            return a
        return a
    elif len(c) >= 2:
        while True:
            a += 1
            if a > b:
                a = 1
            if a in c:
                return a

"""
Funções que envolvem os dados
"""

""" Insere os dados nos dados  :)
De 1 a 6 os dados são verdes, de 7 a 10 amarelos e 11 a 13 vermelho, cada dado recebe 6 lados,
contendo cérebro.
"""

# Feito uma tupla contendo os tres dado com suas respectivas cores e seus lados
# que serão verificados conforme o sorteio randomico
def dados():
    dado = ("VERDE", "CEREBRO", "PASSO", "CEREBRO", "TIRO", "PASSO", "CEREBRO"), (
        "AMARELO", "TIRO", "PASSO", "CEREBRO", "TIRO", "PASSO", "CEREBRO"), (
               "VERMELHO", "TIRO", "PASSO", "TIRO", "CEREBRO", "PASSO", "TIRO")
    return dado


# Tubo Grande que mostra os dados disponíveis dentro
# V= Verde A= Amarelo Vermelho= X
# a = a quantidade de verde, b = amarelo, c = vermelho
def tubo(a, b, c):
    print(f'\n{"POTE!":^40}')
    print(f'{" "*10}{"-" * 20} ')
    sys.stdout.write(f'{"VERDE":^10}|')
    for l in range(6):
        if a > l:
            sys.stdout.write(" V ")
        else:
            sys.stdout.write("   ")
    print(" \ ")
    sys.stdout.write(f'{"AMARELO":^10}|')
    for l in range(6):
        if b > l:
            sys.stdout.write(" A ")
        else:
            sys.stdout.write("   ")
    print("  |")
    sys.stdout.write(f'{"VERMELHO":^10}|')
    for l in range(6):
        if c > l:
            sys.stdout.write(" X ")
        else:
            sys.stdout.write("   ")
    print(" / ")
    print(f'{" "*10}{"-" * 20} \n')


# Verifica ganhador e faz o mata mata
# indice a = jogadores, indice b = quantJog, indice c = Bolleano caso ja tenha entrado no mata mata
def ver_Ganhador(a, b, c, d):
    contador = 0
    mata_mata = []
    for l in range(1, b + 1):
        if a[l][1] >= 13:
            mata_mata.append(l)
    if c == True:
        if len(d) >= 1:
            for l in range(0,len(d)):  # (len(mata_mata)+1)
                if a[d[0]][2] != a[d[l]][2]:
                    contador += 1
            if contador == 0:
                if len(d) >= 2:
                    lista = posicoes(a, b)
                    for l in range(len(d) - 1, -1, -1):
                        if a[lista[0]][1] > a[d[l]][1]:
                            d.pop(l)
                    return d
                if len(d) == 1:
                    return d
            else:
                return d

    elif c == False:
        if len(mata_mata) >= 1 and mata_mata != 12203:
            for l in range(1, b + 1): 
                if a[mata_mata[0]][2] != a[l][2]:
                    contador += 1
            if contador == 0:
                if len(mata_mata) >= 2:
                    lista = posicoes(a, b)
                    for l in range(len(mata_mata) - 1, -1, -1):
                        if a[lista[0]][1] > a[mata_mata[l]][1]:
                            mata_mata.pop(l)
                    return mata_mata
                if len(mata_mata) == 1:
                    return mata_mata
    if c == False:
        mata_mata = [12203]
        return mata_mata

# Organiza as posções dos jogadores e elimina os que estão com menos de 13 pontos.
# Pode ser usado para criar um ranking mais dinâmico"
# indice a = jogadores, b = quantJog
def posicoes(a,b):
    lista = []
    for l in range(1, b + 1):
        lista.append(l)
    for l in range(0, b + 1):
        for c in range(l, b):
            if a[lista[l]][1] < a[lista[c]][1]:
                aux = lista[c]
                aux2 = lista[l]
                lista.pop(c)
                lista.insert(c, aux2)
                lista.pop(c)
                lista.insert(l, aux)
    return lista


# Função para ter uma pré-visualização das cores dos dados sorteados
# a = sorte (variavel com um numero aleatorio)
def rolDados(a):
    for l in range(3):
        c = random.randint(1, 6)
        if l == 0:
            print(f'{dado[a][0]:^16}{" -> ":^16}{dado[a][c]:^16}')
        elif l == 1:
            print(f'{dado[a][0]:^16}{" -> ":^16}{dado[a][c]:^16}')
        else:
            print(f'{dado[a][0]:^16}{" -> ":^16}{dado[a][c]:^16}')
        return dado[a][c]


# Faz uma lista contendo os três dados que o jogador sorteou
def listDados():
    jogadas = []
    while passe == True:
        for l in range(verde):
            jogadas.append(0)
        for _ in range(amarelo):
            jogadas.append(1)
        for _ in range(vermelho):
            jogadas.append(2)
        break
    return jogadas


# Início #######################################################################################
jogadores = []              # Lista de jogadores
passe = True                # Variável para conceder licensa para entrar nas estruturas de reptiçao
ganhador = False            # Variavel para verificar se ja ouve um ganhador, para iniciar na proxima rodada
regras()
passo_List = []             # Lista de dados que cairam em passo para serem rejogados novamente
mata_mata = []              # Lista para a morte subita em caso de empate
while passe == True or reset == True:
    gamer = 0
    reset = False           # Em caso o jogador quiser resetar, será utilizado esta variavel
    passe = True
    quantJog = 0            # Usado para determinar a quantidade de jogadores
    jogador = "inicio123"   # Variavel para adicionar jogador
    jogadores.append(insere_jogadores(jogador))     # Preenche a linha zero da lista dos nomes para referência
    titulo()        # Chama a função Titulo
    while passe == True:                            # Insere os jogadores, limitado até 4 jogadores
        while True:
            separador()
            print("PARA CONTINUAR DIGITE -> ok")
            jogador = input("Insira " + str(quantJog + 1) + "º Jogador: ")
            jogador = verifica_jogador(jogador,jogadores,quantJog)
            if jogador == "ok":
                break
            jogadores.append(insere_jogadores(jogador))
            quantJog += 1
            # if quantJog == 4: Esta linha é para caso queira limitar os jogadores
                # break
            # break

        # Abre o menu caso o jogador queira fazer alguma alteração antes do jogo
        while passe == True or ganhador == True:
            while True:
                showPlacar(quantJog)
                options = (
                    f'{"[1] Continuar":^45}\n{"[2] Ver regras":^45}\n{"[3] Incluir jogador":^45}\n{"[4] Alterar jogador":^45}\n'
                    f'{"[5] Excluir jogador":^45}\n{"[6] Zerar ranking":^45}\n{"[7] Resetar":^45}\n{"[0] Fechar jogo":^45}\n')
                print(options)
                while True:
                    try:
                        continuar = int(input("insira a opção escolhida: "))
                        break
                    except ValueError:
                        print("Insira uma opção válida")
                if continuar == 2:                          # Ver Regras
                    while True:
                        regras()
                        break
                elif continuar == 3:                        # Incluir Jogador
                    jogador = input("Insira o nome do Jogador: ")
                    jogador = verifica_jogador(jogador, jogadores, quantJog)
                    jogadores.append(insere_jogadores(jogador))
                    quantJog += 1
                elif continuar == 4:                        # Alterar jogador
                    jogador = input("Qual jogador deseja alterar: ")
                    for l in range(quantJog + 1):
                        if jogador == jogadores[l][0]:
                            while True:
                                print(f'{"Alterando jogador"}{jogadores[l][0]}')
                                jogador = input("Insira " + str(l) + "º Jogador: ")
                                jogadores[l][0] = verifica_jogador(jogador, jogadores, quantJog)
                                break
                elif continuar == 5:                        # Excluir Jogador
                    cont = 0
                    passe = True
                    if quantJog == 2:
                        print("Não é possível excluir jogador (mínimo 2 jogadores)")
                    else:
                        while True:
                            jogador = input("Qual jogador deseja excluir:")
                            for l in range(quantJog + 1):
                                if cont == 1:
                                    break
                                elif jogador == jogadores[l][0]:
                                    while True:
                                        jogadores.pop(l)
                                        quantJog -= 1
                                        cont = 1
                                        break
                            if cont == 1:
                                break
                            elif cont == 0:
                                continuar = input("Jogador não encontrado!")
                                break
                elif continuar == 6:                    # Zerar Ranking
                    for l in range(1, quantJog + 1):
                        for c in range(1, 5):
                            jogadores[l][c] = 0
                elif continuar == 7:                    # Resetar
                    jogadores.clear()
                    passe = False
                    reset = True
                    break
                elif continuar == 0:                    # Fechar jogo
                    passe = False
                    reset = False
                    ganhador = False
                    break
                else:                                   # Retorna
                    break

                # Inicio do rolar de dados #################################################
            rodada = 0
            final = False
            lista_reposicao = []
            while passe == True:
                jogar = 0
                ganhador = False
                rodada = 1
                cont = 0            # Contador para controlar a quantidade de 3 dados sorteados
                cer = 0             # armazena os cerebros da rodada
                tir = 0             # armazenda os tiros da rodada
                pas = 0             # armazena os passos da rodada
                titulo()
                dado = dados()      # recebe uma tupla com a cor do dado e sua respectiva cor
                verde = 6           # armazena a quantidade de dados da cor ...
                amarelo = 4
                vermelho = 3
                if gamer == 0:
                    gamer = random.randint(1, quantJog)
                showPlacar(quantJog)
                print(f'{"vez do ZUMBI":^7}{"-->  "}{jogadores[gamer][0]}')
                continuar = input("Pressione ENTER: \n")
                while True:
                    if jogar == 2:                      # Sorteio mostra as cores dos dados
                         break
                    jogadas = listDados()
                    while True:
                        if len(jogadas) == 0:
                            jogadas.extend(lista_reposicao)
                            for l in range(len(lista_reposicao)):
                                if lista_reposicao[0] == 0:
                                    verde += 1
                                elif sorte == 1:
                                    amarelo += 1
                                else:
                                    vermelho += 1
                            lista_reposicao.clear()
                        if pas > 0:                      # rola os dados que contém passo
                            sorte = random.choice(passo_List)
                            passo_List.remove(sorte)
                            pas -= 1
                        else:
                            sorte = random.choice(jogadas)
                            jogadas.remove(sorte)
                            if sorte == 0:
                                verde -= 1
                            elif sorte == 1:
                                amarelo -= 1
                            else:
                                vermelho -= 1
                        if cont == 0:
                            cor1 = sorte
                        elif cont == 1:
                            cor2 = sorte
                        else:
                            cor3 = sorte
                        sys.stdout.write(f'{dado[sorte][0] :^17}')  # imprime as cores dos dados
                        if cont == 2:
                            break
                        else:
                            cont += 1
                    cont = 0
                    print("")                                       # Mostra o resultado dos dados
                    continuar = input(f'\n{"ENTER PARA LANÇAR":^49}\n\n')
                    sorte = rolDados(cor1)
                    if sorte == "CEREBRO":
                        cer += 1
                    elif sorte == "TIRO":
                        tir += 1
                    elif sorte == "PASSO":
                        pas += 1
                        passo_List.append(cor1)
                    sorte = rolDados(cor2)
                    if sorte == "CEREBRO":
                        cer += 1
                    elif sorte == "TIRO":
                        tir += 1
                    elif sorte == "PASSO":
                        pas += 1
                        passo_List.append(cor2)
                    sorte = rolDados(cor3)
                    if sorte == "CEREBRO":
                        cer += 1
                    elif sorte == "TIRO":
                        tir += 1
                    elif sorte == "PASSO":
                        pas += 1
                        passo_List.append(cor3)
                    print(f'{"-"*49}\n'
                          f'|{"Cerebro(s)":^15}|{"Passo(s)":^15}|{"Tiro(s)":^15}|\n'
                          f'|{cer :^15}|{pas :^15}|{tir:^15}|\n'
                          f'{"-"*49}\n')
                    if tir >= 3:
                        tir = 0
                        cer = 0
                        pas = 0
                        continuar = input(f'\n{" XIII! VOCÊ TOMOU TRÊS TIROS, OS CÉREBROS FORAM PERDIDOS!"}\n'
                                          f'{"PRESSIONE ENTER CONTINUAR"}')
                        jogadores[gamer][2] += 1
                        mata_mata = ver_Ganhador(jogadores, quantJog, final,mata_mata)  ##############
                        gamer = muda_jogador(gamer, quantJog, mata_mata)
                        passo_List.clear()
                        passe = False
                        jogar = 2
                    else:
                        tubo(verde, amarelo, vermelho)          # Mostra o tubo contendo os dados disponíveis.
                        while passe == True:
                            try:
                                passe = True
                                jogar = int(input(f'{"ZUMBI":^7}{"-->  "}{jogadores[gamer][0]}\n'
                                                  f'{" CONTINUAR->[1], PASSAR->[2], POTE[3], RANKING[4], REGRAS[5],"}'
                                                  f'{" DADOS ->[6]"}\n'))
                                if jogar == 1:
                                    passe = True
                                    break
                                elif jogar == 2:
                                    jogadores[gamer][1] += cer
                                    jogadores[gamer][2] += 1                # acrescenta uma rodada
                                    passo_List.clear()
                                    mata_mata = ver_Ganhador(jogadores, quantJog, final,mata_mata)
                                    gamer = muda_jogador(gamer, quantJog, mata_mata)
                                    passe = False
                                    separador()
                                    break
                                elif jogar == 3:
                                    tubo(verde, amarelo, vermelho)
                                elif jogar == 4:
                                    showPlacar(quantJog)
                                elif jogar == 5:
                                    regras()
                                elif jogar == 6:
                                    print(f'\n{"Cerebro(s)":^10}{"Passo(s)":^10}{"Tiro(s)":^10}\n'
                                          f'{cer :^10}{pas :^10}{tir:^10}')
                            except ValueError:
                                print("OPÇÃO INVÁLIDA")
                    cont = 0
                    mata_mata = ver_Ganhador(jogadores, quantJog, final,mata_mata)
                    if mata_mata[0] != 12203:
                        final = True
                        passe = True
                    if len(mata_mata) >= 1 and mata_mata[0] != 12203:
                        if len(mata_mata) == 1:
                            showPlacar(quantJog)
                            jogadores[mata_mata[0]][3] += 1
                            jogar =input(f'{"VITÓRIA DO ZUMBI -->"}{jogadores[mata_mata[0]][0]}\n')
                            ganhador = True
                            gamer = int(mata_mata[0])
                            mata_mata.clear()
                            passe = True
                            jogar = 2
                            for l in range(1, quantJog + 1):
                                for c in range(1, 3):
                                    jogadores[l][c] = 0
                            break
                    if passe == False and mata_mata[0] == 12203:
                        passe = True
                        break
                if ganhador == True:
                    if passe == False:
                        ganhador = False
                        break
                    else:
                        break
print("Adeus...")
