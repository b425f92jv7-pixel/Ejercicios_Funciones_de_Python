# Escribe un programa que pida dos números enteros y muestre el cociente de la división entera.
#*****division entera*****
#*****zona funcional*****

def capturar_numero1():
    numero1 = int(input("Digite el primer número entero: "))
    return numero1 

def capturar_numero2():
    numero2 = int(input("Digite el segundo número entero: "))
    return numero2

def hacer_division(numero1, numero2):
    division_entera = numero1 / numero2
    return division_entera

def hacer_mensaje( division_entera):
    mensaje = "El cociente de la división entera es: " + str(division_entera)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)  
    
#****zona codigo principal*****
numero1 = capturar_numero1()
numero2 = capturar_numero2()
division_entera = hacer_division(numero1, numero2)    
mensaje = hacer_mensaje(division_entera)
imprimir = imprimir_mensaje(mensaje)    