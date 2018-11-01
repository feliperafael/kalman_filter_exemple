#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 00:25:33 2018

@author: felipe
"""

import numpy as np
import matplotlib.pyplot as plt

# P = sigma_modelo
# R = sigma_sensor
sigma_sensor = 4.0
var_sensor = sigma_sensor*sigma_sensor

sigma_sistema = np.sqrt(0.0529)
var_sistema = 0.0529

tam = 10 # amostras

def sistema(i):
    return  1.4*i + np.random.normal(0,np.sqrt(var_sistema))

def sensor(i):
    s = [1.21, -4.77, 0.98, 5.25, 4.53, 5.39, 11.57, 8.34, 18.31, 24.16]
    return s[i]

x_k = np.zeros(tam)

prior = [0, sigma_sensor**2]# [mean,var] 

for i in range(tam):
    
    x, P = prior        # media mi e variancia a priori
    z, R = [sensor(i), var_sensor] # media e variancia da medicao do sensor (medicao)
    
    y = z - x        # inovacao
    K = P / (P + R)  # ganha de Kalman

    x = x + K*y      # posteriori
    P = (1 - K) * P  # variancia posteriori
    post = [x, P]
    
    
    dx = i # mean
    Q =  var_sistema # variancia do sistema
    x = x + dx
    P = P + Q    
    x_k[i] = x # resultado do kalman
    prior = post #atualizo para o proximo passo
   

############# plot #########################
    
t = np.linspace(1,tam,tam)
y_sistema = np.zeros(tam)
y_sensor = np.zeros(tam)
for i in range(tam):
    y_sistema[i] = sistema(i)
    y_sensor[i] = sensor(i)
#plt.plot(t,y_sistema, label='sistema')
plt.plot(t,y_sensor, label='sensor y')
plt.plot(t,x_k, label='kalman')
plt.title('aplicação do filtro de kalman sobre um sensor y'.decode('utf-8'))
plt.ylabel(r'$y_{k}$')
plt.xlabel('tempo k')
plt.legend()
plt.savefig('questao_4.png')
plt.show() # mostra
