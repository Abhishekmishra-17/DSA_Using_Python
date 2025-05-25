# Selection Sort in Python

This directory contains an implementation of the Selection Sort algorithm in Python, including both the standard and an optimized version. The code also measures and prints the time taken to sort the array.

## What is Selection Sort?
Selection Sort is a simple comparison-based sorting algorithm. It divides the input list into two parts: the sublist of items already sorted, and the sublist of items remaining to be sorted. It repeatedly selects the smallest (or largest) element from the unsorted sublist, swapping it with the leftmost unsorted element, and moving the sublist boundaries one element to the right.

## Flow Diagram (Mermaid)
```mermaid
flowchart TD
    A([Start]) --> B[Set i = 0]
    B --> C{Is i < n-1?}
    C -- No --> G([End])
    C -- Yes --> D[Set min_index = i]
    D --> E[For j = i+1 to n-1: If arr[j] < arr[min_index], set min_index = j]
    E --> F[Swap arr[i] and arr[min_index]]
    F --> H[Increment i]
    H --> C
```

## Features
- Standard Selection Sort (`Selection_Sort`)
- Optimized Selection Sort (`optimize_Selection_Sort`): Only swaps when necessary
- Time measurement for each sort

## Time and Space Complexity
| Version         | Best Case | Average Case | Worst Case | Space Complexity |
|----------------|-----------|--------------|------------|------------------|
| Standard       | O(n^2)    | O(n^2)       | O(n^2)     | O(1)             |
| Optimized      | O(n^2)    | O(n^2)       | O(n^2)     | O(1)             |

- n = number of elements in the array
- Both versions are in-place (no extra space)
- The optimized version reduces unnecessary swaps, which can improve performance on nearly sorted arrays, but does not change the overall time complexity

## Input/Output Examples

### Example 1: Standard Selection Sort
**Input:**
```python
arr = [64, 25, 12, 22, 11]
Selection_Sort(arr)
```
**Output:**
```
Selection Sort took X.XXXXXX seconds to sort 5 elements.
[11, 12, 22, 25, 64]
```

### Example 2: Optimized Selection Sort
**Input:**
```python
arr = [64, 25, 12, 22, 11]
optimize_Selection_Sort(arr)
```
**Output:**
```
Optimized Selection Sort took X.XXXXXX seconds to sort 5 elements.
[11, 12, 22, 25, 64]
```

### Example 3: Already Sorted Array
**Input:**
```python
arr = [1, 2, 3, 4, 5]
optimize_Selection_Sort(arr)
```
**Output:**
```
Optimized Selection Sort took X.XXXXXX seconds to sort 5 elements.
[1, 2, 3, 4, 5]
```

### Example 4: Empty Array
**Input:**
```python
arr = []
Selection_Sort(arr)
```
**Output:**
```
Selection Sort took X.XXXXXX seconds to sort 0 elements.
[]
```

## Edge Cases
- Empty array (should return empty array)
- Array with one element (should return the same array)
- Array with all elements equal (should return the same array)
- Already sorted array (optimized version avoids unnecessary swaps)
- Array sorted in reverse order (worst case for swaps)

## How to Run
1. Make sure you have Python 3 installed.
2. Run the script:
   ```sh
   python Selection_Sort.py
   ```
3. The script will sort a large array and print the time taken for both standard and optimized selection sort.

## File Location
`Sorting Algorithm/Selection_Sort/Selection_Sort.py`

## Author
- Implementation by [Abhishekmishra-17]

---
For more sorting algorithms, see the parent directory.
