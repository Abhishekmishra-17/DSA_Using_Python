import time

def Selection_Sort(arr: list[int]) -> list[int]:
    """
    Selection Sort Algorithm
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    # Start the timer
    start_time = time.time()
    length = len(arr)
    for i in range(length):
        min_index = i
        for j in range(i+1, length):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    # Stop the timer
    end_time = time.time()
    # Print the elapsed time
    print(f"Selection Sort took {end_time - start_time} seconds to sort {length} elements.")
    # Return the sorted array
    return arr

def optimize_Selection_Sort(arr: list[int]) -> list[int]:
    """
    Optimized Selection Sort Algorithm
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    # Start the timer
    start_time = time.time()
    length = len(arr)
    for i in range(length):
        min_index = i
        for j in range(i+1, length):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    # This optimization checks if a swap is necessary before performing it
    # This can save time in cases where the array is already sorted or nearly sorted
    
    # Stop the timer
    end_time = time.time()
    # Print the elapsed time
    print(f"Optimized Selection Sort took {end_time - start_time} seconds to sort {length} elements.")
    # Return the sorted array
    return arr

if __name__ == "__main__":
    arr =[i for i in range(10000, 0, -1)]
    # print("Unsorted array:", arr)
    sorted_arr = Selection_Sort(arr)
    # print("Sorted array:", sorted_arr)
    sorted_arr = optimize_Selection_Sort(arr)
    # print("Sorted array using Optimized Selection Sort:", sorted_arr)