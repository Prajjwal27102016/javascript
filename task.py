menu = {
    "1": {"name": "Sahi Paneer", "price": 200},
    "2": {"name": "Chhole Bature", "price": 100},
    "3": {"name": "Pizza", "price": 220},
    "4": {"name": "French Fries", "price": 150}
}

print("Welcome to the Digital Cafe")
for key, item in menu.items():
    print(f"{key}. {item['name']} - Rs {item['price']}")

choice = input("\nPlease enter the number of the item you want to order: ")

if choice in menu:
    selected_item = menu[choice]["name"]
    price = menu[choice]["price"]
    print("=" * 30)
    print(f"You selected: {selected_item}")
    print(f"Total Amount to Pay: Rs {price}")
    print("=" * 30)
    print("Thank you for your order!")
else:
    print("Invalid choice. Please pick a number from 1 to 4.")