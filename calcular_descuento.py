# Definir la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcular el monto del descuento
    descuento = (porcentaje_descuento / 100) * monto_total
    return descuento

# Programa principal
def main():
    # Primera llamada: Solo proporcionamos el monto total (por defecto 10% de descuento)
    monto_total1 = 1000  # Ejemplo de monto total de compra
    descuento1 = calcular_descuento(monto_total1)
    monto_final1 = monto_total1 - descuento1
    print(f"Compra 1: Monto Total = {monto_total1}, Descuento = {descuento1}, Monto Final = {monto_final1}")

    # Segunda llamada: Proporcionamos tanto el monto total como el porcentaje de descuento
    monto_total2 = 500  # Otro ejemplo de monto total de compra
    porcentaje_descuento2 = 15  # Un descuento diferente
    descuento2 = calcular_descuento(monto_total2, porcentaje_descuento2)
    monto_final2 = monto_total2 - descuento2
    print(f"Compra 2: Monto Total = {monto_total2}, Descuento = {descuento2}, Monto Final = {monto_final2}")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()

