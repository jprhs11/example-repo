class Shoe:
    """
    A class to represent a shoe item in the inventory.
    """

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        """Returns the cost of the shoe."""
        return self.cost

    def get_quantity(self):
        """Returns the quantity of the shoe in stock."""
        return self.quantity

    def __str__(self):
        """Returns a string representation of the Shoe object."""
        return (
            f"({self.country}, {self.code}, {self.product}, "
            f"{self.cost}, {self.quantity})"
        )


# Global list to store shoe objects
shoe_list = []


def read_shoes_data():
    """Reads data from inventory.txt and populates shoe_list."""
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # Skip the header line
            for line in file:
                data = line.strip().split(",")
                if len(data) == 5:
                    new_shoe = Shoe(*data)
                    shoe_list.append(new_shoe)
    except FileNotFoundError:
        print("Error: inventory.txt not found. Please ensure the file exists.")


def capture_shoes():
    """Allows user to manually add a new shoe to the inventory."""
    try:
        country = input("Enter Country: ")
        code = input("Enter SKU Code: ")
        product = input("Enter Product Name: ")
        cost = float(input("Enter Cost: "))
        quantity = int(input("Enter Quantity: "))

        new_shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(new_shoe)
        print("Shoe successfully captured and added to the list.")
    except ValueError:
        print("Invalid input. Please ensure cost and quantity are numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def view_all():
    """Prints all shoes using manual string padding for alignment."""
    header = (
        f"{'Country':<20} | {'Code':<10} | {'Product':<25} |"
        f"{'Cost':<10} | {'Quantity':<10}"
    )
    print(header)
    print("-" * len(header))
    for s in shoe_list:
        print(
            f"{s.country:<20} | {s.code:<10} | {s.product:<25} |"
            f"{s.cost:<10.2f} | {s.quantity:<10}"
        )


def re_stock():
    """Finds the shoe with the lowest quantity and allows restocking."""
    if not shoe_list:
        print("Inventory is empty.")
        return

    lowest_shoe = min(shoe_list, key=lambda x: x.quantity)
    print(
        f"\nLOWEST STOCK ALERT: {lowest_shoe.product} "
        f"has only {lowest_shoe.quantity} units."
    )

    update = input("Do you want to add stock? (yes/no): ").lower()
    if update == "yes":
        try:
            amount = int(input("Enter quantity to add: "))
            lowest_shoe.quantity += amount
            print("Stock updated successfully.")
        except ValueError:
            print("Invalid input. Quantity must be an integer.")


def search_shoe(code):
    """Searches for a shoe by its SKU code."""
    for shoe in shoe_list:
        if shoe.code == code:
            return shoe
    return None


def highest_qty():
    """Identifies the shoe with the highest quantity (suggested for sale)."""
    if not shoe_list:
        return

    highest_shoe = max(shoe_list, key=lambda x: x.quantity)
    print(
        f"\nFOR SALE: {highest_shoe.product} is currently overstocked "
        f"({highest_shoe.quantity} units)."
    )


def value_per_item():
    """Calculates and displays the total inventory value per shoe."""
    print(f"\n{'Product':<25} | {'Total Value':<15}")
    print("-" * 43)
    for s in shoe_list:
        value = s.cost * s.quantity
        print(f"{s.product:<25} | R{value:,.2f}")


def main_menu():
    """Main program loop and interface."""
    read_shoes_data()
    print(f"Total shoes loaded: {len(shoe_list)}")

    while True:
        print("\n--- SHOE INVENTORY MANAGEMENT ---")
        print(
            "1. Capture | 2. View | 3. Re-stock | 4. Search | "
            "5. Value | 6. Highest | 7. Exit"
        )
        choice = input("Enter choice (1-7): ")

        if choice == '1':
            capture_shoes()
        elif choice == '2':
            view_all()
        elif choice == '3':
            re_stock()
        elif choice == '4':
            code_to_find = input("Enter SKU Code to search: ")
            result = search_shoe(code_to_find)
            if result:
                print(f"Found: {result}")
            else:
                print("Product not found.")
        elif choice == '5':
            value_per_item()
        elif choice == '6':
            highest_qty()
        elif choice == '7':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please select 1-7.")


if __name__ == "__main__":
    main_menu()
