import string
import random

alphabets = list(string.ascii_letters)
numbers = list(range(10))
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to MyPyPassword Generator")
num_total = int(input("Enter the length of your desired password (alphabets + numbers + symbols): "))
num_alpha = int(input(f"Out of {num_total}, how many alphabets? : "))
if num_alpha >= num_total:
    print("Passwords needs to have Alphabets + Numbers + Symbols")
    exit()

num_numbers = int(input(f"from the remaining {num_total - num_alpha} characters, how many numbers? : "))
if num_numbers >= num_total - num_alpha:
    print(f"Passwords needs to have Alphabets + Numbers + Symbols. You only have {num_total - num_alpha} characters left Please select a number less than {num_total - num_alpha}")
    exit()

num_symbols = num_total - num_alpha - num_numbers
if num_symbols <= 0:
    print("Passwords needs to have Alphabets + Numbers + Symbols")
    exit()

print(f"Will use {num_symbols} symbols in the password")

print("\n############### Generating a secure password ###############")
final_password = []

for i in range(num_alpha):
    final_password.append(random.choice(alphabets))
for i in range(num_numbers):
    final_password.append(random.choice(numbers))
for i in range(num_symbols):
    final_password.append(random.choice(symbols))

random.shuffle(final_password)
final_password = ''.join([str(i) for i in final_password]) 
print(f"\n\t\tYour Password is: {final_password}")
print("\n############################################################")


