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
        

# Calcular estadisticas
saldos_list = list(saldos.values())
saldo_mas_alto = max(saldos_list)
saldo_mas_bajo = min(saldos_list)
saldo_promedio = statistics.mean(saldos_list)
    
