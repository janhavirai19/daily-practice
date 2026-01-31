#addition of two values>>>>>>>>>>>>>>>>>>>>

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
        print("Invalid operator ")



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




# Smart Employee Evaluation System  >>>>>>>>>>


print("Smart Employee Evaluation System--")

name=input("Employee Name: ")
age=int(input("age:"))
salary=int(input("Monthly Salary:"))
experience=int(input("Experience(years): "))
department=input("Department: ")
  

annual_salary=salary*12
bonus=salary* 0.10
total_salary=annual_salary +bonus

is_senior = age>=40
is_experienced=experience>5

eligible_for_promotion = is_senior and is_experienced
high_potential=is_senior or experience >=3
not_fresher = not (experience ==0)

performance_score=0
performance_score+=10
performance_score+=experience
performance_score -= 2


allowed_departments =["IT","HR","Finance","Management"]
dept_check=department in allowed_departments

default_bonus=None
has_bonus = default_bonus is None

flag_admin=1
flag_employee=2

access_level = flag_admin | flag_employee   
security_check = flag_admin & flag_employee


print("\n== Employee Details==")
print("Name:",name)
print("Annual salary:",annual_salary)
print("Total Salary with Bonus:",total_salary)

print("\n Eligibility::")
print("Senior Employee:",is_experienced)
print("Promotion Eligible",eligible_for_promotion)
print("High Potential:",high_potential)
print("Not fresher",not_fresher)
print("\nDepartment Valid:", dept_check)
print("Bonus Assigned:", has_bonus)

print("\nAccess Level Code:", access_level)
print("Security Check Code:", security_check)

print("\nPerformance Score:", performance_score)
print("---- Evaluation Completed ----")
