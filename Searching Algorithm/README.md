# Linear Search Algorithm

This module implements the Linear Search algorithm in Python, providing two main functions:
- `linear_search_single`: Finds the first occurrence of an item in a list.
- `linear_search_multiple`: Finds all occurrences of an item in a list.

## Functions

### 1. `linear_search_single(data_list: list, item) -> bool`
- **Description:** Searches for the first occurrence of `item` in `data_list`. Prints the index if found, otherwise prints not found.
- **Time Complexity:** O(n), where n is the length of the list.
- **Space Complexity:** O(1)

### 2. `linear_search_multiple(data_list: list, item) -> list | bool`
- **Description:** Searches for all occurrences of `item` in `data_list`. Returns a list of indices if found, otherwise prints not found.
- **Time Complexity:** O(n)
- **Space Complexity:** O(k), where k is the number of occurrences of `item`.

## Flow Diagram

Below is a simple flow diagram for the linear search process:

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

## Example Usage

```python
from Linear_Search import linear_search_single, linear_search_multiple

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
item_to_search = 5
linear_search_single(data, item_to_search)

# For multiple occurrences
result = linear_search_multiple([1, 2, 3, 4, 5, 6, 7, 8, 9, 5], 5)
if result:
    print(f"5 found at indices: {result}")
```

## References
- [Wikipedia: Linear Search](https://en.wikipedia.org/wiki/Linear_search)
- [GeeksforGeeks: Linear Search](https://www.geeksforgeeks.org/linear-search/)
