moneda1 = "BTC"
moneda2 = "LTC"
moneda3 = "BCC"

moneda = input("Ingrese la moneda a comprar: ")
if moneda == moneda1 or moneda==moneda2 or moneda==moneda3:
    cantidad = float(input("Ingrese la cantidad de "+moneda+" a comprar:"))
    if moneda == "BTC" and cantidad>0.01:
        print("Compra Exitosa")
    elif moneda == "LTC" and cantidad> 1.0:
        print("Compra Exitosa")
    elif moneda == "BCC" and cantidad > 0.1:
        print("Compra Exitosa")
    else:
        print("Comprar fallida, cantidad menor al mínimo")
else:
    print("Debe ingresar una de las siguientes monedas: BTC, LTC, BCC")