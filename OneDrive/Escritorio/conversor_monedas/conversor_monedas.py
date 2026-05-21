# Conversor de euros y dólares

euro_usd = 1.1
dolar_euro = 0.91

moneda_origen = input("¿Qué moneda quieres convertir? (euros o dólares): ").lower().strip()

if moneda_origen not in ["euro", "euros", "dolar", "dolares", "dólar", "dólares"]:
    print("Error: moneda no válida")

else:
    try:
        cantidad = float(input("¿Cuánto quieres convertir?: "))

        if moneda_origen in ["euro", "euros"]:
            cantidad_convertida = cantidad * euro_usd
            print(cantidad, "euros son", round(cantidad_convertida, 2), "dólares")

        else:
            cantidad_convertida = cantidad * dolar_euro
            print(cantidad, "dólares son", round(cantidad_convertida, 2), "euros")

    except ValueError:
        print("Error: debes introducir un número válido")