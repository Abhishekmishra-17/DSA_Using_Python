# Linear and Binary Search Algorithms

This module implements both Linear Search and Binary Search algorithms in Python.

## Definitions

- **Linear Search:**
  Linear Search is a simple searching algorithm that checks every element in a list sequentially until the desired element is found or the list ends. It does not require the list to be sorted.

- **Binary Search:**
  Binary Search is an efficient searching algorithm that works on sorted lists. It repeatedly divides the search interval in half, comparing the target value to the middle element, and discards the half in which the target cannot lie.

## Uses

- **Linear Search:**
  - Useful for small or unsorted datasets.
  - Can be used when the list is not sorted or when only a single/few searches are needed.
  - Suitable for searching in linked lists, arrays, or any iterable.

- **Binary Search:**
  - Best for large, sorted datasets where search speed is important.
  - Commonly used in searching databases, dictionaries, and sorted arrays.
  - Used in libraries and frameworks for fast lookup operations.

## Difference Between Linear Search and Binary Search

| Feature                | Linear Search                        | Binary Search                        |
|------------------------|--------------------------------------|--------------------------------------|
| List Requirement       | Works on unsorted or sorted lists    | Requires sorted list                 |
| Time Complexity        | O(n)                                 | O(log n)                             |
| Space Complexity       | O(1)                                 | O(log n) (recursive) or O(1) (iter.) |
| Approach               | Sequential, checks every element     | Divide and conquer, halves each time |
| Implementation         | Simple, easy to implement            | Slightly more complex                |
| Use Case               | Small/unsorted data, few searches    | Large/sorted data, frequent searches |
| Efficiency             | Less efficient for large datasets    | Very efficient for large datasets    |

## Functions

### 1. `linear_search_single(data_list: list, item) -> bool`
- **Description:** Searches for the first occurrence of `item` in `data_list`. Prints the index if found, otherwise prints not found.
- **Time Complexity:** O(n), where n is the length of the list.
- **Space Complexity:** O(1)

### 2. `linear_search_multiple(data_list: list, item) -> list | bool`
- **Description:** Searches for all occurrences of `item` in `data_list`. Returns a list of indices if found, otherwise prints not found.
- **Time Complexity:** O(n)
- **Space Complexity:** O(k), where k is the number of occurrences of `item`.

### 3. `binary_search(item, e_index, s_index=0, data_list=[], prev_partition=0) -> int`
- **Description:** Searches for `item` in a sorted `data_list` using the binary search algorithm. Prints the index if found, otherwise prints not found.
- **Time Complexity:** O(log n), where n is the length of the list.
- **Space Complexity:** O(log n) due to recursion stack.

## Flow Diagrams

### Linear Search
```mermaid
graph TD;
    A[Start] --> B{Is data_list empty?}
    B -- Yes --> C[Print "Given data list is empty" and return False]
    B -- No --> D[Set i = 0]
    D --> E{Is i < length of data_list?}
    E -- No --> F[Print "item not found" and return False]
    E -- Yes --> G{Is data_list[i] == item?}
    G -- Yes --> H[Print "item found at index i" and return True (or add i to index_list for multiple search)]
    G -- No --> I[Increment i by 1]
    I --> E
```

### Binary Search
```mermaid
graph TD;
    A[Start] --> B{Is data_list empty?}
    B -- Yes --> C[Print "Given data list is empty" and return False]
    B -- No --> D[Set partition = (s_index + e_index) // 2]
    D --> E{Is data_list[partition] == item?}
    E -- Yes --> F[Print "item found at index partition" and return True]
    E -- No --> G{Is s_index >= e_index?}
    G -- Yes --> H[Print "item not found" and return False]
    G -- No --> I{Is item > data_list[partition]?}
    I -- Yes --> J[Set s_index = partition + 1, repeat search]
    I -- No --> K[Set e_index = partition - 1, repeat search]
```

## Example Usage

```python
from Linear_Search import linear_search_single, linear_search_multiple
from Binary_Search import binary_search

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
item_to_search = 5
linear_search_single(data, item_to_search)

# For multiple occurrences
result = linear_search_multiple([1, 2, 3, 4, 5, 6, 7, 8, 9, 5], 5)
if result:
    print(f"5 found at indices: {result}")

# Binary Search Example
array = [100, 1, 2, 5, 6, 7, 89, 9, 3]
array.sort()
binary_search(100, len(array)-1, 0, data_list=array)
```

## References
- [Wikipedia: Linear Search](https://en.wikipedia.org/wiki/Linear_search)
- [GeeksforGeeks: Linear Search](https://www.geeksforgeeks.org/linear-search/)
- [Wikipedia: Binary Search](https://en.wikipedia.org/wiki/Binary_search_algorithm)
- [GeeksforGeeks: Binary Search](https://www.geeksforgeeks.org/binary-search/)
