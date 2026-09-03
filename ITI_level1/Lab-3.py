# OOP:
# 1. Write a Python program to create a class representing a Circle. Include
# methods to calculate its area and perimeter.
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

c = Circle(5)

print("Area =", c.area())
print("Perimeter =", c.perimeter())


# 2. Write a Python program to create a person class. Include attributes like name,
# country and date of birth. Implement a method to determine the person's age.

from datetime import datetime

class Person:
    def __init__(self, name, country, dateOfBirth):
        self.name = name
        self.country = country
        self.dateOfBirth = datetime.strptime(dateOfBirth, "%d/%m/%Y")

    def calculateAge(self):
        today = datetime.today()

        age = today.year - self.dateOfBirth.year

        if (today.month, today.day) < (self.dateOfBirth.month, self.dateOfBirth.day):
            age -= 1

        return age


person1 = Person("Fatma", "Egypt", "5/07/2005")

print("Name:", person1.name)
print("Country:", person1.country)
print("Age:", person1.calculateAge())

# 3. Write a Python program to create a calculator class. Include methods for basic
# arithmetic operations.

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if(self.num2==0):
            return "cannot divide by zero"
        else:
            return self.num1 / self.num2


calc = Calculator(10, 5)

print("Addition:", calc.add())
print("Subtraction:", calc.subtract())
print("Multiplication:", calc.multiply())
print("Division:", calc.divide())
        
# 4. Write a Python program to create a class that represents a shape. Include
# methods to calculate its area and perimeter. Implement subclasses for different
# shapes like circle, triangle, and square.

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


circle = Circle(5)
square = Square(4)
triangle = Triangle(3, 4, 5)

print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())

print("Square Area:", square.area())
print("Square Perimeter:", square.perimeter())

print("Triangle Area:", triangle.area())
print("Triangle Perimeter:", triangle.perimeter())