import string
import random

# print(num)
# all_characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
# print(all_characters)

# print("yor pass ",password)
print("🔐 Password Generator")

password = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

while True:
    user_input = input("Enter length of your password: ")
    if user_input.isdigit():
        n = int(user_input)
        break
    else:
        print("❌ Please enter a valid number!")


print("Your password is ready ")
for i in range(n):
    num = random.randint(0, 93)
    print(password[num], end="")