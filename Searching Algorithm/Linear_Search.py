def linear_search_single(data_list: list, item) -> bool:
    length = len(data_list)
    if length == 0:
        print("Given data list is empty")
        return False
    else:
        for i in range(length):
            if data_list[i] == item:
                print(f"{item} found at index {i}")
                return True
        print(f"{item} not found")
        return False


def linear_search_multiple(data_list: list, item) -> list | bool:
    length = len(data_list)
    index_list = []
    if length == 0:
        print("Given data list is empty")
        return False
    else:
        for i in range(length):
            if data_list[i] == item:
                index_list.append(i)
        if index_list:
            return index_list
        else:
            print(f"{item} not found")
            return False


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    item_to_search = 5
    linear_search_single(data, item_to_search)

    data_multiple = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
    item_to_search_multiple = 5
    result = linear_search_multiple(data_multiple, item_to_search_multiple)
    if result:
        print(f"{item_to_search_multiple} found at indices: {result}")