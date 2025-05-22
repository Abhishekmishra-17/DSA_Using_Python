# Question 1: Write a python code which merges two sorted array into a single sorted array.

def merge_sorted_arrays(arr1, arr2):
    """
    Merges two sorted arrays into a single sorted array.

    Parameters:
    arr1 (list): First sorted array.
    arr2 (list): Second sorted array.

    Returns:
    list: Merged sorted array.
    """
    merged_array = []
    i, j = 0, 0

    # Traverse both arrays and merge them
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    # Append remaining elements of arr1
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1

    # Append remaining elements of arr2
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1

    return merged_array

# using for loop
def merge_sorted_arrays(arr1, arr2):
    """
    Merges two sorted arrays into a single sorted array.

    Parameters:
    arr1 (list): First sorted array.
    arr2 (list): Second sorted array.

    Returns:
    list: Merged sorted array.
    """
    merged_array = []
    i, j = 0, 0

    # Traverse both arrays and merge them
    for i in range(len(arr1)):
        merged_array.append(arr1[i])
    
    for j in range(len(arr2)):
        merged_array.append(arr2[j])

    return sorted(merged_array) # without using sorted  and sort function

# using while loop
def merge_sorted_arrays(arr1, arr2):
    """
    Merges two sorted arrays into a single sorted array.

    Parameters:
    arr1 (list): First sorted array.
    arr2 (list): Second sorted array.

    Returns:
    list: Merged sorted array.
    """
    merged_array = []
    i, j = 0, 0

    # Traverse both arrays and merge them
    while i < len(arr1) or j < len(arr2):
        if i < len(arr1) and (j >= len(arr2) or arr1[i] <= arr2[j]):
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    return merged_array