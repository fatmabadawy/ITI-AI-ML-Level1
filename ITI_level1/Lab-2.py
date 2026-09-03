#Basics
# 1. Write a program that accepts a length in inches and prints the length in centimeters (1 inch = 2.54cm).
# Note: use float() for real numbers not int() when casting the data type in input statement, and add {:.2f} in print statement for two decimal places.

length = float(input("Enter a length in inches: "))
length *= 2.54
print(f"Length in cm is: {length:.2f}")

# 2. Write a program that converts temperatures from Celsius to Fahrenheit.

temp= float(input("Enter a temperatures in Celsius : "))
temp = (temp * 9/5) + 32
print("Temperature in Fahrenheit is: {:.2f}".format(temp))


# 3. Write a program that calculates the volume of a sphere.
radius = float(input("Enter a radius: "))
volume = (4/3) * 3.14 * (radius**3)
print("Volume of the sphere = {:.2f}".format(volume))

# 4. Write a program to calculate and display an employee’s gross and net pay. In this scenario, tax is deducted from the gross pay at a rate of 20% to give the net pay.

hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

gross_pay = hours * rate
tax = gross_pay * 0.20
net_pay = gross_pay - tax

print("Gross Pay: {:.2f}".format(gross_pay))
print("Net Pay: {:.2f}".format(net_pay))


# 5. Write a program to print the numbers 1 - 10 to the screen.

for i in range(1,11):
    print(i)

# 6. Write a program that accepts a number from the user until a negative number is entered.

x = int(input("Enter a number: "))
while x >= 0:
    x = int(input("Enter a number: "))

# 7. Write a program that accepts an integer and prints the specified range it belongs to.
# - Range 1: 0 to 10
# - Range 2: 11 to 20
# - Range 3: 21 to 30
# - Range 4: 31 to 40

x=int(input("Enter a number: "))
if(0 <= x <= 10):
    print("Range 1")
elif(11 <= x <= 20):
    print("Range 2")
elif(21 <= x <= 30):
    print("Range 3")
elif(31 <= x <= 40):
    print("Range 4")



# Strings:
# 1. Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

x=input("Enter a string: ")
print("Reversed string is: ", x[::-1])

# 2. Write a Python function that accepts a string and counts the number of upper- and lower-case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output : No. of Upper case characters : 3  No. of Lower case Characters : 12


def count_case(s):
    upper = 0
    lower = 0
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    print("No. of Upper case characters : ",upper)
    print("No. of Lower case Characters : ",lower)

count_case('The quick Brow Fox')

# 3. Write a Python function that checks whether a passed string is a palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

def is_palindrome(s):
    s = s.replace(" ", "").lower()  
    if (s == s[::-1]):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

is_palindrome('madam')



# Lists
# 1. Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5] Unique List : [1, 2, 3, 4, 5]

def distinct_elements(lst):
    unique_list = []
    
    for i in lst:
        if i not in unique_list:
            unique_list.append(i)
    
    return unique_list


lst = [1, 2, 3, 3, 3, 3, 4, 5]
print("Unique List:", distinct_elements(lst))


def unique_list(lst):
    return list(set(lst))

    
# 2. Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9] Expected Result : [2, 4, 6, 8]

def even_list(lst):
    even = []   
    for i in lst:
        if i % 2 == 0:
            even.append(i)    
    return even

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Even numbers:", even_list(lst))


# 3. Write a Python function to find the kth largest element in a list.

def kth_largest(lst, k):
    sorted_list = sorted(lst, reverse=True)
    return sorted_list[k - 1]

lst = [10, 5, 20, 8, 15]

k = int(input("Enter k: "))

print("Kth largest:", kth_largest(lst, k))

# 4. Write a Python function to check if a list is a palindrome or not. Return true otherwise false.

def List_ispalindrome(lst):
    lst2 = lst[::-1]  
    if lst == lst2:
        return True
    else:
        return False

# 5. Write a program that stores a shopping list of 10 items. Print the whole list to the screen, then print items 2 and 8.
lst = []

for i in range(10):
    x = input("Enter an item: ")
    lst.append(x)

print("All items:", lst)
print("Item 2:", lst[1])
print("Item 8:", lst[7])

# 6. Extend the previous program, to insert an item into the list.

lst = []

for i in range(10):
    x = input("Enter an item: ")
    lst.append(x)

print("Original list:", lst)

item = input("Enter an item to insert: ")
position = int(input("Enter the position: "))

lst.insert(position, item)

print("Updated list:", lst)


# Dictionary:
my_dict = {'a': 3, 'b': 1, 'c': 2}
# 1. Write a Python script to sort (ascending and descending) a dictionary by value.

def sort_dic(my_dict):
    ascending = dict(sorted(my_dict.items(), key=lambda x: x[1]))
    descending = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
    print("Ascending:", ascending)
    print("Descending:", descending)

sort_dic(my_dict)

# 2. Write a Python script to check whether a given key already exists in a dictionary.

key=input("Enter a key: ")
if (key in my_dict.keys()):
    print("key exist")
else:
    print("key is not exit")


# 3. Write a Python program to iterate over dictionaries using for loops.

for i,j in my_dict.items():
    print("key is ",i,"value is ",j)

# 4. Generate Dictionary of Numbers and Their Squares.

dic={}
for i in range (10):
    dic[i] = (i**2)
print(dic)
# 5. Write a program that adds some employee data to a dictionary. Use an employee number
# as the key.

employees = {}

emp_no = input("Enter employee number: ")
name = input("Enter employee name: ")
salary = float(input("Enter employee salary: "))

employees[emp_no] = {
    "name": name,
    "salary": salary
}

print(employees)

# Functions:
# 1. Write a program that accepts a number from the user and uses a function to
# square the number then return the result. Print the result to the screen.

def square(number):
    return number ** 2


x = float(input("Enter a number: "))

result = square(x)

print("Square =", result)

# 2. Write a function that returns the largest of two numbers. Test the function and
# print the results to the screen.

def largest(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

result = largest(x, y)

print("Largest number =", result)