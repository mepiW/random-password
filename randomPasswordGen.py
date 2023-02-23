import random
import string

print("PASSWORD GENERATOR")
print("=" * 18)

lenght = int(input("How many characters should your password be? "))

upper = string.ascii_uppercase
lower = string.ascii_lowercase
nums = string.digits
symbols = "!#$%&+-/*?@._"

password = ""

for i in range(1, lenght):
    chars = "".join(random.choice(upper + lower + nums + symbols))  
    password += chars

print(f"Here is your randomly generated password: {password}")