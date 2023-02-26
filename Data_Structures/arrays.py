"""Arrays

An array is a collection of elements of the same data type, 
stored in contiguous memory locations, with a fixed size.
"""

import array as arr

numbers: arr = arr.array('i', [1, 2, 3, 4, 5])

print(numbers[3])  # 4

numbers[3] = 6
print(numbers)     # array('i', [1, 2, 3, 6, 5])

numbers.append(7)
print(numbers)     # array('i', [1, 2, 3, 6, 5, 7])


numbers.remove(7)
print(numbers)     # array('i', [1, 2, 3, 6, 5])


"""
One common use of arrays is in data analysis and scientific computing, 
where large datasets need to be stored and manipulated efficiently. 
In these fields, arrays are often used to store numerical data such as 
measurements or simulation results, and then perform computations on 
that data using specialized libraries like NumPy or SciPy.
"""

