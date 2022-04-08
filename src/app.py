import dados
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time
from tkinter import Tk, Frame, Button, Label, ttk, Canvas
import random
import re
import serial
import lfuzzy

CONNECTED = False
PAUSE = False
START = False
ARDUINO = ""
PESSOAS = 0
NOME_ARQ = "saida" + time.strftime('%Y_%m_%d_%H_%M_%S')
print(NOME_ARQ)
dados.grava_dados_2('entrada,pessoas,umidade,temperatura,resposta', NOME_ARQ)

fig, axs = plt.subplots(2, 2, facecolor='#B0E0E6')

x = np.arange(0, 1, 1)
axs[0, 0].set_title("Number of People")
axs[0, 1].set_title("Air Humidity")
axs[1, 0].set_title("Temperature")
axs[1, 1].set_title("Fuzzy Output")

line1, = axs[0, 0].plot(x, random.random(), color='blue', marker='o', linestyle='dotted', linewidth=5, markersize=1,
                        markeredgecolor='m')
line2, = axs[0, 1].plot(x, random.random(), color='green', marker='o', linestyle='dotted', linewidth=5, markersize=1,
                        markeredgecolor='m')
line3, = axs[1, 0].plot(x, random.random(), color='red', marker='o', linestyle='dotted', linewidth=5, markersize=1,
                        markeredgecolor='m')
line4, = axs[1, 1].plot(x, random.random(), color='yellow', marker='o', linestyle='dotted', linewidth=5, markersize=1,
                        markeredgecolor='m')


def animate(i):
    line1.set_ydata(random.random())
    line2.set_ydata(random.random())
    line3.set_ydata(random.random())
    line4.set_ydata(random.random())
    return line1, line2, line3, line4


def conectar():
    try:
        global ARDUINO
        ARDUINO = serial.Serial('COM3', 9600)
        # print("Arduino connected!")
        janela.title("GoodAir - Connected")
        name = "saida_" + time.strftime("%Y_%m_%d_%H_%M")
        global CONNECTED
        CONNECTED = True
    except:
        janela.title("GoodAir - No Connected")
        CONNECTED = False


def start():
    global ani
    ani = animation.FuncAnimation(fig, animate, interval=20, blit=True, save_count=10)
    canvas.draw()
    global START
    START = True


def pause():
    # ani.event_source.stop()
    print("pause")
    global PAUSE
    PAUSE = True


def continuar():
    # ani.event_source.start()
    global PAUSE
    PAUSE = False


def close():
    janela.destroy()
    exit()


def atualiza():
    janela.update()


#   time.sleep(0.25)

def getin():
    global PESSOAS
    PESSOAS = PESSOAS + 1


#    global pessoas
#    pessoas = pessoas + 1

def goout():
    global PESSOAS
    PESSOAS = PESSOAS - 1
    if PESSOAS < 0:
        PESSOAS = 0


janela = Tk()
janela.geometry('900x700')
janela.title('GoodAir')
janela.minsize(width=720, height=480)

frame = Frame(janela, bg='white', bd=3)
frame.pack(expand=1, fill='both')

canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().pack(padx=5, pady=5, expand=1, fill='both')

Button(frame, text='Iniciar', width=15, bg='purple4', fg='white', command=start).pack(pady=5, side='left', expand=1)
Button(frame, text='Pausar', width=15, bg='purple4', fg='white', command=pause).pack(pady=5, side='left', expand=1)
Button(frame, text='Continuar', width=15, bg='purple4', fg='white', command=continuar).pack(pady=5, side='left',
                                                                                            expand=1)
Button(frame, text='Entra Pessoa', width=15, bg='purple4', fg='white', command=getin).pack(pady=5, side='left',
                                                                                           expand=1)
Button(frame, text='Sai Pessoa', width=15, bg='purple4', fg='white', command=goout).pack(pady=5, side='left', expand=1)
Button(frame, text='Sair', width=15, bg='purple4', fg='white', command=close).pack(pady=5, side='left', expand=1)

conectar()

i = 0
pessoas = 0
amostra = 0

while True:

    if (CONNECTED == True and PAUSE == False and START == True):
        msg = str(ARDUINO.readline())
        msg = msg[2:-5]
        msg_data = re.split(': |, ', msg)
        # print(msg_data)

        umidade = float(msg_data[1])
        # pessoas = int(msg_data[3])
        pessoas = PESSOAS
        temperatura = float(msg_data[5])
        resposta = lfuzzy.gera_fuzzy(umidade, pessoas)

        if i == 0:
            linha = (str(amostra) + ',' + str(pessoas) + ',' + str(umidade) + ',' + str(temperatura) + ',' + str(resposta))
            print(linha)
            