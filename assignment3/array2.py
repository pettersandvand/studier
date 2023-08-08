class Array:

    def __init__(self, shape, *values):
        """

        Initialize an array of 1-dimensionality. Elements can only be of type:
        - int
        - float
        - bool

        Make sure that you check that your array actually is an array, which means it is homogeneous (one data type).
        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either numeric or boolean.
        Raises:
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """
        num_val = 1
        for i in shape:
            if i > 1:
                num_val = num_val * i
        if sum(shape) == len(shape):
            num_val = len(shape)
        if num_val != len(values):
            raise ValueError("The shape does not match number of values passed.")

        shape_counter = 0
        value_index = 0
        temp = []
        if len(shape) > 1:
            for i in shape:
                temp3 = []
                while shape_counter < i:
                    if isinstance(values[value_index], type(values[0])):
                        temp3.append(values[value_index])
                    else:
                        raise TypeError("Not all values has the same type")
                    value_index += 1
                    shape_counter += 1
                temp.append(temp3)
                shape_counter = 0
        else:
            for el in values:
                temp.append(el)


        self.array = temp
        self.len = len(self.array)
        self.shape = shape

        # Optional: If not all values are of same type, all are converted to floats.

    def __getitem__(self, item):
        """ Returns value of item in array .
            Args :
                item ( int): Index of value to return ., or array whit int to target element in multi dimentional array.
            Returns :
                value : Value of the given item .
        """
        return self.array[item]

    def __str__(self):
        """Returns a nicely printable string representation of the array.
        Returns:
            str: A string representation of the array.
        """
        return str(self.array)

    def __add__(self, other):
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """
        temp = []
        a = self.flat_array()

        if type(other) == Array and self.shape == other.shape:
            b = other.flat_array()
            if self.shape == other.shape:
                for i in range(0, len(a)):
                    temp.append(a[i] + b[i])
                return Array(self.shape, *temp)

        elif type(other) == float or type(other) == int:
            for i in range(0, len(a)):
                temp.append(a[i] + other)
            return Array(self.shape, *temp)

        else:
            print("NotImplemented")

    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """
        try:
            return other + self
        except:
            print("NotImplemented")

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.
        Returns:
            Array: the difference as a new array.
        """
        temp = []
        a = self.flat_array()

        if type(other) == Array and self.shape == other.shape:
            b = other.flat_array()
            if self.shape == other.shape:
                for i in range(0, len(a)):
                    temp.append(a[i] - b[i])
                return Array(self.shape, *temp)

        elif type(other) == float or type(other) == int:
            for i in range(0, len(a)):
                temp.append(a[i] - other)
            return Array(self.shape, *temp)

        else:
            print("NotImplemented")

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number being subtracted from.
        Returns:
            Array: the difference as a new array.
        """
        try:
            return other - self
        except:
            print("NotImplemented")

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        temp = []
        a = self.flat_array()

        if type(other) == Array and self.shape == other.shape:
            b = other.flat_array()
            if self.shape == other.shape:
                for i in range(0, len(a)):
                    temp.append(a[i] * b[i])
                return Array(self.shape, *temp)

        elif type(other) == float or type(other) == int:
            for i in range(0, len(a)):
                temp.append(a[i] * other)
            return Array(self.shape, *temp)

        else:
            print("NotImplemented")

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        # Hint: this solution/logic applies for all r-methods
        try:
            return other * self
        except:
            print("NotImplemented")

    def __eq__(self, other):
        """Compares an Array with another Array.
        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.
        Args:
            other (Array): The array to compare with this array.
        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.
        """
        if len(self.array) == len(other.array):
            for i in range(0, len(self.array)):
                if self.array[i] != other.array[i]:
                    return False
            return True
        else:
            return False

    def flat_array(self):
        """Flattens the N- dimensional array of values into a 1-
        dimensional array .
        Returns :
        list : flat list of array values .
        """
        flat_array = []
        if isinstance(self.array[0], list):
            for sublist in self.array:
                for item in sublist:
                    flat_array.append(item)
            return flat_array
        else:
            return self.array

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.
        If `other` is an array and the two array shapes do not match, this method should raise ValueError.
        If `other` is not an array or a number, it should return TypeError.
        Args:
            other (Array, float, int): The array or number to compare with this array.
        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.
        Raises:
            ValueError: if the shape of self and other are not equal.
            TypeError: if array type of other is not numbers
        """
        temp = []
        a = self.flat_array()
        if type(other) == Array and self.shape == other.shape and (isinstance(a[0], int) or isinstance(a[0], float)):
            b = other.flat_array()
            if self.shape == other.shape and (isinstance(b[0], int) or isinstance(b[0], float)):
                for i in range(0, len(a)):
                    if a[i] == b[i]:
                        temp.append(True)
                    else:
                        temp.append(False)
                return Array(self.shape, *temp)

        elif type(other) == float or type(other) == int:
            for i in range(0, len(a)):
                if a[i] == other:
                    temp.append(True)
                else:
                    temp.append(False)
            return Array(self.shape, *temp)

        else:
            if self.shape != other.shape:
                raise ValueError("Arrays has not same shape")
            else:
                raise TypeError("Array has not the required type, float or int")

    def min_element(self):
        """Returns the smallest value of the array.
        Only needs to work for type int and float (not boolean).
        Returns:
            float: The value of the smallest element in the array.
        """
        temp = None
        for x in self.flat_array():
            if temp == None or x < temp:
                temp = x
        return temp
