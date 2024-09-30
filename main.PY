import os
# EJ 1
"""
print("Ejercicio 1")
def fact(num):
    if num < 0:
        print("El factorial no está definido para números negativos.")
        return
    resultado = 1
    for i in range(2, num + 1):
        resultado *= i
    print(f"El factorial de {num} es {resultado}")   
numero=int(input("Ingrese un número para saber su factorial ")) 
fact(numero)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
"""
# EJ 2
print("Ejercicio 2")
def obtener_mes_en_texto(mes):
    meses = [
        "", "Enero", "Febrero", "Marzo", "Abril",
        "Mayo", "Junio", "Julio", "Agosto",
        "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    if 1 <= mes <= 12:
        print(meses[mes])
    else:
        print("")

mes = int(input("Ingrese un mes "))
obtener_mes_en_texto(mes)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

# EJ 3
print("Ejercicio 3")

input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')