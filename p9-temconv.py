temp = float(input("Enter the tempareture: "))
unit = input("Is this tempareture in Celsius or Fahrenheit (C/F): ")




if unit == "C":
    temp = round((9*temp)/5 +32,1)
    print(f"The temperature in Farenheit is: {round(temp,2)}°F")
elif unit == "F":
    temp = ((temp-32) *5/9)
    print(f"The temperature in Celsius is: {round(temp,2)}°C")
    
else:
   print(f"{unit} is an invalid unit of measurement")
