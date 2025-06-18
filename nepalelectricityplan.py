print("Welcome to the Nepal Electricity Assotiation.")
print("What was your monthly number of units?")
units = float(input("Enter the number of units of electricity"))

if units <= 20:
    total_amount=100
elif units <=50:
    total_amount=100+(units*6)
elif units <=100:
    total_amount=100+(units*8)
else units 
