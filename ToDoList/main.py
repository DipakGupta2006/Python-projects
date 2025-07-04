print("sj")
lst = []

def view():
    if len(lst) == 0:
        print("Your Todo List is Empty Type 2 for adding your Task")
        return
    
    print("Your Task:")
    j=1
    for i in lst:
        print(f"{j}. {i.title()}")
        j+=1

def add():
    t = input("Enter new Task: ")
    lst.append(t)
    print("Task added!")


def done():
    print("Your Task:")
    j=1
    for i in lst:
        print(f"{j}. {i}")
        j+=1
    
    d = int(input("Enter task number to mark as done: "))

    lst[d-1] += " ✅" 
    


def rem():
    print("Your Task:")
    j=1
    for i in lst:
        print(f"{j}. {i}")
        j+=1
    r = int(input("Enter task number to remove: "))
    lst.pop(r-1)

while True:
    print("\n--- To-Do List ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Remove task")
    print("5. Quit")
    print()

    try:
        choose = int(input("Enter your choice (1-5): "))
        print()
        print()

        if choose == 1:
            view()

        elif choose == 2:
            add()

        elif choose == 3:
            done()

        elif choose == 4:
            rem()

        elif choose == 5:
            break

        else:
            print("Invalid Input! Please enter a number between 1-5.")

    except ValueError:
        print("\nInvalid Input! Please enter a valid integer.")


print("Goodbye")

