#*****horas a minutos*****
#*****zona funcional*****

def capturar_hora():
    hora = float(input("digite la hora: ")) 
    return hora

def hacer_convercion(hora):
    conversion= (hora*60)
    return conversion

def hacer_mesaje(hora, conversion ):
    mensaje = str(hora) + " convertido a minutos es: " + str(conversion)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)

#****zona codigo principal*****
hora = capturar_hora()
conversion = hacer_convercion(hora)
mensaje = hacer_mesaje(hora, conversion)
imprimir = imprimir_mensaje(mensaje)
