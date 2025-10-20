import csv

FILENAME = "inventory.csv"

#   Adding new item


def add_item():
    name = input("Item Name:  ")
    quantity = int(input("Quantity: "))
    price = float(input("unit price ($): "))

    with open(FILENAME,  "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, quantity, price])
    print("✅ Item added successfully!\n")

# view all item


def view_inventory():
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            print("\n=== current inventory ===")
            print(f"{'Item':20s} {'Qty':>6s} {'Price (₦)':>10s}")
            print("-" * 40)
            for row in reader:
                print(f"{row[0]:20s} {row[1]:>6s} {row[2]:>10s}")
            print()
    except FileNotFoundError:
        print("⚠️ No inventory file found. Add items first.\n")

# sell an item


def sell_item():
    item_to_sell = input("Enter item name to sell: ")
    qty_sold = int(input("Enter quantity sold: "))

    items = []
    found = False

    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                name, qty, price = row
                qty = int(qty)
                if name.lower() == item_to_sell.lower():
                    found = True
                    if qty_sold > qty:
                        print("❌ Not enough stock available.")
                        return
                    qty -= qty_sold
                    print(f"✅ Sold {qty_sold} units of {name}.")
                items.append([name, qty, price])
    except FileNotFoundError:
        print("⚠️ No inventory file found.\n")
        return

    if found:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(items)
    else:
        print("❌ Item not found.\n")


# check low stock items

def low_stock_alert():
    threshold = int(input("Enter low stock threshold: "))
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            print("\n=== Low Stock Items ===")
            for row in reader:
                name, qty, price = row
                if int(qty) <= threshold:
                    print(f"⚠️ {name} has only {qty} left!")
            print()
    except FileNotFoundError:
        print("⚠️ No inventory file found.\n")


# restock an item
def restock_item():
    item_to_restock = input("Enter item name to restock: ")
    try:
        qty_added = int(input("Enter quantity to add: "))
        if qty_added <= 0:
            print("❌ Quantity must be a positive integer.")
            return
    except ValueError:
        print("❌ Invalid quantity. Please enter a number.")
        return

    items = []
    found = False

    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                name, qty, price = row
                qty = int(qty)
                if name.lower() == item_to_restock.lower():
                    found = True
                    qty += qty_added
                    print(f"✅ Restocked {qty_added} units of {name}.")
                items.append([name, qty, price])
    except FileNotFoundError:
        print("⚠️ No inventory file found.\n")
        return

    if found:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(items)
    else:
        print("❌ Item not found.\n")

        # --- 6. Main menu ---


def main():
    while True:
        print("=== Inventory Tracker ===")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Sell Item")
        print("4. Check low stock")
        print("5. Restock Item")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            sell_item()
        elif choice == "4":
            restock_item()
        elif choice == "5":
            low_stock_alert()
        elif choice == "6":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
