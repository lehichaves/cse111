def main():
        # Create and print a list named fruit.
        fruit_list = ["pear", "banana", "apple", "mango"]
        print(f"original: {fruit_list}")

        #Add code to reverse and print fruit_list.
        fruit_list.reverse()
        print(f"reverse: {fruit_list}")

        #Add code to append "orange" to the end of fruit_list and print the list.
        fruit_list.append("orange")
        print(f"added orange: {fruit_list}")

        #Add code to find where "apple" is located in fruit_list and insert "cherry" before "apple" in the list and print the list.
        i = fruit_list.index("apple")
        fruit_list.insert(i, "cherry")
        print(f"added cherry: {fruit_list}")

        #Add code to remove "banana" from fruit_list and print the list.
        fruit_list.remove("banana")
        print(f"remove banana: {fruit_list}")

        #Add code to pop the last element from fruit_list and print the popped element and the list.
        last = fruit_list.pop()
        print(f"fruit removed: {last}")

        #Add code to sort and print fruit_list.
        fruit_list.sort()
        print(fruit_list)

        #Add code to clear and print fruit_list.
        fruit_list.clear()
        print(fruit_list)


# Call main to start this program.
if __name__ == "__main__":
    main()