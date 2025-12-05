#******cuadrado de un numero******
#*****zona funcional********
def capturar_n():
    numero= int(input("ingrese el numero: "))
    return numero


def sumar_ns (numero):
    mult = (numero * numero)
    return mult

def hacer_mensaje(mult):
    mensaje = "el cuadrado del numero es: " + str(mult)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)  
    
  
#****codigo principal*****    
n= capturar_n()

mult = sumar_ns(n)
mensaje = hacer_mensaje(mult)

imprimir = imprimir_mensaje(mensaje)
