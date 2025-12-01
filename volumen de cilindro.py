#*********volumen de un cilindro*******
#*********zona de funciones************

def definir_radio () :
    radio = int(input("digite el valor del radio: "))
    return radio

def definir_altura ():
    altura = int(input("digite el valor de la altura: ")) 
    return altura

def hacer_volumen (radio,altura) :
    volumen = float(3.1416 * radio**2 * altura )  
    return volumen

def hacer_mensaje (volumen):
    mensaje = "El volumen del cilindro es: " + str(volumen)
    return mensaje


def imprimir_mensaje (mensaje):
    print(mensaje)
    
#****zona codigo principal*****
radio = definir_radio()
altura = definir_altura()
volumen = hacer_volumen(radio, altura)
mensaje = hacer_mensaje(volumen)
imprimir = imprimir_mensaje(mensaje)