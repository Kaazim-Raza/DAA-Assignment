from functions import generate_random_numbers, read_numbers_from_file, linear_search, binary_search, sort_numbers, is_sorted

if __name__ == "__main__":
    # Main menu
    print("Select an option:")
    print("1. Generate file with random numbers")
    print("2. Search for a number in a file")
    print("3. Sort numbers in a file")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        # Generate file
        amount = int(input("How many random whole numbers do you want to generate? "))
        time_taken, filename = generate_random_numbers(amount)
        print(f"File '{filename}' generated with {amount} random whole numbers.")
        print(f"Time taken: {time_taken:.5f} seconds.")
    
    elif choice == "2":
        # Search for a number in a file
        filename = input("Enter the filename to search in: ")
        target = int(input("Enter the number to search for: "))
        numbers = read_numbers_from_file(filename)
        if numbers is None:
            exit()

        print("Choose search algorithm:")
        print("1. Linear Search")
        print("2. Binary Search")
        search_choice = input("Enter your choice (1/2): ")

        if search_choice == "1":
            # Linear search
            line, time_taken = linear_search(numbers, target)
        elif search_choice == "2":
            # Binary search
            if not is_sorted(numbers):
                print("Please sort the file first.")
                exit()
            line, time_taken = binary_search(numbers, target)
        else:
            print("Invalid choice.")
            exit()

        if line == -1:
            print(f"Number {target} not found.")
        else:
            print(f"Number {target} found on line {line}.")
        print(f"Time taken: {time_taken:.5f} seconds.")

    elif choice == "3":
        # Sort numbers in a file
        filename = input("Enter the filename to sort: ")
        numbers = read_numbers_from_file(filename)
        if numbers is None:
            exit()

        print("Choose sorting order:")
        print("1. Ascending")
        print("2. Descending")
        sort_choice = input("Enter your choice (1/2): ")

        ascending = sort_choice == "1"
        sorted_numbers, time_taken = sort_numbers(numbers, ascending)

        # Overwrite the file with sorted numbers
        with open(filename, 'w') as file:
            for number in sorted_numbers:
                file.write(f"{number}\n")

        order = "ascending" if ascending else "descending"
        print(f"File '{filename}' sorted in {order} order.")
        print(f"Time taken: {time_taken:.5f} seconds.")

    else:
        print("Invalid choice.")
