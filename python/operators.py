#addition of two values>>>>>>>>>>>>>>>>>>>>

# a=int(input("Enter ur first number "))
# b=int(input("Enter ur first number "))
# op=input("Enter operatos(+,-,*,/)")
# match op:
#     case "+":
#         print("Addition",a+b)
#     case "-":
#         print("Subtaction",a-b)
#     case "*":
#         print("Multiplication",a*b)
#     case "/":
#         print("Division",a/b)
#     case "%":
#         print("Modulus:", a % b)
#     case "**":
#         print("Power:", a ** b)
#     case _:
#         print("Invalid operator ")


#Smart Queue Priority System WITH COMPARISION OPERATORS >>>>>>>>>>>>>>>>>>>>


name=input("Enter customer name: ")
age=int(input("enter age:"))
vip=input("Are u  VIP? (yes/no):") 
print ("\n --- Queue Status---")

if age>=60:
    print(name,"is a Senior Citizen-> High Prioriy")
elif vip=="yes":
    print(name,"is a VIP Customer-> Medium Priority")
else:
    print(name,"is a Normal Custome->Low priority")