print("Calcular el IVA de un producto")
precioBase = float(input("Ingrese el precio base del producto: "))
valorIva = precioBase * 0.19
precioConIva = precioBase + valorIva
print(f"El valor del IVA es: {valorIva}")
print(f"El valor del producto con IVA es: {precioConIva}")