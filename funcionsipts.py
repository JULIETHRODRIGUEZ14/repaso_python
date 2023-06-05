personalizada = 2950

def calcular_saldo(recarga):
    if recarga > personalizada:
        saldo = recarga - personalizada
        print("El saldo de la tarjeta es:", saldo)
    elif recarga < personalizada and recarga > 0:
        saldo = recarga - personalizada
        print("Su saldo debe ser:", saldo)
    else:
        print("Su saldo es insuficiente")

def realizar_transbordo():
    print("Transferencia realizada")

tarjeta = int(input("Ingrese si tu tarjeta SIPT: 1. Personalizada 2. Normal\n"))

if tarjeta == 1:
    transbordo = int(input("Ingrese 1 para primer viaje o 2 para transbordo\n"))
    if transbordo == 1:
        recarga = int(input("Ingrese la recarga de la tarjeta: "))
        if recarga > 2950:
            calcular_saldo(recarga)
        else:
            print("Su saldo es insuficiente")
    elif transbordo == 2:
        realizar_transbordo()
    else:
        print("Opción inválida")
elif tarjeta == 2:
    recarga = int(input("Ingrese la recarga de la tarjeta: "))
    calcular_saldo(recarga)
else:
    print("Tarjeta inválida")
