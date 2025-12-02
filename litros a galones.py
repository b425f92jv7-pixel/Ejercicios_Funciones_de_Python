#*****litros a gslones*****
#*****zona funcional*****

def capturar_litros():
    litros = int(input("digite el valor de los litros que desea convertir: ")) 
    return litros

def hacer_convercion(litros):
    conversion= (litros * 0.264)
    return conversion

def hacer_mesaje(litros, conversion ):
    mensaje = str(litros) + " litros convertidos a galones es: " + str(conversion)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)

#****zona codigo principal*****
litros = capturar_litros()
conversion = hacer_convercion(litros)
mensaje = hacer_mesaje(litros, conversion)
imprimir = imprimir_mensaje(mensaje)
