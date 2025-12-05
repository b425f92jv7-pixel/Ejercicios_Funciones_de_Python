#******algoritmo division******
#*****zona funcional********
def capturar_n1():
    n1= int(input("ingrese el primer numero: "))
    return n1

def capturar_n2():
    n2= int(input("ingrese el segundo numero: "))
    return n2

def div_ns (n1, n2):
    div = (n1 / n2)
    return div

def hacer_mensaje(div):
    mensaje = "la division de los numeros es: " + str(div)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)  
    
  
#****codigo principal*****    
n1 = capturar_n1()
n2 = capturar_n2()
div = div_ns(n1, n2)
mensaje = hacer_mensaje(div)

imprimir = imprimir_mensaje(mensaje)
