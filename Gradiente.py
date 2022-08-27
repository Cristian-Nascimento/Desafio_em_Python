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

import numpy as np
import matplotlib.pyplot as plt
import pandas as plt
from matplotlib import cm

# def f_x(x,y):
#     return (x - 1)**2 + 2*y**2

# def gradiente(x,y):
#     return np.array([2*(x - 1), 4*y])

x = np.linspace(-10.0,10.0,100)
y = np.linspace(-10.0,10.0,100)

xlinha,ylinha=np.meshgrid(x,y)

zlinha = ((xlinha-1)**2 + (2 * ylinha)**2)

plt.contour(xlinha,ylinha,zlinha)
plt.show()

# ax = plt.axes(projection='3d')
# ax.view_init(50, 30)
# ax.plot_surface(x, y, z, cmap=cm.coolwarm )
# ax.set_xlabel('eixo x')
# ax.set_ylabel('eixo y')
# ax.set_zlabel('eixo z')

