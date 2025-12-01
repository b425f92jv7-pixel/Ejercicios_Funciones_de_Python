#*********volumen de un cono*********
#*********zona de funciones************

def capturar_radio():
    radio = int(input("Digite el valor del radio: "))
    return radio

def capturar_altura():
    altura = int(input("Digite el valor de la altura: "))
    return altura

def hacer_volumen(radio, altura):
    volumen = int((1/3) * 3.1416 * radio**2 * altura)
    return volumen

def hacer_mensaje(volumen):
    mensaje = "El volumen del cono es: " + str(volumen)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)
    
    
#****zona codigo principal*****
radio = capturar_radio()
altura = capturar_altura()
volumen = hacer_volumen(radio, altura)
mensaje = hacer_mensaje(volumen)
imprimir = imprimir_mensaje(mensaje)
