#**********un numero es par o impar**********
#********zona funcional*************

def capturar_numero():
    numero = int(input("digite un numero entero: "))
    return numero

def determinar(numero):
    if numero % 2 == 0:
        resultado = "par"
    else:
        resultado = "impar"
    return resultado

def hacer_mensaje(resultado):
    mensaje = "el numero es: " + resultado
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)
    
#******** zona codigo principal ************
numero = capturar_numero()
resultado = determinar(numero)
mensaje = hacer_mensaje(resultado)
imprimir = imprimir_mensaje(mensaje)