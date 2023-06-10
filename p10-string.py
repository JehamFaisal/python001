# name= input("Enter youyr name: ")

# result= len(name)
# result= name.find(" ")
# result= name.rfind(" ")

# name= name.capitalize()
# name= name.lower()
# result= name.isalpha()
# result= name.isdigit()
# result= phone_number.count("-")
# phone_number = phone_number.replace("-","")
# print(help(str))
# print(result)

# validate user input exercise

# 1. User name is no more than 12 charecter
# 2. Username must not contain spaces
# 3. user name must not contain digits


username = (input("Enter your username: "))

if len(username) > 12:
    print("Your username can't more than 12 characters")
elif not username.find(" ")==-1:
    print("Your user name can't contain spaces")
elif not username.isalpha():
    print ("Your user name can't contain numbers")
else:
    print(username)
