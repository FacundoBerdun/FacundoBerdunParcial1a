
def aplicarAumento(precio):
    aumento = precio * 5 /100
    precio_total = precio + aumento
    return precio_total

precio = int(input("ingrese un precio: "))
precio_total = aplicarAumento(precio)
print(precio_total)