import time
import serial
import re
from src.lfuzzy import gera_fuzzy
from time import sleep
from src.dados import grava_dados


while True:
    try:
        arduino = serial.Serial('/dev/ttyUSB0', 9600)
        print("Arduino conectado!")
        break
    except:
        pass

nome_arq = "saida"+time.strftime("%X")
v_pessoas = []
v_umidade = []
v_resposta = []
v_temperatura = []

while True:
    msg = str(arduino.readline())
    msg = msg[2:-5]
    msg_data = re.split(': |, ', msg)
    print(msg_data)

    umidade = float(msg_data[1])
    pessoas = int(msg_data[3])
    temperatura = float(msg_data[5])

    v_umidade.append(umidade)
    v_pessoas.append(pessoas)
    v_resposta.append(gera_fuzzy(umidade, pessoas))
    v_temperatura.append(temperatura)

    grava_dados(v_pessoas, v_umidade, v_temperatura,v_resposta, nome_arq)
    arduino.flush()

