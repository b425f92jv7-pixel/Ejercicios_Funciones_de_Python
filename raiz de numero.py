#******raiz de un numero******
#*****zona funcional********
def capturar_n():
    numero= int(input("ingrese el numero: "))
    return numero


def hacer_raiz (numero):
    raiz = (numero ** 0.5 )
    return raiz

def hacer_mensaje(raiz):
    mensaje = "la raiz del numero es: " + str(raiz)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)  
    
  
#****codigo principal*****    
n= capturar_n()
mult = hacer_raiz(n)
mensaje = hacer_mensaje(mult)
imprimir = imprimir_mensaje(mensaje)