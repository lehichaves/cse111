#Name: Lehi Chaves
#CSE111 - Programming with functions
#Week 5
#W05 Prove Assignment: Grocery Store

import csv
from datetime import datetime

current_date_and_time = datetime.now()

def main ():

    try:        

        name_store = "Inkom Emporium"
        print(name_store)
        print()

        key_INDEX = 0

        products_dict = read_dictionary("products.csv", key_INDEX)
        
        requested_items = {}
        total = 0
        items_total = 0

        with open("week5/request.csv", "rt") as request_file:

            PRODUCT_NUMBER = 0
            QUANTITY_PRODUCT = 1

            reader = csv.reader(request_file)
            next(reader)

            for row_list in reader:
                product_number = row_list[PRODUCT_NUMBER]
                quantity_product = int(row_list[QUANTITY_PRODUCT])
                
                if product_number in products_dict:
                    product_key = products_dict[product_number]
                    product_name = product_key[1]
                    price = float(product_key[2])

                    price_total = price * quantity_product
                    total += price_total

                    requested_items[product_name] = f"{quantity_product} @ {price}"
                    items_total += quantity_product
                else:                    
                    raise KeyError(product_number)

        for item, quantity in requested_items.items():
            print(f"{item}: {quantity}")
        
        sales_tax = 0.06
        sales_tax_amount = total * sales_tax

        total_total = sales_tax_amount + total

        print()
        print(f"Number of Items = {items_total}")
        print(f"SubTotal: {total:.2f}")
        print(f"Sales Tax {sales_tax_amount:.2f}")
        print(f"Total: {total_total:.2f}")

        print("Thank you for shopping at the Inkom Emporium.")
        print()
        print(f"{current_date_and_time:%a %b %d %I:%M:%S %p %Y}")

    except FileNotFoundError:
        print("Error: missing file")
        print("[Errno 2] No such file or directory: 'products.csv'")        
    except PermissionError:
        print("Error: Permission denied to access the file.")
    except KeyError as e:
        print(f"Error: unknown product ID in the request.csv file '{e.args[0]}'")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
  
  
def read_dictionary (products, key_column_index):
    dictionary = {}
    with open("week5/products.csv", "rt") as csv_file:

        reader = csv.reader(csv_file)

        next(reader)

        for row_list in reader:

            if len(row_list) != 0:

                key = row_list[key_column_index]

                dictionary[key] = row_list

    return dictionary


# Call main to start this program.
if __name__ == "__main__":
    main()