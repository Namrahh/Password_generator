import random

letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n', 'o','p','q','r','s','t','u','v','w','x','y','z',]
numbers = ['0','1','2','3','4','5','6','7','8','9']            
symbols = ['!','@','#','$','%','^','&','*','(',')','_','+']

# easy letter+symbols+numbers
# hard shuffle

print("Welcome to the PyPassword Generator!")

nr_letter = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

password = " "

for i in range(1, nr_letter+1):
  password += random.choice(letter)

for i in range (1, nr_numbers + 1):
  password += random.choice(numbers)

for i in range(1,nr_symbols + 1):
  password += random.choice(symbols)

print (f"Your password is: {password}")
