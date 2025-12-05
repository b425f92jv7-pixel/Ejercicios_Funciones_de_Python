#*****radio de un circulo y hacer la circunferencia*******
#******** zona funcional*************

def tomar_radio():
    radio = float(input("digite el valor del radio del circulo: "))
    return radio

def hacer_circunferencia(radio):
    circunferencia = 2 * 3.1416 * radio
    return circunferencia

def hacer_mensaje(circunferencia):
    mensaje = "la circunferencia del circulo es: " + str(circunferencia)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)
    
#******** zona codigo principal ************
radio = tomar_radio()
circunferencia = hacer_circunferencia(radio)
mensaje = hacer_mensaje(circunferencia)
imprimir_mensaje(mensaje)