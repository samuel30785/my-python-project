#weight converter, we begin by creating the weight variable
weight= float(input("Enter your weight"))
unit= input("kilograms or pounds? (K or L):")

if unit=="K":  #being true
    weight= weight * 2.205
    unit= "lbs"
else: 
    if unit=="L":
        weight=weight/2.205
        unit="Kgs" 
    else:
      print(f"{unit} was not valid") # if i insert a variable not valid or supported e.g pizza

print(f"Your weight is: {round(weight)} {unit}")
