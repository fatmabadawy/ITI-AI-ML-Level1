import numpy as np

# 1. Write a Python program to find the maximum and minimum value of a given flattened array.

arr = np.array([[0, 1], [2, 3]])

print("Original flattened array:")
print(arr)

print("Maximum value of the above flattened array:")
print(np.max(arr))

print("Minimum value of the above flattened array:")
print(np.min(arr))


# 2. Write a NumPy program to get the minimum and maximum value of a given array along the second axis.

arr = np.array([[0, 1], [2, 3]])

print("\nOriginal array:")
print(arr)

print("Maximum value along the second axis:")
print(np.max(arr, axis=1))

print("Minimum value along the second axis:")
print(np.min(arr, axis=1))


# 3. Write a NumPy program to calculate the difference between the maximum and the minimum values of a given array along the second axis.

arr = np.array([[0, 1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10, 11]])

difference = np.max(arr, axis=1) - np.min(arr, axis=1)

print("\nOriginal array:")
print(arr)

print("Difference between the maximum and the minimum values of the said array:")
print(difference)


# 4. Write a NumPy program to compute the 80th percentile for all elements in a given array along the second axis.

arr = np.array([[1.0, 2.0, 3.0, 4.0]])

print("\nOriginal array:")
print(arr)

print("80th percentile:")
print(np.percentile(arr, 80, axis=1))


# 5. Write a NumPy program to compute the median of flattened given array.

arr = np.array([[0, 1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10, 11]])

print("\nOriginal array:")
print(arr)

print("Median of said array:")
print(np.median(arr))


# 6. Write a NumPy program to compute the weighted average of a given array.

arr = np.array([0, 1, 2, 3, 4])
weights = np.array([1, 2, 3, 4, 5])

weighted_average = np.average(arr, weights=weights)

print("\nOriginal array:")
print(arr)

print("Weighted average of the said array:")
print(weighted_average)


# 7. Write a NumPy program to compute the mean, standard deviation, and variance of a given array along the second axis.

arr = np.array([[0, 1, 2, 3, 4, 5]])

print("\nOriginal array:")
print(arr)

print("Mean:")
print(np.mean(arr, axis=1))

print("Standard deviation:")
print(np.std(arr, axis=1))

print("Variance:")
print(np.var(arr, axis=1))


# 8. Write a NumPy program to compute the covariance matrix of two given arrays.

arr1 = np.array([0, 1, 2])
arr2 = np.array([2, 1, 0])

print("\nOriginal array1:")
print(arr1)

print("Original array2:")
print(arr2)

print("Covariance matrix of the said arrays:")
print(np.cov(arr1, arr2))


# 9. Write a NumPy program to compute cross-correlation of two given arrays.

arr1 = np.array([0, 1, 3])
arr2 = np.array([2, 4, 5])

print("\nOriginal array1:")
print(arr1)

print("Original array2:")
print(arr2)

print("Cross-correlation of the said arrays:")
print(np.correlate(arr1, arr2))


# 10. Write a NumPy program to compute Pearson product-moment correlation coefficients of two given arrays.

arr1 = np.array([0, 1, 3])
arr2 = np.array([2, 4, 5])

print("\nOriginal array1:")
print(arr1)

print("Original array2:")
print(arr2)

print("Pearson product-moment correlation coefficients of the said arrays:")
print(np.corrcoef(arr1, arr2))


# 11. Write a NumPy program to test element-wise of a given array for finiteness,
# positive or negative infinity, NaN, NaT, negative infinity, and positive infinity.

arr = np.array([1.0, np.nan, np.inf])

print("\nTest element-wise for finiteness:")
print(np.isfinite(arr))

print("Test element-wise for positive or negative infinity:")
print(np.isinf(arr))

print("Test element-wise for NaN:")
print(np.isnan(arr))

arr_nat = np.array(['NaT', '2020-01-01'], dtype='datetime64')

print("Test element-wise for NaT:")
print(np.isnat(arr_nat))

print("Test element-wise for negative infinity:")
print(np.isneginf(np.array([-np.inf, 0, np.inf])).astype(int))

print("Test element-wise for positive infinity:")
print(np.isposinf(np.array([-np.inf, 0, np.inf])).astype(int))


# 12. Write a Python program to count number of occurrences of each value in a given array of non-negative integers.

arr = np.array([0, 1, 6, 1, 4, 1, 2, 2, 7])

print("\nOriginal array:")
print(arr)

print("Number of occurrences of each value in array:")
print(np.bincount(arr))


# 13. Write a NumPy program to compute the histogram of nums against the bins.

nums = np.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1])
bins = np.array([0, 1, 2, 3])

result = np.histogram(nums, bins)

print("\nnums:")
print(nums)

print("bins:")
print(bins)

print("Result:")
print(result)