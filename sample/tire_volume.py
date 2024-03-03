#Name: Lehi Chaves
#CSE111 - Programming with functions
#Week 1
#Activity - Prove - Tire volume

from datetime import datetime

import math

#Date
current_date_and_time = datetime.now()

print(f"{current_date_and_time:%Y-%m-%d}")

print("This is the tires available: ")
print("185 / 50 / 14")
print("205 / 60 / 15")
print("175 / 65 / 16")
print("195 / 55 / 17")

prices_tires = {
    (185, 50, 14): 120, 
    (205, 60, 15): 140,
    (175, 65, 16): 160,
    (195, 55, 17): 180,
}
print()

while True:

#width tires
    width_tire_mm = float(input("Enter the width of tire in mm: "))
    
#Ratio Tire
    ratio_tire = float(input("Enter the aspect ratio od the tire: "))
    
#Diameter wheel
    diameter_wheel_in = float(input("Enter the diameter of the wheel in inches: "))
   
#Looking if is available the tire choosed
    tire_sizes = (int(width_tire_mm), int(ratio_tire), int(diameter_wheel_in))
    if tire_sizes in prices_tires:
        price = prices_tires[tire_sizes]
        print(f"This tire is ${price} dollars")
        break
    else:
        print()
        print("Price not available for this tire size, please start again!")
        print()



#Volume form
v = (math.pi * width_tire_mm**2 * ratio_tire * (width_tire_mm * ratio_tire + 2540 * diameter_wheel_in)) / 10000000000

print(f"The approximate volume is {v:.2f} liters")

print()

ask_costumer = input("Do you want to buy this tire? Yes/No ").lower()

if ask_costumer == "yes":
    ask_phone = input("What's your phone number to register? ")
    print("Thank you!")
elif ask_costumer == "no":
    print("Ok. Next week we will have more tires sizes, please looking again next week. See you! Have a good one!")
    quit()
else:
    print("Please, yes or no?")


#Opening volumes.txt
with open("volumes.txt", mode="at") as volumes_file:
    print(f"{current_date_and_time}, {width_tire_mm}, {ratio_tire}, {diameter_wheel_in}, {v:.2f}, {ask_phone}", file=volumes_file)