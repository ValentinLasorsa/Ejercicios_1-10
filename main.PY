import os
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