import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as ss

def f_linear_c(x):
    return x

def f_linear_d(x):
    return -x

def f_trap():
    return [0, 1, 1, 1, 0]

def gera_grafico_linear():
    x = np.linspace(0, 4)
    fig, (ax0, ax1) = plt.subplots(1, 2)

    ax0.plot(x, f_linear_c(x))
    ax0.set_title("Linear Crescente")

    ax1.plot(x, f_linear_d(x), color='red')
    ax1.set_title("Linear Decrescente")

    plt.show()

def gera_grafico_trap():
    x = [0, 1, 2, 3, 4]
    y = f_trap()

    plt.plot(x, y)
    plt.title("Função Trapezoidal")

    plt.text(0.1, 0, 'A')
    plt.plot(0, 0, marker='.', markersize=20)

    plt.text(1.1, 1, 'B')
    plt.plot(1, 1, marker='.', markersize=20)

    plt.text(3.1, 1, 'C')
    plt.plot(3, 1, marker='.', markersize=20)

    plt.text(3.9, 0, 'D')
    plt.plot(4, 0, marker='.', markersize=20)
    plt.show()

def gera_grafico_tri():
    x = [0, 1, 2]
    y = [0, 1, 0]

    plt.plot(x, y)
    plt.title("Função Triangular")

    plt.text(0.1, 0, 'A')
    plt.plot(0, 0, marker='.', markersize=20)

    plt.text(1.1, 1, 'B')
    plt.plot(1, 1, marker='.', markersize=20)

    plt.text(1.9, 0, 'C')
    plt.plot(2, 0, marker='.', markersize=20)

    plt.show()

def impulso(n):
    if n == 0:
        return 1
    else:
        return 0



def gera_grafico_impulso():
        #x = [0, 1, 2, 3, 4]
        x = np.linspace(0, 300, 300)
        y = ss.unit_impulse(300, 40)

        plt.plot(x, y)
        plt.title("Função Siglenton")
        plt.text(42.1, 1, 'a')
        plt.plot(40, 1, marker='.', markersize=20)

        plt.show()

def gera_grafico_transito_1():
    x = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
    y = [16375728, 16542327,17348067,17939815,16541515,13849665,13028944,12261529,10546694,8721541,
    7062601,5444715,4600929,3581106,2742302,1779587,1036034,403099]
    plt.plot(x, y)
    plt.title("Risco de morte no trânsito (ano 2000)")
    plt.xlabel("Idade")
    plt.ylabel("Habitantes")
    plt.show()


gera_grafico_transito_1()