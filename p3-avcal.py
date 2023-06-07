print("Which one you want to calculate?  Area or Volumn \n")
print(" Give 1 for Area and other for Volumn " )

num= int(input("Enter a Number : "))

if num == 1 :
 length = float(input("Enter Length: "))
 weidth = float(input("Enter Weidth: "))

 area= length* weidth

 print(f"The area is : {area} cm^2")

else :
 length = float(input("Enter Length: "))
 height = float(input("Enter height: "))
 weidth = float(input("Enter Weidth: "))

 volume= length* weidth* height

 print(f"The volume is : {volume} cm^3")

