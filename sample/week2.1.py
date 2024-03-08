import math

def main():
    odometer_start = float(input("Enter the starting odometer in miles: "))
    odometer_end = float(input("Enther the endind odometer in miles: "))
    amount_fuel = float(input("Enter amout fuel in gallons: "))

    mpg = (odometer_end - odometer_start) / amount_fuel
    lp100k = 235.215 / mpg

    print(f"{mpg:.2f} miles per gallon")
    print(f"{lp100k:.2f} liters per kilometers")

def miles_per_gallon(odometer_start, odometer_end, amount_fuel):
    
    mpg = (odometer_end - odometer_start) / amount_fuel
    return mpg


def lp100k_from_mpg(mpg):
    
    lp100k = 235.215 / mpg
    return lp100k

main()

