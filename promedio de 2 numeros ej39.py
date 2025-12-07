
#*****promedio de 2 numeros*****
#*****zona funcional*****

def capturar_numero1():
    numero1 = int(input("Digite el primer número entero: "))
    return numero1

def capturar_numero2():
    numero2 = int(input("Digite el segundo número entero: "))
    return numero2

def hacer_promedio(numero1, numero2):
    promedio = (numero1 + numero2) / 2
    return promedio

def hacer_mensaje(promedio):
    mensaje = "El promedio de los dos números es: " + str(promedio)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)
    
#****zona codigo principal*****
numero1 = capturar_numero1()        
numero2 = capturar_numero2()
promedio = hacer_promedio(numero1, numero2)
mensaje = hacer_mensaje(promedio)
imprimir_mensaje(mensaje)