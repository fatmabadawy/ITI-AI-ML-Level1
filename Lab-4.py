# Part -1
import numpy as np

# 1. Write a NumPy program to test whether none of the elements of a given array are zero.
arr = np.array([1, 2, 3, 4, 5])
print(np.all(arr != 0))

# 2. Write a NumPy program to test if any of the elements of a given array are non-zero.
arr = np.array([0, 0, 3, 0])
print(np.any(arr != 0))

# 3. Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a number).
arr = np.array([1, np.inf, np.nan, 5])
print(np.isfinite(arr))

# 4. Write a NumPy program to test elements-wise for positive or negative infinity.
arr = np.array([1, np.inf, -np.inf, 5])
print(np.isinf(arr))

# 5. Write a NumPy program to test element-wise for NaN of a given array.
arr = np.array([1, np.nan, 3, np.nan])
print(np.isnan(arr))

# 6. Write a NumPy program to create an element-wise comparison (greater, greater_equal,
# less and less_equal) of two given arrays.
arr1 = np.array([1, 5, 10])
arr2 = np.array([2, 5, 8])

print("Greater:", np.greater(arr1, arr2))
print("Greater Equal:", np.greater_equal(arr1, arr2))
print("Less:", np.less(arr1, arr2))
print("Less Equal:", np.less_equal(arr1, arr2))

# 7. Write a NumPy program to create an element-wise comparison (equal, equal within a
# tolerance) of two given arrays.
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2.000001, 4])

print("Equal:", np.equal(arr1, arr2))
print("Equal within tolerance:", np.isclose(arr1, arr2))

# 8. Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives.
arr = np.concatenate([np.zeros(10), np.ones(10), np.full(10, 5)])
print(arr)

# 9. Write a NumPy program to create an array of integers from 30 to 70.
arr = np.arange(30,71)
print(arr)


# 10. Write a NumPy program to create an array of all even integers from 30 to 70.
arr = np.arange(30,71,2)
print(arr)

# 11. Write a NumPy program to create a 3x3 identity matrix.
arr = np.eye(3)
print(arr)


# 12. Write a NumPy program to generate a random number between 0 and 1.
random_number = np.random.rand()
print(random_number)

# 13. Write a NumPy program to create a vector with values ranging from 15 to 55 and print all
# values except the first and last.
arr = np.arange(15, 56)
print(arr[1:-1])

# 14. Write a NumPy program to create a 3X4 array and iterate over it.
arr = np.arange(12).reshape(3, 4)

for i in arr:
    for x in i:
        print(x)


# 15. Write a NumPy program to create a vector of length 10 with values evenly distributed
# between 5 and 50.

arr = np.linspace(5, 50, 10)
print(arr)


# 16. Write a NumPy program to create a vector with values from 0 to 20 and change the sign
# of the numbers in the range from 9 to 15.

arr = np.arange(0,21)
arr[9:16] = -arr[9:16]
print(arr)


# 17. Write a NumPy program to multiply the values of two given vectors.

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

result = arr1 * arr2

print(result)

# 18. Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.

arr = np.arange(10,22).reshape(3,4)
print(arr)


# 19. Write a NumPy program to find the number of rows and columns in a given matrix.

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

rows, columns = arr.shape

print("Rows:", rows)
print("Columns:", columns)

# 20. Write a NumPy program to create a 5x5 zero matrix with elements on the main diagonal
# equal to 1, 2, 3, 4, 5.

arr = np.zeros((5, 5), dtype=int)

np.fill_diagonal(arr, [1, 2, 3, 4, 5])

print(arr)

# 21. Write a NumPy program to create a 3x3x3 array filled with arbitrary values.

arr = np.random.rand(3, 3, 3)

print(arr)

# 22. Write a NumPy program to compute the sum of all elements, the sum of each column and
# the sum of each row in a given array.

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Total sum:", np.sum(arr))
print("Column sums:", np.sum(arr, axis=0))
print("Row sums:", np.sum(arr, axis=1))

# 23. Write a NumPy program to compute the inner product of two given vectors.

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = np.inner(arr1, arr2)

print(result)

# 24. Write a NumPy program to add a vector to each row of a given matrix.

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

vector = np.array([10, 20, 30])

result = matrix + vector

print(result)

# 25. Write a NumPy program to check whether two arrays are equal (element wise) or not.

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

result = np.array_equal(arr1, arr2)

print(result)

# 26. Write a NumPy program to create a new array of given shape (5,6) and type, filled with zeros.

arr = np.zeros((5, 6), dtype=int)

print(arr)

# 27. Write a NumPy program to sort a given array by row and column in ascending order.

arr = np.array([
    [3, 1, 2],
    [9, 5, 6],
    [8, 7, 4]
])

row_sorted = np.sort(arr, axis=1)
column_sorted = np.sort(arr, axis=0)

print("Sorted by rows:", row_sorted)
print("Sorted by columns:", column_sorted)


# 28. Write a NumPy program to extract all numbers from a given array less and greater than a specified number.

arr = np.array([1, 5, 8, 10, 15, 20])
number = 10

less = arr[arr < number]
greater = arr[arr > number]

print("Less than 10:", less)
print("Greater than 10:", greater)

# 29. Write a NumPy program to replace all numbers in a given array equal, less and greater
# than a given number.

arr = np.array([1, 5, 10, 15, 20])
number = 10

arr[arr < number] = 0
arr[arr > number] = 1
arr[arr == number] = 2

print(arr)


# 30. Write a NumPy program to create a 4x4 array. Create an array from said array by swapping
# first and last, second and third columns.

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

result = arr[:, ::-1]

print(result)

# 31. Write a NumPy program to swap rows and columns of a given array in reverse order.

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

result = arr[::-1, ::-1]

print(result)


# 32. Write a NumPy program to multiply two given arrays of the same size element-by-element.

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

result = arr1 * arr2

print(result)



# Part-2

# 1. Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.

list1 = [12.23, 13.32, 100, 36.32]

arr = np.array(list1)

print("Original List:", list1)
print("One-dimensional NumPy array:", arr)

# 2. Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

arr = np.arange(2, 11).reshape(3, 3)
print(arr)

# 3. Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.

arr = np.zeros(10)

print(arr)

arr[5] = 11

print("Update sixth value to 11")
print(arr)

# 4. Write a NumPy program to create an array with values ranging from 12 to 38.

arr = np.arange(12,38)
print(arr)

# 5. Write a NumPy program to reverse an array (the first element becomes the last).

arr = np.arange(12, 39)

print("Original array:")
print(arr)

reverse_arr = arr[::-1]

print("Reverse array:")
print(reverse_arr)

# 6. Write a NumPy program to convert an array to a floating type.

arr = np.array([1, 2, 3, 4])

float_arr = arr.astype(float)

print("Original array:")
print(arr)

print("Array converted to a float type:")
print(float_arr)

# 7. Write a NumPy program to append values to the end of an array.

arr = np.array([10, 20, 30])

arr = np.append(arr, [40, 50, 60, 70, 80, 90])

print("Original array:")
print([10, 20, 30])

print("After append values to the end of the array:")
print(arr)


# 8. Write a NumPy program to create an empty and full array.

empty_array = np.empty((3, 4))

full_array = np.full((3, 3), 6)

print("Empty array:")
print(empty_array)

print("Full array:")
print(full_array)

# 9. Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees.
# Centigrade values are stored in a NumPy array.

celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0])

fahrenheit = (celsius * (9 / 5)) + 32

print("Values in Centigrade degrees:")
print(celsius)

print("Values in Fahrenheit degrees:")
print(fahrenheit)

# 10. Write a NumPy program to test whether each element of a 1-D array is also present in a
# second array.

array1 = np.array([0, 10, 20, 40, 60])
array2 = np.array([0, 40])

result = np.isin(array1, array2)

print("Array1:", array1)
print("Array2:", array2)

print("Compare each element of array1 and array2")
print(result)

# 11. Write a NumPy program to find common values between two arrays.

array1 = np.array([0, 10, 20, 40, 60])
array2 = np.array([10, 30, 40, 50, 70, 90])

common = np.intersect1d(array1, array2)

print("Array1:")
print(array1)

print("Array2:")
print(array2)

print("Common values:")
print(common)

# 12. Write a NumPy program to get the unique elements of an array.

arr = np.array([10, 10, 20, 20, 30, 30])

unique_values = np.unique(arr)

print("Original array:")
print(arr)

print("Unique elements:")
print(unique_values) 

# 13. Write a NumPy program to find the set difference between two arrays. The set
# difference will return sorted, distinct values in array1 that are not in array2.

array1 = np.array([0, 10, 20, 40, 60, 80])
array2 = np.array([10, 30, 40, 50, 70, 90])

difference = np.setdiff1d(array1, array2)

print("Array1:")
print(array1)

print("Array2:")
print(array2)

print("Set difference:")
print(difference)


# 14. Write a NumPy program to compare two arrays using NumPy.

array1 = np.array([1, 2])
array2 = np.array([4, 5])

print("a > b")
print(array1 > array2)

print("a >= b")
print(array1 >= array2)

print("a < b")
print(array1 < array2)

print("a <= b")
print(array1 <= array2)


print("Element-wise comparison:")
print(array1 == array2)

print("Arrays are equal:", np.array_equal(array1, array2))

# 15. Write a NumPy program to sort along the first and last axes of an array.Sample array: [[2,5],[4,4]]

arr = np.array([[4, 6],[2, 1]])

print("Original array:", arr)

print("Sort along the first axis:")
print(np.sort(arr, axis=0))

print("Sort along the last axis:")
print(np.sort(arr, axis=1))

# 16. Write a NumPy program to get the values and indices of the elements that are bigger than 10 in a given array.

arr = np.array([
    [0, 10, 20],
    [20, 30, 40]
])

values = arr[arr > 10]
indices = np.where(arr > 10)

print("Values bigger than 10 =", values)
print("Their indices are", indices)


# 17. Write a NumPy program to create a contiguous flattened array.

arr = np.array([
    [10, 20, 30],
    [20, 40, 50]
])

new_arr = np.ascontiguousarray(arr).flatten()

print("New flattened array:")
print(new_arr)

# 18. Write a NumPy program to create a 2-dimensional array of size 2 x 3 (composed of 4-
# byte integer elements), also print the shape, type and data type of the array.

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
], dtype=np.int32)

print("Array:")
print(arr)

print("Shape:", arr.shape)
print("Type:", type(arr))
print("Data type:", arr.dtype)


# 19. Write a NumPy program to create another shape from an array without changing its data.

arr = np.array([1, 2, 3, 4, 5, 6])

print("Original array:")
print(arr)

print("Reshape 3x2:")
print(arr.reshape(3, 2))

print("Reshape 2x3:")
print(arr.reshape(2, 3))


# 20. Write a NumPy program to create a new array of 3*5, filled with 2.

arr = np.full((3, 5), 2)

print(arr)

# 21. Write a NumPy program to create an array of 10's with the same shape and type as the given array.

arr = np.array([
    [2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2]
])

new_arr = np.full_like(arr, 10)

print(new_arr)

# 22. Write a NumPy program to create a 2-D array whose diagonal equals [4, 5, 6, 8] and 0's elsewhere.

arr = np.diag([4, 5, 6, 8])

print(arr)


# 23. Write a NumPy program to create a 1-D array with values from 0 to 50 and an array from 10 to 50.

arr1 = np.arange(0, 50)
arr2 = np.arange(10, 50)

print("Array from 0 to 50:")
print(arr1)

print("Array from 10 to 50:")
print(arr2)


# 24. Write a NumPy program to find the 4th element of a specified array.

arr = np.array([
    [2, 4, 6],
    [6, 8, 10]
])

print("Fourth element of the array:")
print(arr.flatten()[3])

# 25. Write a NumPy program to test whether specified values are present in an array.

arr = np.array([
    [1.12, 2.00, 3.45],
    [2.33, 5.12, 6.00]
])

values = [2.00, 4.00, 6.00, 8.00, 10.00]

for value in values:
    print(np.isin(value, arr))