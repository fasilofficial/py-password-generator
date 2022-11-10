import random
print(" PYTHON PASSWORD GENERATOR ")
print("***************************\n")
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,0123456789'
number = int(input("Enter number of passwords: "))
length = int(input("Enter password length: "))
print("\nHere are your passwords:\n")
for i in range(1, number+1):
    password = ''
    for len in range(length):
        password += random.choice(chars)
    print(f"{i}) {password}")