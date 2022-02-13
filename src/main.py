import serial
import re
from src.lfuzzy import gera_fuzzy
from time import sleep

while True:
    try:
        arduino = serial.Serial('/dev/ttyUSB0', 9600)
        print("Arduino conectado!")
        break

    except:
        pass

while True:
    msg = str(arduino.readline())
    msg = msg[2:-5]
    #print(msg)

    msg_data = re.split(': |, ', msg)
    print(msg_data)
    umidade = float(msg_data[1])
    pessoas = int(msg_data[3])

    gera_fuzzy(umidade, pessoas)
    arduino.flush()

