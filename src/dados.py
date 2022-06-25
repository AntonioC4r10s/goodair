import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import collections as mc
import matplotlib.patches as mpatches

def grava_dados(v_pessoas, v_umidade, v_temperatura,v_resposta, arq):

    datas = {
        'pessoas': v_pessoas,
        'umidade': v_umidade,
        'temperatura': v_temperatura,
        'resposta': v_resposta
    }

    saida = pd.DataFrame(datas)
    type(saida)
    saida.to_csv("save/"+arq+".csv")

def grava_dados_2(linha, arq):

    arquivo = open('save/'+ arq + '.csv', 'a+')
    arquivo.write(linha+'\n')
    arquivo.close()

def gera_grafico(arq):
    df = pd.read_csv(arq)

    fig, axs = plt.subplots(2, 2)

    axs[0, 0].plot(df['entrada'], df['pessoas'], label='pessoas')
    axs[0, 0].set_title("(a) Número de pessoas")
    axs[0, 0].legend()

    axs[0, 1].plot(df['entrada'], df['umidade'], label='umidade')
    axs[0, 1].set_title("(b) Umidade relativa do ar")
    axs[0, 1].legend()

    axs[1, 0].plot(df['entrada'], df['temperatura'], label='temperatura')
    axs[1, 0].set_title("(c) Temperatura")
    axs[1, 0].legend()

    axs[1, 1].plot(df['entrada'], df['resposta'], label='resposta')
    axs[1, 1].set_title("(d) Resposta fuzzy")
    axs[1, 1].legend()

    plt.show()
    return fig

def gera_grafico_3(arq):
    df = pd.read_csv(arq)
    fig, axs = plt.subplots(2, 2)


#   a) Número de pessoas

    x_pessoas = df['entrada'].to_list()
    y_pessoas = df['pessoas'].to_list()
    i_pessoas = 0
    segments_pessoas = []
    colors_pessoas = np.zeros(shape=(len(y_pessoas), 4))

    for x1, x2, y1, y2 in zip(x_pessoas, x_pessoas[1:], y_pessoas, y_pessoas[1:]):
        if y1 < 1:
            colors_pessoas[i_pessoas] = tuple([1, 0, 0, 1])
        if y1 >= 1 and y1 < 10:
            colors_pessoas[i_pessoas] = tuple([0, 1, 0, 1])
        if y1 >= 10:
            colors_pessoas[i_pessoas] = tuple([0, 0, 1, 1])
        segments_pessoas.append([(x1, y1), (x2, y2)])
        i_pessoas += 1

    lc_saida = mc.LineCollection(segments_pessoas, colors=colors_pessoas, linewidths=2)
    axs[0, 0].plot(x_pessoas, y_pessoas)
    axs[0, 0].add_collection(lc_saida)
    axs[0, 0].set_title("(a) Número de Pessoas")
    pop_a_pessoas = mpatches.Patch(color='r', label='Nenhuma')
    pop_b_pessoas = mpatches.Patch(color='g', label='Poucas')
    pop_c_pessoas = mpatches.Patch(color='b', label='Muitas')
    axs[0, 0].legend(handles=[pop_a_pessoas, pop_b_pessoas, pop_c_pessoas])


#   b) Umidade

    x_umidade = df['entrada'].to_list()
    y_umidade = df['umidade'].to_list()
    i_umidade = 0
    segments_umidade = []
    colors_umidade = np.zeros(shape=(len(y_umidade), 4))

    for x1, x2, y1, y2 in zip(x_umidade, x_umidade[1:], y_umidade, y_umidade[1:]):
        if y1 < 50:
            colors_umidade[i_umidade] = tuple([1, 0, 0, 1])
        if y1 >= 50 and y1 < 75:
            colors_umidade[i_umidade] = tuple([0, 1, 0, 1])
        if y1 >= 75:
            colors_umidade[i_umidade] = tuple([0, 0, 1, 1])
        segments_umidade.append([(x1, y1), (x2, y2)])
        i_umidade += 1

    lc_umidade = mc.LineCollection(segments_umidade, colors=colors_umidade, linewidths=2)
    axs[0, 1].plot(x_umidade, y_umidade)
    axs[0, 1].add_collection(lc_umidade)
    axs[0, 1].set_title("(b) Umidade Relativa do Ar")
    pop_a_umidade = mpatches.Patch(color='r', label='Ruim')
    pop_b_umidade = mpatches.Patch(color='g', label='Boa')
    pop_c_umidade = mpatches.Patch(color='b', label='Excessiva')
    axs[0, 1].legend(handles=[pop_a_umidade, pop_b_umidade, pop_c_umidade])

#   c) Temperatura

    axs[1, 0].plot(df['entrada'], df['temperatura'], label='Temperatura', color='r')
    axs[1, 0].set_title("(c) Temperatura")
    axs[1, 0].legend(handles=[mpatches.Patch(color='r', label='Temperatura')])


#   d) Saída:

    x_saida = df['entrada'].to_list()
    y_saida = df['resposta'].to_list()
    i_saida = 0
    segments_saida = []
    colors_saida = np.zeros(shape=(len(y_saida), 4))

    for x1, x2, y1, y2 in zip(x_saida, x_saida[1:], y_saida, y_saida[1:]):
        if y1 < 50:
            colors_saida[i_saida] = tuple([1, 0, 0, 1])
        if y1 >= 50 and y1 < 70:
            colors_saida[i_saida] = tuple([0, 1, 0, 1])
        if y1 >= 70:
            colors_saida[i_saida] = tuple([0, 0, 1, 1])
        segments_saida.append([(x1, y1), (x2, y2)])
        i_saida += 1

    lc_saida = mc.LineCollection(segments_saida, colors=colors_saida, linewidths=2)
    axs[1, 1].plot(x_saida, y_saida)
    axs[1, 1].add_collection(lc_saida)
    axs[1, 1].set_title("(d) Resposta Fuzzy")
    pop_a_saida = mpatches.Patch(color='r', label='Alto')
    pop_b_saida = mpatches.Patch(color='g', label='Normal')
    pop_c_saida = mpatches.Patch(color='b', label='Desligado')
    plt.legend(handles=[pop_a_saida, pop_b_saida, pop_c_saida])


#   Plot

    plt.show()
    return fig

#arquivo = ("src/save-coleta/dia-4.csv")
#arquivo = arquivo[4:]
#gera_grafico_3(arquivo)