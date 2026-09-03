# 1- Write a Python program which accepts the radius of a circle from the
# user and compute the area.

radius = float(input("Enter the radius of the circle: "))
area = 3.14 * radius ** 2
print("The area of the circle is:", area)

# 2- Write a Python program to Check if a Number is Odd or Even.

number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number, "is an Even number.")
else:
    print(number, "is an Odd number.")

# 3- Write a Python program to sum of three given integers. However, if two
# values are equal sum will be zero.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a == b or a == c or b == c:
    sum = 0
else:
    sum = a + b + c

print("The sum of the three numbers is:", sum)

# 4- Python program to Print the Natural Numbers Summation Pattern.

n = int(input("Enter the number of terms: "))

total = 0

for i in range(1, n + 1):
    total += i
    if i == n:
        print(i, end=" = ")
    else:
        print(i, end=" + ")

print(total)



# 5- Check Prime Number in Python.

number = int(input("Enter a number: "))
is_prime = True
if number <= 1:
    is_prime = False
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")


#6- Write a Python program to compute and display the first 16 numbers
# powers of 2, starting with 1.

for i in range(16):
    print("2 raised to the power of", i, "is:", 2 ** i)

# 7- Write a Python program to print all even numbers from 1 to n using for
# loop.

n = int(input("Enter a number: "))
print("Even numbers from 1 to", n, "are:")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=" ")

# Python program to generate all even numbers between given range.
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print("Even numbers between", start, "and", end, "are:")
for i in range(start, end + 1):
    if i % 2 == 0:
        print(i, end=" ")
