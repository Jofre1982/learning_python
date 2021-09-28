from datetime import datetime
cripto = input("Indique el nombre de la moneda: ")
cant = float(input("Indique la cantidad de la moneda que posee: "))
cotizacion=float(input("Cotización por US$ del día de la Criptomoneda: "))
hoy=datetime.now()
print("La fecha completa y hora en la que obtuvo la información fue:"+hoy.strftime("%A, %d de %B de %Y a las %I:%M:%S%p"))