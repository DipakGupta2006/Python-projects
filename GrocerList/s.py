import os

grocery_list = []

def load_list():
    if os.path.exists("grocery_list.txt"):
        with open("grocery_list.txt", "r") as file:
            for line in file:
                grocery_list.append(line.strip())

def save_list():
    with open("grocery_list.txt", "w") as file:
        for item in grocery_list:
            file.write(item + "\n")

def add_item():
    item = input("Enter item to add: ").strip()
    grocery_list.append(item)
    print(f"✅ '{item}' added to your grocery list.")

def view_list():
    if not grocery_list:
        print("🛒 Your grocery list is empty.")
        return
    print("\n📝 Grocery List:")
    for idx, item in enumerate(grocery_list, start=1):
        print(f"{idx}. {item}")

def remove_item():
    view_list()
    if not grocery_list:
        return
    try:
        index = int(input("Enter item number to remove: "))
        removed = grocery_list.pop(index - 1)
        print(f"❌ '{removed}' removed from the list.")
    except (ValueError, IndexError):
        print("⚠️ Invalid input. Try again.")

def menu():
    print("\n==== Grocery List App ====")
    print("1. Add Item")
    print("2. View List")
    print("3. Remove Item")
    print("4. Save List")
    print("5. Load List")
    print("6. Exit")

load_list()

while True:
    menu()
    choice = input("Choose an option (1-6): ")
    
    if choice == "1":
        add_item()
    elif choice == "2":
        view_list()
    elif choice == "3":
        remove_item()
    elif choice == "4":
        save_list()
        print("💾 List saved.")
    elif choice == "5":
        grocery_list.clear()
        load_list()
        print("📂 List loaded from file.")
    elif choice == "6":
        save_list()
        print("👋 Exiting... Your list is saved.")
        break
    else:
        print("❗Invalid choice. Please try again.")
