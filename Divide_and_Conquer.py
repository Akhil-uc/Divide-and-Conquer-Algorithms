"""
Assignment 2: Divide-and-Conquer Algorithms
Student Name: Akhil Reddy Tekula
Student ID: 005043361
"""

import random
import time
import tracemalloc


#  Merge Sort 
def merge_sort(numbers):
    """Sort a list using the Merge Sort algorithm."""

    if len(numbers) <= 1:
        return numbers

    middle = len(numbers) // 2

    left_part = merge_sort(numbers[:middle])
    right_part = merge_sort(numbers[middle:])

    sorted_list = []

    left_start = 0
    left_end = len(left_part)

    right_start = 0
    right_end = len(right_part)

    while left_start < left_end and right_start < right_end:

        if left_part[left_start] <= right_part[right_start]:
            sorted_list.append(left_part[left_start])
            left_start += 1
        else:
            sorted_list.append(right_part[right_start])
            right_start += 1

    while left_start < left_end:
        sorted_list.append(left_part[left_start])
        left_start += 1

    while right_start < right_end:
        sorted_list.append(right_part[right_start])
        right_start += 1

    return sorted_list


#  Quick Sort 
def quick_sort(values):
    """Sort a list using the Quick Sort algorithm."""

    if len(values) <= 1:
        return values

    pivot = values[len(values) // 2]

    smaller = []
    equal = []
    larger = []

    for value in values:
        if value < pivot:
            smaller.append(value)
        elif value > pivot:
            larger.append(value)
        else:
            equal.append(value)

    return quick_sort(smaller) + equal + quick_sort(larger)


#  Performance Measurement 
def evaluate_sort(sort_algorithm, dataset):
    """Measure execution time and peak memory usage."""

    tracemalloc.start()

    start_time = time.perf_counter()

    sort_algorithm(dataset.copy())

    end_time = time.perf_counter()

    _, peak_memory = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    execution_time = end_time - start_time
    memory_used = peak_memory / 1024

    return execution_time, memory_used


#  Generate Test Data 
def create_datasets(size):
    """Generate sorted, reverse sorted, and random datasets."""

    ascending = list(range(size))

    descending = list(range(size, 0, -1))

    random_values = random.sample(range(size * 10), size)

    return {
        "Ascending": ascending,
        "Descending": descending,
        "Random": random_values
    }


#  Main Program 
def run():

    input_sizes = [1000, 5000, 10000]

    print("=" * 80)
    print("MERGE SORT VS QUICK SORT PERFORMANCE COMPARISON")
    print("=" * 80)

    for size in input_sizes:

        print(f"\nInput Size: {size}")

        datasets = create_datasets(size)

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


#  Program Entry 
if __name__ == "__main__":
    run()