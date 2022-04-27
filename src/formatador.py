import pandas as pd
import time
from lfuzzy import gera_fuzzy
from dados import grava_dados_2
import csv

print("Insira o que deseja fazer:"
      "\n1- Criar novo arquivo"
      "\n2- Editar arquivo existente - (alterar o número de pessoas)"
      "\n3- Editar arquivo existente - (alterar o número de pessoas e fuzzy)"
      "\n4- Consertar a numeração")
option = int(input())

if option == 1:

    NOMEDOARQUIVO = "saida" + time.strftime('%Y_%m_%d_%H_%M_%S')
    entrada = 0

    grava_dados_2('entrada,pessoas,umidade,temperatura,resposta', NOMEDOARQUIVO)

    while True:
        l = int(input("Digite o número de linhas: "))
        if l == 0:
            break
        p = input("Digite o número de pessoas: ")
        t = input("Digite a temperatura: ")
        u = input("Digite a umidade: ")

        f = gera_fuzzy(u, p)


        for i in range(0, l):
            linha = (str(entrada) + ',' + str(p) + ',' + str(u) + ',' + str(t) + ',' + str(f))
            grava_dados_2(linha, NOMEDOARQUIVO)
            entrada += 1
        print("\n" + ('entrada: '+ str(entrada) + ',' +'pessoas: '+ str(p) + ',' + 'umidade: '+ str(u) + ',' +
                      'temperatura: ' + str(t) + ',' + 'saída: ' + str(f)) + '\n')

if option == 2:
    nomedoarquivo = input("Insira o nome do arquivo que será alterado ")
    nomedoarquivo = 'save/' + nomedoarquivo
    nlinha = int(input("A partir de qual linha ocorrerá a alteração? "))

    arquivo = open(nomedoarquivo, 'r')
    csv_file = csv.reader(arquivo)
    dados = list(csv_file)
    NOVOARQUIVO = "novo"
#    open(NOVOARQUIVO, 'w')

    grava_dados_2('entrada,pessoas,umidade,temperatura,resposta', NOVOARQUIVO)

    for i in range(0, nlinha - 1):
        centrada = i
        cp = dados[i][1]
        ct = dados[i][3]
        cu = dados[i][2]
        cf = dados[i][4]

        print(centrada)
        copia = (str(centrada) + ',' + str(cp) + ',' + str(cu) + ',' + str(ct) + ',' + str(cf))
        grava_dados_2(copia, NOVOARQUIVO)

    while nlinha < len(dados):
        l = int(input("Insira o número de linhas que serão alteradas: "))
        if l == 0:
            break
        p = int(input("Insira o número de pessoas: "))
        t = float(dados[nlinha][3])
        u = float(dados[nlinha][2])
        f = gera_fuzzy(u, p)
        linha = (str(nlinha) + ',' + str(p) + ',' + str(u) + ',' + str(t) + ',' + str(f))

        for j in range(nlinha, nlinha + l):
            #print(j)
            grava_dados_2(linha, NOVOARQUIVO)

            #print("\n" + ('entrada: ' + str(nlinha) + ',' + 'pessoas: ' + str(p) + ',' + 'umidade: ' + str(u) + ',' +
            #          'temperatura: ' + str(t) + ',' + 'saída: ' + str(f)) + '\n')
            nlinha = nlinha + 1

        lpfim = len(dados) - nlinha
        print("Faltam " + str(lpfim) + " para o fim")

if option == 3:
    pass

if option == 4:
    nomedoarquivo = input("Insira o nome do arquivo que será alterado ")
    nomedoarquivo = 'save/' + nomedoarquivo

    arquivo = open(nomedoarquivo, 'r')
    csv_file = csv.reader(arquivo)
    dados = list(csv_file)
    NOVOARQUIVO = "novo_contagem"
    #    open(NOVOARQUIVO, 'w')

    grava_dados_2('entrada,pessoas,umidade,temperatura,resposta', NOVOARQUIVO)

    for i in range(0, len(dados)):
        centrada = i
        cp = dados[i][1]
        ct = dados[i][3]
        cu = dados[i][2]
        cf = dados[i][4]

        print(centrada)
        copia = (str(centrada) + ',' + str(cp) + ',' + str(cu) + ',' + str(ct) + ',' + str(cf))
        grava_dados_2(copia, NOVOARQUIVO)


print("Finalizado...")
