#******area rectangulo ******
#*******zona de funciones ********
def tomar_longitud ():
    longitud = int(input("digite el valor de la longitud: "))
    return longitud

def tomar_ancho ():
    ancho = int(input("digite el valor del ancho: "))
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
longitud = tomar_longitud()
ancho = tomar_ancho()
area = hacer_area(longitud, ancho)
mensaje = hacer_mensaje(area)
imprimir = imprimir_mensaje(mensaje)