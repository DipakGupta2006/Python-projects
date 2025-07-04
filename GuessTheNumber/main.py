import random as r

print("🎯 Welcome to the 'Guess the Number' game!")
print("I've picked a number between 1 and 100. Can you guess it?")
print()

randomNum = r.randint(1,100)

count =0

while True:
    try:
        user = int(input("Enter your guess : "))
        
        count+=1
        if randomNum < user:
            print("📈 Too high! Try again.")
        
        elif randomNum > user :
            print("📉 Too low! Try again.")

        else:
            print(f"🎉 Correct! You guessed the number in {count} attempts.")
            break
        print()

    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        print()
    
