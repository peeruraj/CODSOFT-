def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error! numbers cannot divide with zero."
    
def modulo(num1,num2):
    return num1 % num2
    
a = True
while a:
    print("\n--------Math Calculator--------\n")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Choose the operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulo")
    print("6. Exit from Calculator")
    choose = input("Enter choice (1/2/3/4/5/6 to exit): ")
        
    if choose == "1":
        result = addition(num1, num2)
        operation = "+"

    elif choose == "2":
        result = subtraction(num1, num2)
        operation = "-"

    elif choose == "3":
        result = multiplication(num1, num2)
        operation = "*"

    elif choose == "4":
        result = division(num1, num2)
        operation = "/"

    elif choose == "5":
        result = modulo(num1, num2)
        operation = "%"

    else :
        result = "Invalid choice"
        operation = ""
    
    if choose == "6":
        print("Exiting from the Calculator.....")
        break

    elif operation:
        print(f"{num1} {operation} {num2} = {result} ✔")
    else:
        print(result)
    
