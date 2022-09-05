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

from tkinter.ttk import Style
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd



# dados = pd.DataFrame()
# dados['x'] = np.linspace(10,0,100)   #Criação do vertor de x1
# dados['y'] = np.linspace(10,0,100)   #Criação do vertor de x2
# x1 = dados['x']
# x2 = dados['y']

# print(type(x1), type(x2))

# def f_x(x1, x2):
#     """
#     Parametro
#     ----------
#     x1 (float): Ponto X1 da funcão no eixo x.
#     x2 (float): Ponto X2 da função no eixo y.

#     Retorno
#     ----------
#     f_x (float): Após o calculo, irá me retornar o vetor 'Z'
#     função que retorna o valor de f(x1,x2) para um deterninado x1,x2
#     """
#     return (x1-1)**2 + 2*x2**2

# def linha_x1(x1):
#     """
#     Parametro
#     ----------
#     x1 (float): Ponto X1 da funcão custo no eixo x1.
    
#     Retorno
#     ----------
#         Função que retorna o valor de custo de f(x1) para um deterninado x1
#     """
#     return 2*(x1 - 1)

# def linha_x2(x2):
#     """
#     Parametro
#     ----------
#     x2 (float): Ponto X2 da funcão custo no eixo x2.

#     Retorno
#     ----------
#         Função que retorna o valor de custo de f(x2) para um deterninado x2

#     """
#     return 4*x2

# def z_funcao():
#     """
#     Parametro
#     ----------
#     Z (float): Ponto Z da funcão custo no eixo z.

#     Retorno
#     ----------
#         Função que retorna um array para o Z do valor de custo de f(x1, x2) para um deterninado x1, x2

#     """
#     return np.array(f_x(x1,x2))

# dados['z'] = np.array(f_x(x1,x2))
# z_final = dados['z']   #z_final está recebendo o array de Z

# print(f' A funcao tem o seu valor de:\n{f_x(x1, x2)}\n')
# print(f' A funcao custo em X1 tem o seu valor de:\n{linha_x1(x1)} \ne em X2: \n{linha_x2(x2)}')

# grafico = plt.axes(projection='3d')
# grafico.plot(x1,x2,f_x(x1,x2))    #plotagem da curvas de nível da funcão custo(objetivo)
# grafico.scatter([1],[0], color='black', marker='x')    #marcação do ponto ótimo [1,0]

# grafico.set(title='Curvas de Nível Gradiente', xlabel='eixo x1', ylabel='eixo x2', zlabel='eixo f(x1,x2)')
# plt.show()

a = []
b = []
k = 10

while k >= 0:
    a.append(int(k)) #Criação do vertor de x1
    k += -1

grad = []
dk = []

def inf(a):
    return (2*(a[i]-1) + 4*a[i])

for i in range(len(a)):
    grad.append(((2*(a[i]-1))**2 + (4*a[i])**2)) # parte de baixo



print(inf(a))
# print(type(a),type(grad))
# grafico = plt.axes(projection='3d')
# grafico.plot(a,grad)    #plotagem da curvas de nível da funcão custo(objetivo)
# grafico.scatter([1],[0], color='black', marker='x')    #marcação do ponto ótimo [1,0]

# grafico.set(title='Curvas de Nível Gradiente', xlabel='eixo x1', ylabel='eixo x2', zlabel='eixo f(x1,x2)')
# plt.show()