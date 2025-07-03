def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Agregar producto al carrito")
    print("2. Mostrar contenido del carrito")
    print("3. Calcular total a pagar")
    print("4. Salir")

def agregar_producto(carrito):
    nombre = input("Ingrese el nombre del producto: ").strip()
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio < 0:
            print("El precio no puede ser negativo.")
            return
        carrito[nombre] = precio
        print(f"Producto '{nombre}' agregado con precio {precio:.2f}")
    except ValueError:
        print("Precio inválido. Intente de nuevo.")

def mostrar_carrito(carrito):
    if not carrito:
        print("El carrito está vacío.")
        return
    print("\n--- Contenido del carrito ---")
    for producto, precio in carrito.items():
        print(f"{producto}: ${precio:.2f}")

def calcular_total(carrito):
    total = sum(carrito.values())
    print(f"\nTotal a pagar: ${total:.2f}")

def main():
    carrito = {}
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if opcion == "1":
            agregar_producto(carrito)
        elif opcion == "2":
            mostrar_carrito(carrito)
        elif opcion == "3":
            calcular_total(carrito)
        elif opcion == "4":
            print("Gracias por usar el carrito de compras. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()