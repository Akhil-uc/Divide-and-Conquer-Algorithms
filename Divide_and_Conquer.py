"""
Assignment 2: Divide-and-Conquer Algorithms
Student Name: Akhil Reddy Tekula
Student ID: 005043361
"""

import random
import time
import tracemalloc

# Merge Sort Algorithm
def merge_sort(numbers):
    """
    Sorts a list using the Merge Sort algorithm.

    The list is recursively divided into two halves until
    each sublist contains only one element. The sorted
    sublists are then merged back together in order.
    """

    # Base case: A list with 0 or 1 element is already sorted.
    if len(numbers) <= 1:
        return numbers

    # Divide the list into two halves.
    middle = len(numbers) // 2

    left_part = merge_sort(numbers[:middle])
    right_part = merge_sort(numbers[middle:])

    # Store the merged sorted elements.
    sorted_list = []

    left_start = 0
    left_end = len(left_part)

    right_start = 0
    right_end = len(right_part)

    # Compare elements from both halves and
    # add the smaller element to the result list.
    while left_start < left_end and right_start < right_end:

        if left_part[left_start] <= right_part[right_start]:
            sorted_list.append(left_part[left_start])
            left_start += 1
        else:
            sorted_list.append(right_part[right_start])
            right_start += 1

    # Add any remaining elements from the left half.
    while left_start < left_end:
        sorted_list.append(left_part[left_start])
        left_start += 1

    # Add any remaining elements from the right half.
    while right_start < right_end:
        sorted_list.append(right_part[right_start])
        right_start += 1

    return sorted_list

# Quick Sort Algorithm
def quick_sort(values):
    """
    Sorts a list using the Quick Sort algorithm.

    A pivot element is selected, and the remaining elements
    are divided into three groups:
    - smaller than the pivot
    - equal to the pivot
    - greater than the pivot

    The smaller and larger groups are recursively sorted.
    """

    # Base case: Lists with 0 or 1 element are already sorted.
    if len(values) <= 1:
        return values

    # Select the middle element as the pivot.
    pivot = values[len(values) // 2]

    smaller = []
    equal = []
    larger = []

    # Partition the elements relative to the pivot.
    for value in values:
        if value < pivot:
            smaller.append(value)
        elif value > pivot:
            larger.append(value)
        else:
            equal.append(value)

    # Recursively sort the partitions and combine them.
    return quick_sort(smaller) + equal + quick_sort(larger)


# Performance Measurement
def evaluate_sort(sort_algorithm, dataset):
    """
    Measures the execution time and peak memory usage
    of the given sorting algorithm.
    """

    # Start tracking memory usage.
    tracemalloc.start()

    # Record the start time.
    start_time = time.perf_counter()

    # Sort a copy of the dataset to preserve the original data.
    sort_algorithm(dataset.copy())

    # Record the end time.
    end_time = time.perf_counter()

    # Get the peak memory used during execution.
    _, peak_memory = tracemalloc.get_traced_memory()

    # Stop memory tracking.
    tracemalloc.stop()

    execution_time = end_time - start_time
    memory_used = peak_memory / 1024  # Convert bytes to KB

    return execution_time, memory_used

# Test Data Generation
def create_datasets(size):
    """
    Creates three datasets for performance testing:

    1. Ascending order
    2. Descending order
    3. Random values
    """

    ascending = list(range(size))

    descending = list(range(size, 0, -1))

    random_values = random.sample(range(size * 10), size)

    return {
        "Ascending": ascending,
        "Descending": descending,
        "Random": random_values
    }


# Main Program
def run():

    # Different input sizes used for comparison.
    input_sizes = [1000, 5000, 10000]

    print("=" * 80)
    print("MERGE SORT VS QUICK SORT PERFORMANCE COMPARISON")
    print("=" * 80)

    # Test each input size.
    for size in input_sizes:

        print(f"\nInput Size: {size}")

        # Generate datasets for the current size.
        datasets = create_datasets(size)

        # Evaluate both sorting algorithms on each dataset.
        for dataset_name, dataset in datasets.items():

            merge_time, merge_memory = evaluate_sort(
                merge_sort,
                dataset
            )

            quick_time, quick_memory = evaluate_sort(
                quick_sort,
                dataset
            )

            print(f"\nDataset Type: {dataset_name}")

            print(
                f"Merge Sort -> "
                f"Time: {merge_time:.6f} seconds | "
                f"Memory: {merge_memory:.2f} KB"
            )

            print(
                f"Quick Sort -> "
                f"Time: {quick_time:.6f} seconds | "
                f"Memory: {quick_memory:.2f} KB"
            )

# Program Entry Point
if __name__ == "__main__":
    run()
