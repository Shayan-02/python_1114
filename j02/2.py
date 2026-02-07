firstName = "ali"
lastname = "rezaee"
age = 25

print("------------ normal --------------")

print("Your first name is", firstName, "\nyour last name is", lastname,"\nSo your full name is", firstName, lastname, "\nYour age is", age, "years old.")

print("------------ fstring --------------")

print(f"Your first name is {firstName} \nyour last name is {lastname} \nSo your full name is {firstName} {lastname} \nYour age is {age} years old.")

print("------------ format --------------")
print("Your first name is {} \nyour last name is {} \nSo your full name is {} {} \nYour age is {} years old.".format(firstName, lastname, firstName, lastname, age))