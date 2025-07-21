menu = {
    "Coffee": 30,
    "Tea": 25,
    "Pasta": 50,
    "Boiled Egg": 15,
    "Milk": 45,
    "Chips": 30,
    "Biscuit": 25
}

print("Welcome to our restaurant! Here's the menu:\n")
for item, price in menu.items():
    print(f"{item}: ₹{price}")

total = 0
ordering = True  # Flag to control the outer loop

while ordering:
    order = input("\nEnter the item you want to order: ").strip().title()

    if order in menu:
        print(f"✔️ Order for '{order}' has been added.")
        total += menu[order]
        print(f"💰 Your total price is now: ₹{total}")

        # Validate the 'yes/no' response
        while True:
            anymore = input("Do you want to order another item? (yes/no): ").strip().lower()
            
            if anymore == "yes":
                break  # Back to the outer ordering loop
            elif anymore == "no":
                print("\n🙏 Thank you for your order!")
                print(f"🧾 Final Bill: ₹{total}")
                ordering = False  # Set flag to False to stop the outer loop
                break
            else:
                print("⚠️ Invalid input. Please type 'yes' or 'no'.")
    else:
        print("❌ Sorry! This item is not available.")
        print("📜 Please choose from the menu.")
