class Product:
    def __init__(self, product_id, name, quantity, price):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.next = None  # Pointer to the next product (for linked list functionality)

class Inventory:
    def __init__(self):
        self.head = None

    def add_product(self, product_id, name, quantity, price):
        new_product = Product(product_id, name, quantity, price)
        if self.head is None:
            self.head = new_product
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_product
        print(f"Added product: {name}, ID: {product_id}, Quantity: {quantity}, Price: ${price:.2f}")

    def update_quantity(self, product_id, quantity):
        current = self.head
        while current:
            if current.product_id == product_id:
                current.quantity += quantity
                print(f"Updated quantity for {current.name}: New Quantity: {current.quantity}")
                return
            current = current.next
        print("Product not found!")

    def calculate_total_value(self):
        total_value = 0
        current = self.head
        while current:
            total_value += current.quantity * current.price
            current = current.next
        return total_value

    def display_inventory(self):
        if self.head is None:
            print("Inventory is empty.")
            return
        print("Current Inventory:")
        current = self.head
        while current:
            print(f"ID: {current.product_id}, Name: {current.name}, Quantity: {current.quantity}, Price: ${current.price:.2f}")
            current = current.next

def main():
    inventory = Inventory()
    
    # Adding initial products
    inventory.add_product(101, "Laptop", 50, 800)
    inventory.add_product(102, "Smartphone", 100, 500)
    inventory.add_product(103, "Tablet", 30, 400)
    
    while True:
        print("\nInventory Management System")
        print("1: Add Product")
        print("2: Update Product Quantity")
        print("3: Calculate Total Inventory Value")
        print("4: Display Inventory")
        print("5: Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            product_id = int(input("Enter product ID: "))
            name = input("Enter product name: ")
            quantity = int(input("Enter product quantity: "))
            price = float(input("Enter product price: "))
            inventory.add_product(product_id, name, quantity, price)
        elif choice == 2:
            product_id = int(input("Enter product ID to update quantity: "))
            quantity = int(input("Enter quantity to add (can be negative to decrease): "))
            inventory.update_quantity(product_id, quantity)
        elif choice == 3:
            total_value = inventory.calculate_total_value()
            print(f"Total inventory value: ${total_value:.2f}")
        elif choice == 4:
            inventory.display_inventory()
        elif choice == 5:
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
