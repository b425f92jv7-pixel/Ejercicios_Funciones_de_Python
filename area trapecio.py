#*********area de trapecio*********
#*********zona de funciones************

def capturar_base_mayor():
    base1 = float(input("Digite la longitud de la base mayor: "))
    return base1

def capturar_base_menor():
    base2 = float(input("Digite la longitud de la base menor: "))
    return base2

def capturar_altura():
    h = float(input("Digite la altura del trapecio: "))
    return h

def hacer_area(base1, base2, h):
    area = ((base1 + base2) / 2) * h
    return area

def hacer_mensaje(area):
    mensaje = ("el area es: " + str(area))
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)
    
#****zona codigo principal*****

base_mayor = capturar_base_mayor()
base_menor = capturar_base_menor()
altura = capturar_altura()
area = hacer_area(base_mayor, base_menor, altura)
mensaje = hacer_mensaje(area)
imprimir = imprimir_mensaje(mensaje)