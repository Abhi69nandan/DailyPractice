import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '=', '_', '+', '?']
print("Welcome to Password Generator")
num_lett = int(input("Enter the no. of letters you want: "))
num_num = int(input("Enter the no. of number you want: "))
num_sym = int(input("Enter the no. of symbols you want: "))
password_list = []
for char in range(1, num_lett + 1):
    password_list.append(random.choice(letters))

for num in range(1, num_num + 1):
    password_list.append(random.choice(numbers))

for sym in range(1, num_sym + 1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your Password is {password}")
