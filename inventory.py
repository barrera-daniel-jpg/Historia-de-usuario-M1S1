def inicio():
    print("===========================") #Linea que mejora la experiencia del sistema
    print(">> BIENVENIDO AL SISTEMA <<") # Mensaje de bienvenida al usuario
    print("===========================") 
#Funcion encargada de darle la bienvenida al usuario

def productos():
    producto = input("\n>> Ingrese el nombre del producto: ").capitalize()
    try:
        price = float(input(">> Ingrese el precio del producto: $"))
        quantity = int(input(">> Ingrese la cantidad vendida del producto: "))
    except ValueError:
        print("-"*40)
        print("Datos invalidos, vuelva intentarlo.")
        print("-"*40)
        return productos()
    costo_total= price*quantity
    
    print("-"*60)
    print (f"Producto = {producto} | Precio = ${price} | Cantidad = {quantity} | Total = ${costo_total}")
    print("-"*60)
    
#Funcion encargada de registrar las caracteristicas del producto
def run():
    inicio()
    productos()
#Funcion encargada de ejecutar todas las funciones anteriores

run()
#Ejecuta la funcion nombrada para iniciar el programa