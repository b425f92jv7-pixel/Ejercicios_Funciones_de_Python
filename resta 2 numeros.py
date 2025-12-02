#*****solicite 2 y reste****
#****zona funcional*****

def capturar_n1():
    numero1= int(input("ingrese el primer numero: "))
    return numero1

def capturar_n2():
    numero2= int(input("ingrese el segundo numero: "))
    return numero2

def sumar_ns (numero1, numero2):
    suma = (numero1 - numero2)
    return suma

def hacer_mensaje(suma):
    mensaje = "la resta de los numeros es: " + str(suma)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)  
    
  
#****codigo principal*****    
n1 = capturar_n1()
n2 = capturar_n2()
suma = sumar_ns(n1, n2)
mensaje = hacer_mensaje(suma)
imprimir = imprimir_mensaje(mensaje)