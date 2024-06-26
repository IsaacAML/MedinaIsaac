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

# Mostrar los saldos
for cliente, (categoria, saldo) in clasificacion.items():
    print(f'{cliente}: ${saldo:.3f} - {categoria}')
    
# Mostrar estadisticas
print('\n Estadisticas:')
print(f'Saldo mas alto: ${saldo_mas_alto:.3f}')
print(f'Saldo mas bajo: ${saldo_mas_bajo:.3f}')
print(f'Saldo promedio: ${saldo_promedio:.3f}')    


# Crear archivo csv
with open('reporte_saldos.csv', mode='w', newline='') as archivo_csv:
    writer = csv.writer(archivo_csv)
    writer.writerow(['Cliente', - 'Saldo', - 'Clasificacion:'])
    writer.writerows([])
    for cliente, (categoria, saldo) in clasificacion.items():
        writer.writerow([cliente, saldo, categoria])
        
    writer.writerow([])
    writer.writerow(['Estadisticas:'])
    
    writer.writerow(['Saldo mas alto', saldo_mas_alto])
    writer.writerow(['Saldo mas bajo', saldo_mas_bajo])
    writer.writerow(['Saldo promedio', saldo_promedio])
print('\n Datos guardados en un archivo csv')



# Opcion para salir de banco santander
print('\n Preciona cualquier tecla para salir')
input()
print('Gracias por usar Banco Santander, vuelva pronto...')