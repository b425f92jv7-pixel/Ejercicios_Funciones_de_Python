#*****solicite 2 y reste****
#****zona funcional*****

def capturar_n1():
    numero1= int(input("ingrese el primer numero: "))
    return numero1

def capturar_n2():
    numero2= int(input("ingrese el segundo numero: "))
    return numero2

def sumar_ns (numero1, numero2):
    resta = (numero1 - numero2)
    return resta

def hacer_mensaje(resta):
    mensaje = "la resta de los numeros es: " + str(resta)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)  
    
  
#****codigo principal*****    
n1 = capturar_n1()
n2 = capturar_n2()
resta = sumar_ns(n1, n2)
mensaje = hacer_mensaje(resta)

imprimir = imprimir_mensaje(mensaje)
