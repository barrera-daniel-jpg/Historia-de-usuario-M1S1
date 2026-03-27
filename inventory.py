def start():
    print("===========================")  # Line that improves the user experience visually
    print(">> WELCOME TO THE SYSTEM <<")  # Welcome message for the user
    print("===========================")
# Function responsible for welcoming the user


def products():  # Function responsible for registering product details

    product = input("\n>> Enter the product name: ").capitalize()  # Asks the user for the product name
    
    # Evaluate possible input errors
    try:
        price = float(input(">> Enter the product price: $"))
        quantity = int(input(">> Enter the quantity sold: "))
    except ValueError:
        print("-" * 40)
        print("Invalid data, please try again.")
        print("-" * 40)
        return products()  # Recursively calls the function if an error occurs

    total_cost = price * quantity  # Calculates total cost

    print("-" * 60)  # Visual separator
    print(f"Product = {product} | Price = ${price} | Quantity = {quantity} | Total = ${total_cost}")
    # Prints summary of entered data
    print("-" * 60)


def run():  # Function responsible for executing all previous functions

    start()     # Calls welcome function
    products()  # Calls product function
