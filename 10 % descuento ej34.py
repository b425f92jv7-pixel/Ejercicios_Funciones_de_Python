#*****10% de descuento****
#*****zona funcional********
def capturar_precio():
    precio = float(input("Digite el precio del artículo: "))
    return precio

def calcular_descuento(precio):
    descuento = precio * 0.10
    return descuento

def calcular_precio_final(precio, descuento):
    precio_final = precio - descuento
    return precio_final

def hacer_mensaje(precio_final):
    mensaje = "El precio final con descuento es: " + str(precio_final)
    return mensaje      

def imprimir_mensaje(mensaje):
    print(mensaje)
    

# Zona de código principal
precio = capturar_precio()      
descuento = calcular_descuento(precio)
precio_final = calcular_precio_final(precio, descuento)
mensaje = hacer_mensaje(precio_final)    
imprimir_mensaje(mensaje)    