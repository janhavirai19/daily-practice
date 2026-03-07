# contacts={
#     "Aman":98765,
#     "Riya":78544,
#     "Siya":89643
# }
# name=input("Enter name: ")
# if name in contacts:
#     print("Number:",contacts[name])
# else:
#     print("Contact not found")



# Output>>>>>>

    #  right input *********
# Enter name: Siya
# Number: 89643

    #  Wrong input   *******
# Enter name: janhavi
# Contact not found


contacts = {
    "Aman": 98765,
    "Riya": 78544,
    "Siya": 89643
}
name = input("Enter name: ").capitalize()
if name in contacts:
    print("📞", contacts[name])
else:
    print(" Not found")
    for c in contacts:
        if name[0] == c[0]:
            print(" Maybe:", c, "-", contacts[c])
if input("Add new contact? (y/n): ").lower() == "y":
    n = input("Name: ").capitalize()
    num = int(input("Number: "))
    contacts[n] = num
print("\n Contacts:")
for k in sorted(contacts):
    print(k, ":", contacts[k])