import pandas as pd
from matplotlib import pyplot as plt

def grava_dados(v_pessoas, v_umidade, v_resposta, arq):

    datas = {
        'pessoas': v_pessoas,
        'umidade': v_umidade,
        'resposta': v_resposta
    }

    saida = pd.DataFrame(datas)
    type(saida)
    saida.to_csv("save/"+arq+".csv")

def gera_grafico(arq):
    df = pd.read_csv(arq)

    fig, (ax0, ax1 ,ax2) = plt.subplots(3)

    ax0.plot(df['entrada'], df['pessoas'], label='pessoas')
    ax0.set_title("Número de pessoas")
    ax0.legend()

    ax1.plot(df['entrada'], df['umidade'], label='umidade')
    ax1.set_title("Umidade relativa do ar")
    ax1.legend()

    ax2.plot(df['entrada'], df['resposta'], label='resposta')
    ax2.set_title("Resposta fuzzy")
    ax2.legend()

    plt.show()

gera_grafico("/home/antonio/PycharmProjects/goodair/src/save/saida17:22:19.csv")