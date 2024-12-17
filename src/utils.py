# src/utils.py

import datetime

class Inventory:
    def __init__(self):
        self.products = {
            1: {"product_name": "Laptop", "brand": "Dell", "model": "XPS 13", "price": 999.99, "quantity": 10},
            2: {"product_name": "Smartphone", "brand": "Samsung", "model": "Galaxy S21", "price": 799.99, "quantity": 15},
            3: {"product_name": "Tablet", "brand": "Apple", "model": "iPad Pro", "price": 1099.99, "quantity": 5},
        }

    def display_products(self):
        print("\n" + "-"*50)
        print(f"{'Available Products:':^50}")
        print("-" * 50)
        print(f"{'Product ID':<12}{'Product Name':<20}{'Brand':<15}{'Model':<15}{'Price':<10}{'Quantity Available':<20}")
        print("-" * 50)
        for product_id, details in self.products.items():
            print(f"{product_id:<12}{details['product_name']:<20}{details['brand']:<15}{details['model']:<15}${details['price']:<10}{details['quantity']:<20}")
        print("-" * 50)

    def sell_product(self, product_id, quantity):
        if product_id in self.products and self.products[product_id]["quantity"] >= quantity:
            self.products[product_id]["quantity"] -= quantity
            return self.products[product_id]["product_name"], self.products[product_id]["price"]
        return None, None

    def process_return(self, product_id, quantity):
        if product_id in self.products and quantity > 0:
            self.products[product_id]["quantity"] += quantity
            return self.products[product_id]["product_name"], self.products[product_id]["price"]
        return None, None


class Sales:
    def __init__(self):
        self.sales_history = []
        self.sale_id_counter = 1

    def record_sale(self, customer_name, product_name, quantity_sold, sale_date):
        sale_id = self.sale_id_counter
        self.sales_history.append({
            "sale_id": sale_id,
            "customer_name": customer_name,
            "product_name": product_name,
            "quantity_sold": quantity_sold,
            "sale_date": sale_date,
        })
        self.sale_id_counter += 1
        return sale_id

    def display_sales(self):
        print("\n" + "-"*50)
        print(f"{'Sales History:':^50}")
        print("-" * 50)
        print(f"{'Sale ID':<10}{'Customer Name':<20}{'Product Name':<20}{'Quantity Sold':<15}{'Sale Date':<15}")
        print("-" * 50)
        for sale in self.sales_history:
            print(f"{sale['sale_id']:<10}{sale['customer_name']:<20}{sale['product_name']:<20}{sale['quantity_sold']:<15}{sale['sale_date']:<15}")
        print("-" * 50)


class Returns:
    def __init__(self):
        self.returns_history = []

    def record_return(self, sale_id, customer_name, product_name, quantity_returned, return_date, refund_amount):
        self.returns_history.append({
            "sale_id": sale_id,
            "customer_name": customer_name,
            "product_name": product_name,
            "quantity_returned": quantity_returned,
            "return_date": return_date,
            "refund_amount": refund_amount,
        })

    def display_returns(self):
        print("\n" + "-"*50)
        print(f"{'Return History:':^50}")
        print("-" * 50)
        print(f"{'Sale ID':<10}{'Customer Name':<20}{'Product Name':<20}{'Quantity Returned':<15}{'Return Date':<15}")
        print("-" * 50)
        for return_record in self.returns_history:
            print(f"{return_record['sale_id']:<10}{return_record['customer_name']:<20}{return_record['product_name']:<20}{return_record['quantity_returned']:<15}{return_record['return_date']:<15}")
        print("-" * 50)