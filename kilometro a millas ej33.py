#*****kilometros a millas*****
#*****zona funcional*****

def capturar_kilometros():
    kilometros = int(input("digite el valor de los kilometros que desea convertir: ")) 
    return kilometros

def hacer_convercion(kilometros):
    conversion= (kilometros*0.621)
    return conversion

def hacer_mesaje(kilometros, conversion ):
    mensaje = str(kilometros) + " km convertido a millas es: " + str(conversion)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)

#****zona codigo principal*****
kilometros = capturar_kilometros()
conversion = hacer_convercion(kilometros)
mensaje = hacer_mesaje(kilometros, conversion)
imprimir = imprimir_mensaje(mensaje)
