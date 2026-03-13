def inicio():
    print("===========================") #Linea que mejora la experiencia del usuario de forma visual
    print(">> BIENVENIDO AL SISTEMA <<") # Mensaje de bienvenida al usuario
    print("===========================") 
#Funcion encargada de darle la bienvenida al usuario

def productos(): #Funcion encargada de registrar las caracteristicas del producto

    producto = input("\n>> Ingrese el nombre del producto: ").capitalize() #Le pide al usuario que ingrese el nombre del producto
    
    # Evular los posibles errores que se pueden presentar
    try:
        price = float(input(">> Ingrese el precio del producto: $"))
        quantity = int(input(">> Ingrese la cantidad vendida del producto: "))
    except ValueError:
        print("-"*40)
        print("Datos invalidos, vuelva intentarlo.")
        print("-"*40)
        return productos() # Sirve para retornar la funcion dado caso se presente un error al ingresar un dato
    costo_total= price*quantity # Calcula el costo total del precio por la cantidad del producto
    
    print("-"*60) #Linea que mejora la experiencia del usuario de forma visual
    print (f"Producto = {producto} | Precio = ${price} | Cantidad = {quantity} | Total = ${costo_total}")
    # Imprime el resumen de los datos agregados tales como: nombre, precio, cantidad y costo total del producto
    print("-"*60)
    
def run(): #Funcion encargada de ejecutar todas las funciones anteriores

    inicio() #Llama dicha funcion para ejecutarse
    productos() #Llama dicha funcion para ejecutarse

run() #Ejecuta la funcion nombrada para iniciar el programa.
