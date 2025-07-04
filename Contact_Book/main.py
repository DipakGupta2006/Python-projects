contact = {}
def add():
    name = input("👤 Enter name: ")

    if name in contact:
        print("⚠️ Contact already exists.")
        return
    
    number = input("📞 Enter phone number: ")
    email = input("✉️ Enter email address: ")
    print("✅ Contact added successfully!")
    contact[name] = {number, email}
    print()


def view():
    if not contact:
        print("📭 No contacts found.")
        return
    
    print("\n📒 Your Contacts:")
    for k, v in contact.items():
        print(f"Name: {k} - Phone and Email: {v}")
    print()



def search():
    s = input("🔍 Enter name to search: ").strip()
    
    if s in contact:
        print(contact[s])
    else :
        print("❌ Contact not found.")



def delete():
    x = input("🗑️ Enter name to delete: ").strip()

    if x in contact:
        del contact[x]
        print("✅ Contact deleted successfully.")
    else:
        print("❌ Contact not found.")

while True:
     print()
     print("📚 CONTACT BOOK")
     print()
     print("1. Add Contact")
     print("2. View Contacts")
     print("3. Search Contact")
     print("4. Delete Contact")
     print("5. Exit")

     choice = int(input("📲 Choose an option (1-5): ").strip())
     print()
     if choice == 1:
        add()
     elif choice == 2:
        view()
     elif choice == 3:
        search()
     elif choice == 4:
        delete()
     elif choice == 5:
        print("👋 Exiting Contact Book. Goodbye!")
        break
     else:
        print("❌ Invalid choice. Please try again.\n")


