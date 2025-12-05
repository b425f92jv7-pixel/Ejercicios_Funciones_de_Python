#*****solicite 2 y de su producto****
#****zona funcional*****

def capturar_n1():
    numero1= int(input("ingrese el primer numero: "))
    return numero1

def capturar_n2():
    numero2= int(input("ingrese el segundo numero: "))
    return numero2

def mult_ns (numero1, numero2):
    mult = (numero1 * numero2)
    return mult

def hacer_mensaje(mult):
    mensaje = "el producto de los numeros es: " + str(mult)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)  
    
  
#****codigo principal*****    
n1 = capturar_n1()
n2 = capturar_n2()
mult = mult_ns(n1, n2)
mensaje = hacer_mensaje(mult)

imprimir = imprimir_mensaje(mensaje)
