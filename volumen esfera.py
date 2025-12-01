#*****volumen esfera*****
#*****zona funcional*****

def capturar_radio():
    radio = int(input("digite el valor del radio: ")) 
    return radio

def hacer_volumen(radio):
    volumen = (4/3 * 3.1416 * radio**3)
    return volumen

def hacer_mesaje(volumen):
    mensaje = "el volumen de una esfera es: " + str(volumen)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)

#****zona codigo principal*****

radio = capturar_radio()
volumen = hacer_volumen(radio)
mensaje = hacer_mesaje(volumen)
imprimir = imprimir_mensaje(mensaje)