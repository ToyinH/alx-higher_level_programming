#!/usr/bin/python3
"""
a function that finds a peak in a list of unsorted integers
"""
def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
    - list_of_integers: List of unsorted integers.

    Returns:
    - The peak element in the list.
    """

    # Get the length of the list
    n = len(list_of_integers)

    # Base case: if the list is empty, return None
    if n == 0:
        return None

    # Binary search-like algorithm to find a peak
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2

        # Compare mid element with its neighbors
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # Move towards the left side
            right = mid
        else:
            # Move towards the right side
            left = mid + 1

    # The peak is found at index 'left'
    return list_of_integers[left]
