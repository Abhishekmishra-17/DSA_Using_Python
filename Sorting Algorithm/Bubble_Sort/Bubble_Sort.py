import time

def Bubble_Sort(arr: list[int]) -> list[int]:
    """
    Bubble Sort Algorithm
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    # Start the timer
    start_time = time.time()
    length = len(arr)
    for i in range(length):
        for j in range(length-1, i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    # Stop the timer
    end_time = time.time()
    # Print the elapsed time
    print(f"Time taken by Bubble Sort: {end_time - start_time} seconds")
    return arr

def optimize_Bubble_Sort(arr: list[int]) -> list[int]:
    """
    Optimized Bubble Sort Algorithm
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    # Start the timer
    start_time = time.time()
    # Optimized Bubble Sort
    length = len(arr)
    for i in range(length):
        swapped = False
        for j in range(length-1, i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                swapped = True
        if not swapped:
            break
    # Stop the timer
    end_time = time.time()
    # Print the elapsed time
    print(f"Time taken by Optimized Bubble Sort: {end_time - start_time} seconds")
    # Return the sorted array
    return arr

if __name__ == "__main__":
    # Test the Bubble Sort Algorithm
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted array:", arr)
    sorted_arr = Bubble_Sort(arr)
    print("Sorted array using Bubble Sort:", sorted_arr)
    sorted_arr = optimize_Bubble_Sort(arr)
    print("Sorted array using Optimized Bubble Sort:", sorted_arr)

    