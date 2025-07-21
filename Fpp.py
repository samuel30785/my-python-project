# temperature conversion, i will begin by knowing what the current unit of measurement is
unit= input("Is this temperature in celcious or fehrenheit(C/F):")
temp=float(input("Enter the temperature:"))   #casting our temp input as a floating number

if unit=="c":
    temp= round((9*temp)/5+32, 1)               #converting celcious to fehrenhite and rounding result to one decimal place
    print(f"The temperature in ferenheite is: {temp}°F)")
else:
    if unit=="F":
        temp = round((temp-32)*5/9, 1)            #converting ferenheite to celcious and rounding result to one decimal place
        print(f"The temperature in celcious is: {temp}°C")
    else:
        print(f"{unit} is an invalid unit of measurement")

