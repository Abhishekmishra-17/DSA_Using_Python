def binary_search(item, e_index, s_index = 0, data_list: list=[], prev_partition = 0) -> int:
    if not data_list:
        print("Given data list is empty")
        return False
    else:
        partition = (s_index+e_index)//2
        print(partition)
        if prev_partition == partition and data_list [partition] == item:
            print(f"{item} found at index {partition}")
        elif prev_partition == partition and data_list[partition]!=item:
            print("Given item is not present in the list")
        elif data_list[partition] == item:
            print(f"{item} found at index {partition}")
            return True
        elif item > data_list[partition]:
            binary_search(item,e_index, partition+1, data_list, partition)
        else:
            binary_search(item,partition,0, data_list, partition)

array = [100,1,2,5,6,7,89,9,3]
array.sort()
binary_search(100, len(array)-1, 0, data_list=array)