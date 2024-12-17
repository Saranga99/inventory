import datetime

# Inventory Management System using Python Data Structures
inventory = {
    1: {"product_name": "Laptop", "brand": "Dell", "model": "XPS 13", "price": 999.99, "quantity": 10},
    2: {"product_name": "Smartphone", "brand": "Samsung", "model": "Galaxy S21", "price": 799.99, "quantity": 15},
    3: {"product_name": "Tablet", "brand": "Apple", "model": "iPad Pro", "price": 1099.99, "quantity": 5},
}

sales_history = []
returns_history = []

# Function to display available products
def display_products():
    print("\n" + "-"*50)
    print(f"{'Available Products:':^50}")
    print("-" * 50)
    print(f"{'Product ID':<12}{'Product Name':<20}{'Brand':<15}{'Model':<15}{'Price':<10}{'Quantity Available':<20}")
    print("-" * 50)
    for product_id, details in inventory.items():
        print(f"{product_id:<12}{details['product_name']:<20}{details['brand']:<15}{details['model']:<15}${details['price']:<10}{details['quantity']:<20}")
    print("-" * 50)

# Function to sell a product
def sell_product():
    customer_name = input("\nEnter customer's name: ")
    try:
        product_id = int(input("Enter the product ID to sell: "))
        if product_id in inventory:
            quantity = int(input(f"Enter quantity of {inventory[product_id]['product_name']} to sell: "))
            if inventory[product_id]["quantity"] >= quantity:
                # Update inventory
                inventory[product_id]["quantity"] -= quantity
                sale_amount = inventory[product_id]["price"] * quantity
                sale_id = len(sales_history) + 1
                sale_date = datetime.date.today()
                sales_history.append({
                    "sale_id": sale_id,
                    "customer_name": customer_name,
                    "product_name": inventory[product_id]["product_name"],
                    "product_id": product_id,
                    "quantity_sold": quantity,
                    "sale_amount": sale_amount,
                    "sale_date": str(sale_date),
                })
                print(f"\n{'Sale completed!':^50}")
                print(f"Sold {quantity} {inventory[product_id]['product_name']}(s) to {customer_name}.")
                print(f"{'Remaining Quantity:':<20} {inventory[product_id]['quantity']}")
                print(f"Sale Amount: ${sale_amount:.2f}")
            else:
                print(f"Insufficient stock for {inventory[product_id]['product_name']}. Only {inventory[product_id]['quantity']} available.")
        else:
            print("Invalid Product ID.")
    except ValueError:
        print("Invalid input. Please enter a valid product ID.")

# Function to process a return
def process_return():
    sale_id = int(input("\nEnter sale ID for return: "))
    for sale in sales_history:
        if sale["sale_id"] == sale_id:
            product_name = sale["product_name"]
            quantity_sold = sale["quantity_sold"]
            product_id = sale["product_id"]
            quantity_returned = int(input(f"Enter quantity of {product_name} to return: "))

            # Validate quantity returned is greater than 0 and less than or equal to quantity sold
            if quantity_returned <= 0:
                print("Returned quantity must be greater than 0.")
                return
            if quantity_returned > quantity_sold:
                print(f"Cannot return more than the quantity sold ({quantity_sold}).")
                return

            # Update inventory
            inventory[product_id]["quantity"] += quantity_returned
            refund_amount = inventory[product_id]["price"] * quantity_returned
            return_date = datetime.date.today()
            returns_history.append({
                "sale_id": sale_id,
                "customer_name": sale["customer_name"],
                "product_name": product_name,
                "product_id": product_id,
                "quantity_returned": quantity_returned,
                "refund_amount": refund_amount,
                "return_date": str(return_date),
            })
            print(f"\n{'Return processed!':^50}")
            print(f"Returned {quantity_returned} {product_name}(s). Refund amount: ${refund_amount:.2f}")
            return
    print("Sale ID not found.")

# Function to display sales history
def display_sales_history():
    print("\n" + "-"*50)
    print(f"{'Sales History:':^50}")
    print("-" * 50)
    print(f"{'Sale ID':<10}{'Customer Name':<20}{'Product ID':<12}{'Product Name':<20}{'Quantity Sold':<15}{'Sale Amount':<15}{'Sale Date':<15}")
    print("-" * 50)
    for sale in sales_history:
        print(f"{sale['sale_id']:<10}{sale['customer_name']:<20}{sale['product_id']:<12}{sale['product_name']:<20}{sale['quantity_sold']:<15}{sale['sale_amount']:<15.2f}{sale['sale_date']:<15}")
    print("-" * 50)

# Function to display return history
def display_returned_history():
    print("\n" + "-"*50)
    print(f"{'Return History:':^50}")
    print("-" * 50)
    print(f"{'Sale ID':<10}{'Customer Name':<20}{'Product ID':<12}{'Product Name':<20}{'Quantity Returned':<20}{'Refund Amount':<15}{'Return Date':<15}")
    print("-" * 50)
    for return_item in returns_history:
        print(f"{return_item['sale_id']:<10}{return_item['customer_name']:<20}{return_item['product_id']:<12}{return_item['product_name']:<20}{return_item['quantity_returned']:<20}{return_item['refund_amount']:<15.2f}{return_item['return_date']:<15}")
    print("-" * 50)

# Function to display customer information
def display_customer_info():
    customer_name = input("\nEnter the customer's name to search for their transactions: ")
    found = False
    print("\n" + "-"*50)
    print(f"{'Customer Transaction History':^50}")
    print("-" * 50)
    print(f"{'Sale ID':<10}{'Product Name':<20}{'Quantity Sold':<15}{'Sale Amount':<15}{'Sale Date':<15}")
    print("-" * 50)
    for sale in sales_history:
        if sale["customer_name"].lower() == customer_name.lower():
            print(f"{sale['sale_id']:<10}{sale['product_name']:<20}{sale['quantity_sold']:<15}{sale['sale_amount']:<15.2f}{sale['sale_date']:<15}")
            found = True
    if not found:
        print(f"No transactions found for customer: {customer_name}")
    print("-" * 50)

# Main menu function
def main_menu():
    while True:
        print("\nInventory Management System")
        print("-" * 50)
        print("1. Display Available Products")
        print("2. Sell a Product")
        print("3. Process a Return")
        print("4. Display Sales History")
        print("5. Display Customer Information")
        print("6. Display Return History")
        print("7. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            display_products()
        elif choice == '2':
            sell_product()
        elif choice == '3':
            process_return()
        elif choice == '4':
            display_sales_history()
        elif choice == '5':
            display_customer_info()
        elif choice == '6':
            display_returned_history()
        elif choice == '7':
            print("\nExiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the system
main_menu()