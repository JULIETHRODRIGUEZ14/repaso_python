import random

def lanzar_moneda():
    # Lanza la moneda y devuelve el resultado ("cara" o "sello")
    resultado = random.choice(["cara", "sello"])
    return resultado

def jugar():
    # Solicita el nombre del jugador
    nombre = input("Ingrese su nombre: ")
    
    # Lanza la moneda aleatoriamente
    resultado_moneda = lanzar_moneda()
    
    # Elige cara o sello
    eleccion = input("Hola " + nombre + "! Elige 'cara' o 'sello': ")
    
    # Solicita la apuesta
    apuesta = float(input("Ingresa la cantidad que deseas apostar: "))
    
    # Verifica el resultado y muestra el mensaje correspondiente
    if eleccion == resultado_moneda:
        print("¡Ganaste!")
        apuesta *= 2
        print("Has ganado %.2f. Ahora tienes %.2f." % (apuesta, apuesta))
    else:
        print("Perdiste.")
        apuesta = 0
        print("Has perdido tu apuesta. Ahora tienes %.2f." % apuesta)

# Inicia el juego
jugar()
