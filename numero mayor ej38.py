# Desarrolla un programa que pida dos números y muestre el mayor de los dos utilizando operadores aritméticos. 
#*****numero mayor*****
#*****zona funcional*****

def capturar_numero1():
    numero1 = int(input("Digite el primer número entero: "))
    return numero1

def capturar_numero2():
    numero2 = int(input("Digite el segundo número entero: "))
    return numero2

def hacer_mayor(numero1, numero2):
    if numero1 > numero2:
        mayor = numero1
    else:
        mayor = numero2
    return mayor

def hacer_mensaje(mayor):
    mensaje = "El número mayor es: " + str(mayor)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)
    
    
#****zona codigo principal*****
numero1 = capturar_numero1()    
numero2 = capturar_numero2()
mayor = hacer_mayor(numero1, numero2)
mensaje = hacer_mensaje(mayor)
imprimir_mensaje(mensaje)