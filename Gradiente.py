'''
Implementar o Algoritmo do Gradiente na orimização do seguinte problema: 
    min f(x1, x2) = (x1 - 1)^2 + 2x2^2
.Inicialmente, plotar as curvas de nível da função objetivo;
.Plotar o valor de  f(x¯)  ao longo das iterações;
.Ao final, marcar o ponto  x¯∗  no gráfico inicial;
.Ter uma função que retorne o valor de  f(x¯)  e de  ∇f(x¯)  para um dado  x¯ ;
.Número máximo de iterações: 100;
.Precisão ϵ=10−2 ;
.Critérios de parada:
    Número máximo de iterações
    ||∇f(x¯)||≤ϵ
.Ponto inicial:  x¯0=[10,10]T
'''

# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 00:01:55 2022

@author: Cristian
"""

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

n = 28
grad = np.zeros(n)
pre = 10**(-1)                                          #precisão

dados = pd.DataFrame()
dados['x'] = np.linspace(10,0,11)
dados['y'] = np.linspace(10,0,11)
x1 = dados['x']
x2 = dados['y']

def f_x(x1, x2):
    """
    Parameters
    ----------
    x1 (float): Ponto X1 da funcão no eixo x.
    x2 (float): Ponto X2 da função no eixo y.

    Returns
    -------
    f_x (float): Após o calculo, irá me retornar o vetor 'Z'
    """
    return (x1-1)**2 + 2*x2**2


def f_gradX(x1, x2):
    """
    Parameters
    ----------
    x1 (float): Ponto X1 da funcão no eixo x.
    x2 (float): Ponto X2 da função no eixo y.

    Returns
    -------
    f_gradX (float): Após o calculo, irá me retornar o gradiente de 'Z'
    """
    return 2*(x1-1) + 4*x2                              #Derivada parcial em relação a x1 = 2*(x1-1) e em x2 = 4*x2

for i in range(n): 
    
    grad[i] = (2*(i-1) + 4*i)/((2*(i-1))**2 + (4*i)**2)
    print(f' o vetor dk de posição:{[i]} na função objetivo tem seu valor de: {grad[i]:.5f}\n')
    
def z_funcao():
    return np.array(f_x(x1,x2))

dados['z'] = np.array(f_x(x1,x2))
z_final = dados['z']

grafico = plt.axes(projection='3d')
grafico.plot( x1, x2, z_final)                          #plotagem da curvas de nível da funcão custo(objetivo)
grafico.scatter([1],[0], color='black', marker='x')     #marcação do ponto ótimo [1,0]
grafico.set(title='Curvas de Nível Gradiente', xlabel='eixo x1', ylabel='eixo x2', zlabel='f(x1,x2)')
plt.show()