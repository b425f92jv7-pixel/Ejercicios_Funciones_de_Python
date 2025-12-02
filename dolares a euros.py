#*********dolares a euros*********
#*********zona de funciones************

def tomar_dolares():
    dolares = float(input("Digite la cantidad en dólares (USD): "))
    return dolares

def tomar_tasa():
    tasa = float(input("Digite la tasa de cambio: "))
    return tasa

def convertir_e(dolares, tasa):
    euros = (dolares * tasa )
    return euros

def hacer_mensaje ( euros):
    mensaje = ("la conversion a euros da: "  ) + str (euros)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)

#****zona codigo principal*****
dolares = tomar_dolares()
tasa = tomar_tasa()
euros = convertir_e(dolares, tasa)
mensaje = hacer_mensaje( euros)
imprimir = imprimir_mensaje(mensaje)