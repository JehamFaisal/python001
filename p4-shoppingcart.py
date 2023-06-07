item = input("What item would you like to buy? : ")
price =  float(input("What is/are the price?  ;"))
quantity= int(input("How many items? : "))

total= price*quantity

print(f"You have bought {quantity} X {item}/s\n")
print(f"Total Price is : ${round(total,2)}")