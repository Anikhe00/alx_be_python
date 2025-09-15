num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
result = 0

match operation:
  case "+":
    result = num1 + num2
    print(f"The result is {result}")
  case "-":
    result = num1 - num2
    print(f"The result is {result}")
  case "*":
    result = num1 * num2
    print(f"The result is {result}")
  case "/":
    if num2 != 0:
      result = round(num1 / num2, 2)
      print(f"The result is {result}")
    else:
      print(f"Cannot divide by zero.")
  case _:
    print("Invalid operator.")

