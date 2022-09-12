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

Created on Sun Sep  4 00:01:55 2022

@author: Cristian
'''

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

dados = pd.DataFrame()
dados['x1'] = np.linspace(10,-10,21)
dados['x2'] = np.linspace(10,-10,21)
x1 = dados['x1']
x2 = dados['x2']
repeticao = 0
norma_grad = 0
pre = pow(10,-2)

def f_x(x1, x2):
    return (x1-1)**2 + 2*x2**2

xx1,xx2 = np.meshgrid(x1,x2)
zlinha = f_x(xx1, xx2)

def f_gradX(x1, x2):
    return pd.Series([[2*(x1-1)],[4*x2]])

for i in dados['x1']:
    for j in dados['x2']:
        if norma_grad >= pre and norma_grad <= pre or repeticao >= 100 :
            break
        funcao_x1x2 = (i-1)**2 + 2*j**2
        print(f' o vetor dk de posição: x1 ={[i]} e x2={[j]} na função objetivo tem seu valor de: {funcao_x1x2:.2f}\n')
        norma_grad = pow(2*(i-1),2) + pow(4*j,2)
        
        repeticao = repeticao + 1

grafico = plt.axes(projection='3d')
grafico.contour( xx1, xx2, zlinha)
grafico.scatter([1],[0], color='black', marker='x')
grafico.set(title='Curvas de Nível Gradiente', xlabel='eixo x1', ylabel='eixo x2', zlabel='f(x1,x2)')
plt.show()
