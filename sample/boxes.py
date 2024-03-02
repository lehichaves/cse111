#CSE111
#Week 1
#Activity: Calling Functions

import math

number_items = int(input("Enter the number of items: "))
items_boxes = int(input("Enter the number of items per box: "))

number_box = math.ceil (number_items / items_boxes)

print()

print(f"For {number_items} items, packing {items_boxes} items in each box, you will need {number_box} boxes.")
