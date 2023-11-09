#Aprel Py-Calc

def Add(num1, num2):
  return num1 + num2

def Subtract(num1, num2):
  return num1 - num2

def Multiply(num1, num2):
  return num1 * num2

def Divide(num1, num2):
  return num1 / num2

def main():
  while True:
    # Get the first number.
    num1 = float(input("Input the first number: "))

    # Get the operator.
    operator = input("Enter the operator (+, -, *, /): ")

    # Get the second number.
    num2 = float(input("Input the second number: "))

    # Perform the operation based on the operator.
    if operator == "+":
      result = Add(num1, num2)
    elif operator == "-":
      result = Subtract(num1, num2)
    elif operator == "*":
      result = Multiply(num1, num2)
    elif operator == "/":
      result = Divide(num1, num2)
    else:
      print("Invalid")
      continue

    if num1<num2:
      print("ERROR")
      continue

    # Print the result.
    print(f"{num1} {operator} {num2} = {result}")

    # Ask the user if they want to continue.
    if input("Do you want to continue? (Y/N): ") == "Y":
      continue
    else:
      break

if __name__ == "__main__":
  main()
