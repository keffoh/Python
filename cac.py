def calculator():
    num1 = float(input("Enter your first number:"))
    num2 = float(input("Enter your second number:"))
    operator = input("Enter the operation(+, -, *, /):")
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator =='/':
        if num2 != 0:
             result = num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."
    return f"{num1} {operator} {num2} = {result}" 
if __name__ == "__main__":
    print(calculator())
            
       