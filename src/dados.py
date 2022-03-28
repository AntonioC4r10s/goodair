import pandas as pd
from matplotlib import pyplot as plt

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

def gera_grafico(arq):
    df = pd.read_csv(arq)

    fig, axs = plt.subplots(2, 2)

    axs[0, 0].plot(df['entrada'], df['pessoas'], label='pessoas')
    axs[0, 0].set_title("Número de pessoas")
    axs[0, 0].legend()

    axs[0, 1].plot(df['entrada'], df['umidade'], label='umidade')
    axs[0, 1].set_title("Umidade relativa do ar")
    axs[0, 1].legend()

    axs[1, 0].plot(df['entrada'], df['temperatura'], label='temperatura')
    axs[1, 0].set_title("Temperatura")
    axs[1, 0].legend()

    axs[1, 1].plot(df['entrada'], df['resposta'], label='resposta')
    axs[1, 1].set_title("Resposta fuzzy")
    axs[1, 1].legend()

#    plt.show()
    return fig

#gera_grafico("/home/antonio/PycharmProjects/goodair/src/save/saida13:26:35.csv")