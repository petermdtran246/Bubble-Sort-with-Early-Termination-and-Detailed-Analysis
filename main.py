def bubble_sort_ascending(arr):
    """
    Sorts an array in ascending order using the bubble sort algorithm with early termination.

    :parameter
        arr: The input array to be sorted.
    """
    n = len(arr)
    total_comparisons = 0
    total_swaps = 0

    for k in range(n):
        # Initialize counters for comparisons and swaps in the iteration
        comparisons = 0
        swaps = 0
        swapped = False

        # Inner loop to compare and swap adjacent elements
        for i in range(0, n - 1 - k):  # Last k elements are already sorted
            comparisons += 1  # Count comparisons for this iteration
            total_comparisons += 1  # Update total comparisons
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]  # Swap elements
                swaps += 1  # Count swaps for this iteration
                total_swaps += 1  # Update total swaps
                swapped = True

        # Print results after each outer loop iteration
        print(f'After iteration {k + 1}:')
        print(f'Partially sorted array: {arr}')
        print(f'Number of comparisons on this iteration: {comparisons}')
        print(f'Number of swaps on this iteration: {swaps}')
        print('-' * 80)

        # Check for early termination
        if not swapped:
            print('The array is sorted.')
            break

    # Print final results
    print()
    print(f'Total comparisons: {total_comparisons}')
    print(f'Total swaps: {total_swaps}')

# Problem instances
A4 = [44, 63, 77, 17, 20, 99, 84, 6, 39, 52]
A5 = [52, 84, 6, 39, 20, 77, 17, 99, 44, 63]
A6 = [6, 17, 20, 39, 44, 52, 63, 77, 84, 99]

print('Sorting A4: ')
bubble_sort_ascending(A4)
print('*' * 80)
print('Sorting A5:')
bubble_sort_ascending(A5)
print('*' * 80)
print('Sorting A6: ')
bubble_sort_ascending(A6)

