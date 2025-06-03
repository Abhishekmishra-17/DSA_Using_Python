# initialize the size of array, check the datatype of data, 
# append the data, insert the data at index a, 
# delete a data from array from beg, delete data from ending, 
# delete data from index a, searching,
# sorting (ascending/descending), travesring,

class Array:

    def __init__(self, r_size=1, c_size=1, dtype=int, data=[], major = "row"):
        self.r_size = r_size
        self.c_size = c_size
        self.dtype = dtype
        self.data = data
        self.major = major
    
    def create(self):
        if self.r_size <= 0 or self.c_size <= 0:
            raise ValueError("Row and column sizes must be greater than zero.")
        elif len(self.data) != self.r_size * self.c_size:
            raise ValueError("Data length must match the product of row and column sizes.")
        if not all(isinstance(x, self.dtype) for x in self.data):
                raise TypeError(f"All elements must be of type {self.dtype}.")
        else:
            try:
                if self.dtype in [int, float, str]:
                    self.data = [self.dtype(x) for x in self.data]
                else:
                    raise TypeError("Unsupported data type. Use 'int', 'float', or 'str'.")
            except ValueError as e:
                raise ValueError(f"Data conversion error: {e}")
            except TypeError as e:
                raise TypeError(f"Data type error: {e}")
            if self.major == "row":
                return [self.data[i:i + self.c_size] for i in range(0, len(self.data), self.c_size)]
            elif self.major == "column":
                return [[self.data[i + j * self.r_size] for j in range(self.c_size)] for i in range(self.r_size)]
            else:
                raise ValueError("Major must be either 'row' or 'column'.")



if __name__ == "__main__":
    arr = Array(c_size=6, dtype=int, data=[1, 2, 3, 4, 5, 6], major="row")
    matrix = arr.create()
    for row in matrix:
        print(*row)
    
    arr_col = Array(r_size=3, c_size=2, dtype=float,data=[1.1, 2.2, 3.3, 4.4, 5.5, 6.0], major="column")
    matrix_col = arr_col.create()
    for col in matrix_col:
        print(*col)
