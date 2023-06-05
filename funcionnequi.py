import random

def ingresar():
    print("Estás ingresando a la plataforma Nequi Colombia")
    print("No dudamos que seas tú... ¡pero es mejor confirmar! ;)")
    celular = input("Ingresa tu número celular: ")
    password = input("Escribe tu clave: ")
    
    if len(celular) == 10 and len(password) == 4:
        print("¡Has ingresado correctamente!")
        return True
    else:
        print("Los datos ingresados son incorrectos.")
        return False

def sacar(valor):
    puntos = int(input("Opciones para sacar:\n1. Punto físico\n2. Cajero\n"))

    if puntos == 1 and valor > 2000:
        codigo = random.randint(000000, 999999)
        valorR = int(input("Ingresa cuánto deseas retirar: "))
        valor = valor - valorR

        print("Para sacar, confirma este código a la persona encargada del punto físico:", codigo)
        print("Acabas de retirar", valorR, "el saldo de la cuenta es", valor)
    elif puntos == 2 and valor > 2000:
        codigo = random.randint(000000, 999999)
        valorR = int(input("Ingresa cuánto deseas retirar: "))
        valor = valor - valorR
        print("Para sacar, confirma el código en el cajero:", codigo)

        print("¡RETIRO EXITOSO!")
        print("El retiro es de", valorR, "el saldo de la cuenta es", valor)
    elif (puntos == 1 or puntos == 2) and valor < 2000:
        print("No te alcanza")
    else:
        print("Transacción inválida")

def enviar(valor):
    envio = int(input("Ingresa el número al que deseas enviar el dinero: "))
    valorE = int(input("Ingresa el valor que deseas enviar: "))

    if valorE < valor:
        valor = valor - valorE
        print("Acabas de enviar", valorE, "el saldo en tu cuenta es", valor)
    elif valorE > valor:
        print("Proceso inválido, saldo insuficiente")

def recargar(valor):
    recarga = int(input("Ingrese el valor que va a recargar en su cuenta: "))
    print("Vas a recargar", recarga)
    seguro = int(input("¿Estás seguro? Ingresa el número correspondiente:\n1. SÍ\n2. NO\n"))

    if seguro == 1:
        valor = valor + recarga
        print("¡RECARGA EXITOSA!")
        print("Has recargado", recarga, "el valor disponible en la cuenta es de", valor)
    elif seguro == 2:
        print("Transacción cancelada")
    else:
        print("Transacción inválida")

def nequi():
    continua = 1
    valor = 4500
    
    if not ingresar():
        return

    while continua == 1:
        opcion = int(input("Ingresa la funcionalidad que deseas realizar:\n1. Sacar\n2. Enviar\n3. Recargar\n4. Salir\n"))

        if opcion == 1:
            sacar(valor)
        elif opcion == 2:
            enviar(valor)
        elif opcion == 3:
            recargar(valor)
        elif opcion == 4:
            print("V")
