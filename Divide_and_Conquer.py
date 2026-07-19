"""
Assignment 2: Divide-and-Conquer Algorithms
Student Name: Akhil Reddy Tekula
Student ID: 005043361
"""

# Import the random module to generate random datasets.
import random

# Import the time module to measure execution time.
import time

# Import tracemalloc to measure peak memory usage.
import tracemalloc


# Define a function that sorts a list using the Merge Sort algorithm.
def merge_sort(numbers):

    # Check if the list contains one or zero elements.
    if len(numbers) <= 1:

        # Return the list because it is already sorted.
        return numbers

    # Calculate the middle index of the list.
    middle = len(numbers) // 2

    # Recursively sort the left half of the list.
    left_part = merge_sort(numbers[:middle])

    # Recursively sort the right half of the list.
    right_part = merge_sort(numbers[middle:])

    # Create an empty list to store the merged sorted values.
    sorted_list = []

    # Initialize the starting index for the left list.
    left_start = 0

    # Store the total number of elements in the left list.
    left_end = len(left_part)

    # Initialize the starting index for the right list.
    right_start = 0

    # Store the total number of elements in the right list.
    right_end = len(right_part)

    # Continue looping while both lists still contain unprocessed elements.
    while left_start < left_end and right_start < right_end:

        # Compare the current element from the left list with the current element from the right list.
        if left_part[left_start] <= right_part[right_start]:

            # Add the smaller element from the left list into the merged list.
            sorted_list.append(left_part[left_start])

            # Move to the next element in the left list.
            left_start += 1

        # Execute this block if the right element is smaller.
        else:

            # Add the smaller element from the right list into the merged list.
            sorted_list.append(right_part[right_start])

            # Move to the next element in the right list.
            right_start += 1

    # Continue until all remaining left-side elements are copied.
    while left_start < left_end:

        # Append the remaining left element.
        sorted_list.append(left_part[left_start])

        # Move to the next left element.
        left_start += 1

    # Continue until all remaining right-side elements are copied.
    while right_start < right_end:

        # Append the remaining right element.
        sorted_list.append(right_part[right_start])

        # Move to the next right element.
        right_start += 1

    # Return the fully merged and sorted list.
    return sorted_list
# Define a function that sorts a list using the Quick Sort algorithm.
def quick_sort(values):

    # Check if the list contains one or zero elements.
    if len(values) <= 1:

        # Return the list because it is already sorted.
        return values

    # Select the middle element of the list as the pivot.
    pivot = values[len(values) // 2]

    # Create a list to store elements smaller than the pivot.
    smaller = []

    # Create a list to store elements equal to the pivot.
    equal = []

    # Create a list to store elements larger than the pivot.
    larger = []

    # Loop through every element in the input list.
    for value in values:

        # Check whether the current element is smaller than the pivot.
        if value < pivot:

            # Add the element to the smaller list.
            smaller.append(value)

        # Check whether the current element is larger than the pivot.
        elif value > pivot:

            # Add the element to the larger list.
            larger.append(value)

        # Execute this block when the element is equal to the pivot.
        else:

            # Add the element to the equal list.
            equal.append(value)

    # Recursively sort the smaller and larger lists and combine the results.
    return quick_sort(smaller) + equal + quick_sort(larger)


# Define a function that measures the execution time and memory usage
# of a sorting algorithm.
def evaluate_sort(sort_algorithm, dataset):

    # Start tracking memory allocations.
    tracemalloc.start()

    # Record the current time before sorting begins.
    start_time = time.perf_counter()

    # Create a copy of the dataset and sort it so the original remains unchanged.
    sort_algorithm(dataset.copy())

    # Record the current time after sorting finishes.
    end_time = time.perf_counter()

    # Retrieve the current and peak memory usage.
    _, peak_memory = tracemalloc.get_traced_memory()

    # Stop tracking memory allocations.
    tracemalloc.stop()

    # Calculate the total execution time.
    execution_time = end_time - start_time

    # Convert memory usage from bytes to kilobytes.
    memory_used = peak_memory / 1024

    # Return both the execution time and memory usage.
    return execution_time, memory_used
# Define a function that creates different datasets for testing.
def create_datasets(size):

    # Create a list of numbers in ascending order starting from 0.
    ascending = list(range(size))

    # Create a list of numbers in descending order.
    descending = list(range(size, 0, -1))

    # Generate a list of unique random numbers.
    random_values = random.sample(range(size * 10), size)

    # Return all three datasets inside a dictionary.
    return {

        # Store the ascending dataset using the key "Ascending".
        "Ascending": ascending,

        # Store the descending dataset using the key "Descending".
        "Descending": descending,

        # Store the random dataset using the key "Random".
        "Random": random_values
# Define the main function that runs the performance comparison.
def run():

    # Create a list containing the input sizes to be tested.
    input_sizes = [1000, 5000, 10000]

    # Print a separator line for better readability.
    print("=" * 80)

    # Print the program title.
    print("MERGE SORT VS QUICK SORT PERFORMANCE COMPARISON")

    # Print another separator line.
    print("=" * 80)

    # Loop through each input size in the list.
    for size in input_sizes:

        # Display the current input size being tested.
        print(f"\nInput Size: {size}")

        # Generate the datasets for the current input size.
        datasets = create_datasets(size)

        # Loop through each dataset stored in the dictionary.
        for dataset_name, dataset in datasets.items():

            # Measure the execution time and memory usage of Merge Sort.
            merge_time, merge_memory = evaluate_sort(
                merge_sort,
                dataset
            )

            # Measure the execution time and memory usage of Quick Sort.
            quick_time, quick_memory = evaluate_sort(
                quick_sort,
                dataset
            )

            # Display the name of the current dataset.
            print(f"\nDataset Type: {dataset_name}")

            # Print the Merge Sort performance results.
            print(
                f"Merge Sort -> "
                f"Time: {merge_time:.6f} seconds | "
                f"Memory: {merge_memory:.2f} KB"
            )

            # Print the Quick Sort performance results.
            print(
                f"Quick Sort -> "
                f"Time: {quick_time:.6f} seconds | "
                f"Memory: {quick_memory:.2f} KB"
            )


# Check whether this file is being run directly.
if __name__ == "__main__":

    # Call the main function to start the program.
    run()
