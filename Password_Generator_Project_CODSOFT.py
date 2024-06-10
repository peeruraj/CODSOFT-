import random

Uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
Random_chars = "{]}];:/?,<>\|()!@#$%^&*-_=+,"

Must_chars = random.choice(Uppercase_letters)+ random.choice(lowercase_letters)+ random.choice(numbers) + random.choice(Random_chars)

All_chars_to_Gen_pass = Uppercase_letters + lowercase_letters + numbers + Random_chars

print("-----------Password Generator-----------")

Result = ""
Length = int(input("Enter the Length of Password: "))

if Length < 4 :
    print("Enter the Desired Length to generate the Password again....")


for i in range(Length-4):
    Result = Result + random.choice(All_chars_to_Gen_pass)

print(f"\nGenerated password is : {Must_chars+Result}")
