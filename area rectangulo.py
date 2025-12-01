#******area rectangulo ******
#*******zona de funciones ********
def capturar_longitud ():
    longitud = int(input("digite el valor de la base: "))
    return longitud

def capturar_ancho ():
    ancho = int(input("digite el valor de la altura: "))
    return ancho

def hacer_area (longitud, ancho ):
    area = longitud * ancho
    return area

def hacer_mensaje(area):
    mensaje = "la area del rectangulo es: " + str(area)
    return mensaje 

def imprimir_mensaje(mensaje):
    print (mensaje)
    
   #*****codigo principal******* 
longitud = capturar_longitud()
ancho = capturar_ancho()
area = hacer_area(longitud, ancho)
mensaje = hacer_mensaje(area)
imprimir = imprimir_mensaje(mensaje)