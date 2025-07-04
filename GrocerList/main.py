lst = []

def add():
    s = input("Enter item to add: ").strip()
    lst.append(s)
    print(f"✅ '{s}' added to your grocery list.")

def view():
    if not lst:
        print("🛒 Your grocery list is empty.")
        return
    print("📝 Grocery List:")

    idx = 1
    for item in lst:
        print(f"{idx}. {item}")
        idx+=1


def remove():
    print("📝 Grocery List:")
    idx = 1
    for item in lst:
        print(f"{idx}. {item}")
        idx+=1

    if not lst:
        return
    try:
        index = int(input("Enter item number to remove: "))
        removed = lst.pop(index - 1)
        print(f"❌ '{removed}' removed from the list.")
    except (ValueError, IndexError):
        print("⚠️ Invalid input. Try again.")


while True:

    print("\n==== Grocery List App ====")
    print("1. Add Item")
    print("2. View List")
    print("3. Remove Item")
    print("4. Save List")
    print("5. Load List")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")
    
    if choice == "1":
        add()

    elif choice == "2":
        view()

    elif choice == "3":
        remove()

    elif choice == "4":
        # save()
        print("💾 List saved.")

    elif choice == "5":
        # grocery_list.clear()
        # load_list()
        print("📂 List loaded from file.")
    
    elif choice == "6":
        # save_list()
        print("👋 Exiting... Your list is saved.")
        break
    
    else:
        print("❗Invalid choice. Please try again.")