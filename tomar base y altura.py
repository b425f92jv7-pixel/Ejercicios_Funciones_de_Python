#******tomar base y altura/area triangulo ******
#*******zona de funciones ********
def capturar_base ():
    base = int(input("digite el valor de la base: "))
    return base

def capturar_altura ():
    altura = int(input("digite el valor de la altura: "))
    return altura

def hacer_area (base, altura):
    area = (base * altura/ 2 )
    return area

def hacer_mensaje(area):
    mensaje = "la area del triangulo es: " + str(area)
    return mensaje 

def imprimir_mensaje(mensaje):
    print (mensaje)
    
    
#***** zona codigo principal*******

dato_base = capturar_base()
dato_altura = capturar_altura()
realizar_area = hacer_area(dato_base, dato_altura)
mensaje = hacer_mensaje(realizar_area)
imprimir = imprimir_mensaje(mensaje)

