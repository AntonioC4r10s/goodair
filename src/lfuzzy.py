import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from time import sleep

def gera_fuzzy(valor_umidade, valor_pessoas):
    #  Universo de variaveis.
    x_umidade = np.arange(0, 101, 1)
    x_npessoas = np.arange(0, 21, 1)
    x_umidificador = np.arange(0, 101, 1)

    #   Funções fuzzy
    umid_ruim = fuzz.trapmf(x_umidade, [0, 0, 40, 50])
    umid_boa = fuzz.trimf(x_umidade, [40, 60, 80])
    umid_excessiva = fuzz.trimf(x_umidade, [70, 100, 100])

    npessoas_nenhuma = fuzz.trapmf(x_npessoas, [0, 0, 0, 0])
    npessoas_poucas = fuzz.trapmf(x_npessoas, [1, 1, 5, 12])
    npessoas_muitas = fuzz.trapmf(x_npessoas, [6, 15, 21, 21])

    umidif_alto = fuzz.trapmf(x_umidificador, [0, 0, 25, 50])
    umidif_normal = fuzz.trimf(x_umidificador, [20, 50, 80])
    umidif_desligado = fuzz.trapmf(x_umidificador, [50, 75, 100, 100])

    qualid_umidade_ruim = fuzz.interp_membership(x_umidade, umid_ruim, valor_umidade)
    qualid_umidade_boa = fuzz.interp_membership(x_umidade, umid_boa, valor_umidade)
    qualid_umidade_exces = fuzz.interp_membership(x_umidade, umid_excessiva, valor_umidade)

    numero_pess_nenhuma = fuzz.interp_membership(x_npessoas, npessoas_nenhuma, valor_pessoas)
    numero_pess_poucas = fuzz.interp_membership(x_npessoas, npessoas_poucas, valor_pessoas)
    numero_pess_muitas = fuzz.interp_membership(x_npessoas, npessoas_muitas, valor_pessoas)

    # Regra 1
    ativar_regra1 = np.fmax(qualid_umidade_exces, numero_pess_nenhuma)
    ativa_umidificado_desligado = np.fmin(ativar_regra1, umidif_desligado)

    # Regra 2
    ativar_regra2 = np.fmax(qualid_umidade_boa, numero_pess_poucas)
    ativa_umidificado_normal = np.fmin(ativar_regra2, umidif_normal)

    # Regra 3
    ativar_regra3 = np.fmax(qualid_umidade_ruim, numero_pess_muitas)
    ativa_umidificado_alto = np.fmin(ativar_regra3, umidif_alto)

    # Aggregate all three output membership functions together
    aggregated = np.fmax(ativa_umidificado_alto,
                         np.fmax(ativa_umidificado_normal, ativa_umidificado_desligado))
    # Calculate defuzzified result
    tip = fuzz.defuzz(x_umidificador, aggregated, 'centroid')
#    tip_activation = fuzz.interp_membership(x_umidificador, aggregated, tip)  # for plot

    #print(tip)
    return (tip)
