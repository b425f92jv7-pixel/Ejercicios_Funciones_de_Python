#*****numero multiplo*****
#*****zona funcional*****

def capturar_n1():
    n1 = int(input("Digite el primer número entero: "))
    return n1

def capturar_n2():
    n2 = int(input("Digite el segundo número entero: "))
    return n2

def hacer_multiplo(numero1, numero2):
    if numero1 % numero2 == 0:
        return True
    else:
        return False
    
def hacer_mensaje(n1, n2, multiplo):
    if multiplo:
        mensaje = str(n1) + " es múltiplo de " + str(n2)
    else:
        mensaje = str(n1) + " no es múltiplo de " + str(n2)
    return mensaje    

def imprimir_mensaje(mensaje):
    print(mensaje)
    
    
#****zona codigo principal*****
n1 = capturar_n1()
n2 = capturar_n2()
multiplo = hacer_multiplo(n1, n2)
mensaje = hacer_mensaje(n1, n2, multiplo)
imprimir_mensaje(mensaje)
    