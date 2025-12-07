#****5% de intereses ****** 
#*****zona funcional********

def capturar_dinero():
    dinero = float(input("Digite la cantidad de dinero en la cuenta: "))
    return dinero   

def calcular_interes(dinero):
    interes = dinero * 0.05
    return interes

def hacer_mensaje(interes):
    mensaje = "el interes de la cuenta es : " + str(interes)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)
    
    
# Zona de código principal
dinero = capturar_dinero()  
interes = calcular_interes(dinero)
mensaje = hacer_mensaje(interes)    
imprimir_mensaje(mensaje)    