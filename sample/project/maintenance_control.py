#Name: Lehi Chaves
#CSE111 - Programming with functions
#Week 7
#W07 Project

"""To run the program you need to put the all files 
in a folder called 'project', because my program
is pulling the csv files with this folder name"""

import csv
from datetime import datetime

current_date_and_time = datetime.now()

def main ():

    print(f"{current_date_and_time:%a %b %d %I:%M:%S %p %Y}")
    print()

    #How many Preventive are done?
    preventive = "preventive.csv"
    total_preventive_done = PM_orders_closed(preventive)
    print(f"{total_preventive_done} preventive orders maintenance are done.")

    #How many Preventive are opened?
    total_preventive_opened = PM_orders_opened(preventive)
    print(f"{total_preventive_opened} preventive orders maintenance are opened.")

    #How many corrective orders are opened?
    corrective = "corrective.csv"
    total_corrective_opened = AM_orders_opened(corrective)
    print(f"{total_corrective_opened} corrective orders need to be done")

    print()

    #How many orders total?
    total_orders_maintanance = total_corrective_opened + total_preventive_done + total_preventive_opened
    print(f"{total_orders_maintanance} maintenance orders was opened in the system.")
    print()

    #How many was done?
    total_orders_done = total_preventive_done
    print(f"{total_orders_done} maintenance orders was done."),
    print()

    #How many orders need to be done?
    total_orders = total_preventive_opened + total_corrective_opened
    print(f"{total_orders} maintenance orders need to be done.")
    print()


def PM_orders_closed(preventive):

    total_preventive_done = 0
    
    with open("project/preventive.csv", "rt") as preventive_orders:

        reader = csv.reader(preventive_orders)
        next(reader)
        for list_preventive in reader:
            preventive_done = list_preventive[3].strip().lower().count("yes")
            total_preventive_done += preventive_done

    return total_preventive_done


def PM_orders_opened(preventive):

    total_preventive_opened = 0
    
    with open("project/preventive.csv", "rt") as preventive_orders:

        reader = csv.reader(preventive_orders)
        next(reader)
        for list_preventive in reader:
            preventive_opened = list_preventive[3].strip().lower().count("no")
            total_preventive_opened += preventive_opened

    return total_preventive_opened


def AM_orders_opened(corrective):

    total_corrective_opened = 0
    
    with open("project/corrective.csv", "rt") as corrective_orders:

        reader = csv.reader(corrective_orders)
        next(reader)
        for list_corrective in reader:
            corrective_opened = list_corrective[3].strip().lower().count("no")
            total_corrective_opened += corrective_opened
        
    return total_corrective_opened


# Call main to start this program.
if __name__ == "__main__":
    main()