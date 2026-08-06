# Inventory Management System

inventory = {}

def add_product():
    name = input("Enter product name: ")
    qty = int(input("Enter quantity: "))
    inventory[name] = qty
    print("Product added successfully.")

def update_product():
    name = input("Enter product name: ")
    if name in inventory:
        qty = int(input("Enter new quantity: "))
        inventory[name] = qty
        print("Quantity updated.")
    else:
        print("Product not found.")

def highest_stock():
    if inventory:
        product = max(inventory, key=inventory.get)
        print("Highest Stock Product:", product)
        print("Quantity:", inventory[product])
    else:
        print("Inventory is empty.")

def remove_product():
    name = input("Enter product name: ")
    if name in inventory:
        if inventory[name] == 0:
            del inventory[name]
            print("Product removed.")
        else:
            print("Quantity is not zero. Cannot remove.")
    else:
        print("Product not found.")

def total_products():
    print("Total Products:", len(inventory))

while True:
    print("\n1.Add Product")
    print("2.Update Quantity")
    print("3.Highest Stock")
    print("4.Remove Product")
    print("5.Total Products")
    print("6.Display Inventory")
    print("7.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_product()
    elif choice == 2:
        update_product()
    elif choice == 3:
        highest_stock()
    elif choice == 4:
        remove_product()
    elif choice == 5:
        total_products()
    elif choice == 6:
        print(inventory)
    elif choice == 7:
        break
    else:
        print("Invalid Choice")