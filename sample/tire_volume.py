#CSE111 - Programming with functions
#Week !
#Activity - Tire volume

import math

width_tire_mm = float(input("Enter the width of tire in mm: "))
ratio_tire = float(input("Enter the aspect ratio od the tire: "))
diameter_wheel_in = float(input("Enter the diameter of the wheel in inches: "))

#Volume form
v = (math.pi * width_tire_mm**2 * ratio_tire * (width_tire_mm * ratio_tire + 2540 * diameter_wheel_in)) / 10000000000

print(f"The approximate volume is {v:.2f} liters")

