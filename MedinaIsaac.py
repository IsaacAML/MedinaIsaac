# Importar librerias

import random, statistics, csv


# Crear lista de clientes
 
clientes = [f'cliente {i+1}' for i in range(10)]


# Asignar saldos aleatorios
saldos = {cliente: round(random.uniform(0,900), 3) for cliente in clientes}


# Clasificacion de saldos
clasificacion = {}
for cliente, saldo in saldos.items():
    if saldo < 300:
        clasificacion[cliente] = ('bajo', saldo)
    elif 300 <= saldo < 600:
        clasificacion[cliente] = ('medio', saldo)
    else:
        clasificacion[cliente] = ('alto', saldo)    
