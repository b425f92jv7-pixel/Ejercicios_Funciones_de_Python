#**********area de un circulo*********
#**********zona de funciones**********

def tomar_radio():
    radio = int(input("Digite el valor del radio: "))
    return radio
    
def hacer_area (radio):
    area = (3.1416 * radio ** 2)
    return area
    
def hacer_mensaje (area):
    mensaje = "El área del círculo es: " + str(area)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)
    
#****zona codigo principal*****
radio = tomar_radio()
area = hacer_area(radio)
mensaje = hacer_mensaje(area)
imprimir = imprimir_mensaje(mensaje)