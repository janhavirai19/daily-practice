a=int(input("Enter ur first number "))
b=int(input("Enter ur first number "))
op=input("Enter operatos(+,-,*,/)")
match op:
    case "+":
        print("Addition",a+b)
    case "-":
        print("Subtaction",a-b)
    case "*":
        print("Multiplication",a*b)
    case "/":
        print("Division",a/b)
    case "%":
        print("Modulus:", a % b)
    case "**":
        print("Power:", a ** b)
    case _:
        print("Invalid operator ❌")