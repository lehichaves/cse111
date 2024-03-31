import csv

def main ():

    key_INDEX = 0

    products_dict = read_dictionary("products.csv", key_INDEX)
    print("All Products")
    print(products_dict)

    requested_items = {}
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
                price = product_key[2]
                requested_items[product_name] = f"{quantity_product} @ {price}"

    print("Requested Items")
    for item, quantity in requested_items.items():
        print(f"{item}: {quantity}")
    
  
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