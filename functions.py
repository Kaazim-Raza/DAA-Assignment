import random
import time
import os

# Function to generate random numbers and write to a file
def generate_random_numbers(amount):
    start_time = time.time()  # Start timing

    filename = f"File_{amount}.txt"  # Set the filename dynamically

    if os.path.exists(filename):
        print(f"File '{filename}' already exists and will be replaced.")

    # Open the file in write mode (overwrite the file if it exists)
    with open(filename, 'w') as file:
        for _ in range(amount):
            number = random.randint(1, 100)  # Generate random number between 1 and 100
            file.write(f"{number}\n")  # Write each number on a new line

    end_time = time.time()  # End timing
    time_taken = end_time - start_time  # Calculate time taken
    return time_taken, filename

# Function to read numbers from a file
def read_numbers_from_file(filename):
    if not os.path.exists(filename):
        print(f"File '{filename}' does not exist.")
        return None
    
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

# Check if the list is sorted
def is_sorted(numbers):
    return all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))

# Linear search function
def linear_search(numbers, target):
    start_time = time.time()
    for index, number in enumerate(numbers):
        if number == target:
            time_taken = time.time() - start_time
            return index + 1, time_taken  # Line number is index + 1
    time_taken = time.time() - start_time
    return -1, time_taken  # Not found

# Binary search function
def binary_search(numbers, target):
    start_time = time.time()
    low, high = 0, len(numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == target:
            time_taken = time.time() - start_time
            return mid + 1, time_taken  # Line number is mid + 1
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    time_taken = time.time() - start_time
    return -1, time_taken  # Not found

# Function to sort numbers
def sort_numbers(numbers, ascending=True):
    start_time = time.time()
    numbers.sort(reverse=not ascending)  # Sort in ascending or descending order
    time_taken = time.time() - start_time
    return numbers, time_taken
