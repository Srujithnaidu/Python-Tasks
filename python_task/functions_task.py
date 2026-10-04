# =====================================without input without return========================================
# Write a function to print your name and age.
def print_name_age():
    name = "Srujith"
    age = 22
    print(f"My name is {name} and I am {age} years old.")
print_name_age()


# Write a function that takes two numbers and prints their sum.
def sum_of_two_numbers():
    a = 5
    b = 10 
    sum = a + b
    print(f"The sum of {a} and {b} is {sum}.")
sum_of_two_numbers()


# Write a function that takes a number and prints whether it is even or odd.
def even_odd():
    num=5
    if num%2==0:
        print(f"{num} is even")
    else:       
        print(f"{num} is odd")
even_odd()

# Write a function that takes two numbers and returns the larger number.
def larger_number():
    a = 5
    b = 10
    if a > b:
        print(f"The larger number between {a} and {b} is {a}.")
    else:
        print(f"The larger number between {a} and {b} is {b}.")
larger_number()

# Write a function that takes a number and prints its multiplication table up to 10.
def multiplication_table():
    n = 5
    print(f"Multiplication table of {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
multiplication_table()



# ==================================================================================================
# 1. NAMED FUNCTION - WITHOUT INPUT & WITHOUT RETURN

# 1. Print a message

def message():
    print("Welcome to Python Programming")

message()


# --------------------------------------------------------------------------------------------------

# 2. Print your name

def display_name():
    name = "Srujith"
    print("Name =", name)

display_name()


# --------------------------------------------------------------------------------------------------

# 3. Check whether a number is even or odd

def check_even_odd():
    number = 25

    if number % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

check_even_odd()


# --------------------------------------------------------------------------------------------------

# 4. Find the largest of two numbers

def largest_of_two():
    a = 45
    b = 72

    if a > b:
        print("Largest =", a)
    else:
        print("Largest =", b)

largest_of_two()


# --------------------------------------------------------------------------------------------------

# 5. Print numbers from 1 to 10

def print_numbers():
    for i in range(1, 11):
        print(i)

print_numbers()


# --------------------------------------------------------------------------------------------------

# 6. Find the sum of numbers from 1 to 10

def sum_numbers():
    sum = 0

    for i in range(1, 11):
        sum += i

    print("Sum =", sum)

sum_numbers()


# --------------------------------------------------------------------------------------------------

# 7. Print the multiplication table of a number

def multiplication_table():
    number = 7

    for i in range(1, 11):
        print(number, "x", i, "=", number * i)

multiplication_table()


# --------------------------------------------------------------------------------------------------

# 8. Find the factorial of a number

def factorial():
    number = 5
    fact = 1

    for i in range(1, number + 1):
        fact *= i

    print("Factorial =", fact)

factorial()


# --------------------------------------------------------------------------------------------------

# 9. Check whether a number is prime

def check_prime():
    number = 29
    count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count == 2:
        print("Prime Number")
    else:
        print("Not a Prime Number")

check_prime()


# --------------------------------------------------------------------------------------------------

# 10. Check whether a number is palindrome

def check_palindrome():
    number = 121
    original = number
    rev = 0

    while number > 0:
        digit = number % 10
        rev = rev * 10 + digit
        number //= 10

    if original == rev:
        print("Palindrome")
    else:
        print("Not a Palindrome")

check_palindrome()


# ==================================================================================================
# 2. NAMED FUNCTION - WITH INPUT & WITHOUT RETURN

# 1. Print the entered name

def display_name(name):
    print("Name =", name)

display_name("Srujith")


# --------------------------------------------------------------------------------------------------

# 2. Check even or odd

def check_even_odd(number):

    if number % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

check_even_odd(24)


# --------------------------------------------------------------------------------------------------

# 3. Find the largest of two numbers

def largest_of_two(a, b):

    if a > b:
        print("Largest =", a)
    else:
        print("Largest =", b)

largest_of_two(45, 72)


# --------------------------------------------------------------------------------------------------

# 4. Find the largest of three numbers

def largest_of_three(a, b, c):

    if a > b and a > c:
        print("Largest =", a)
    elif b > c:
        print("Largest =", b)
    else:
        print("Largest =", c)

largest_of_three(45, 72, 31)


# --------------------------------------------------------------------------------------------------

# 5. Print numbers from 1 to N

def print_numbers(n):

    for i in range(1, n + 1):
        print(i)

print_numbers(10)


# --------------------------------------------------------------------------------------------------

# 6. Find the sum from 1 to N

def sum_numbers(n):

    sum = 0

    for i in range(1, n + 1):
        sum += i

    print("Sum =", sum)

sum_numbers(10)


# --------------------------------------------------------------------------------------------------

# 7. Print multiplication table

def multiplication_table(number):

    for i in range(1, 11):
        print(number, "x", i, "=", number * i)

multiplication_table(8)


# --------------------------------------------------------------------------------------------------

# 8. Find the factorial

def factorial(number):

    fact = 1

    for i in range(1, number + 1):
        fact *= i

    print("Factorial =", fact)

factorial(6)


# --------------------------------------------------------------------------------------------------

# 9. Check whether a number is prime

def check_prime(number):

    count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count == 2:
        print("Prime Number")
    else:
        print("Not a Prime Number")

check_prime(31)


# --------------------------------------------------------------------------------------------------

# 10. Check whether a number is palindrome

def check_palindrome(number):

    original = number
    rev = 0

    while number > 0:
        digit = number % 10
        rev = rev * 10 + digit
        number //= 10

    if original == rev:
        print("Palindrome")
    else:
        print("Not a Palindrome")

check_palindrome(1221)


# ==================================================================================================
# 3. NAMED FUNCTION - WITHOUT INPUT & WITH RETURN

# 1. Return a fixed number

def get_number():
    number = 25
    return number

result = get_number()
print("Number =", result)


# --------------------------------------------------------------------------------------------------

# 2. Return the sum of two fixed numbers

def addition():
    a = 20
    b = 30

    return a + b

result = addition()
print("Sum =", result)


# --------------------------------------------------------------------------------------------------

# 3. Return the largest of two numbers

def largest_of_two():

    a = 45
    b = 72

    if a > b:
        return a
    else:
        return b

result = largest_of_two()
print("Largest =", result)


# --------------------------------------------------------------------------------------------------

# 4. Return the largest of three numbers

def largest_of_three():

    a = 35
    b = 72
    c = 51

    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

result = largest_of_three()
print("Largest =", result)


# --------------------------------------------------------------------------------------------------

# 5. Return the sum from 1 to 10

def sum_numbers():

    sum = 0

    for i in range(1, 11):
        sum += i

    return sum

result = sum_numbers()
print("Sum =", result)


# --------------------------------------------------------------------------------------------------

# 6. Return the factorial of a number

def factorial():

    number = 5
    fact = 1

    for i in range(1, number + 1):
        fact *= i

    return fact

result = factorial()
print("Factorial =", result)


# --------------------------------------------------------------------------------------------------

# 7. Return whether a number is even or odd

def check_even_odd():

    number = 26

    if number % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"

result = check_even_odd()
print(result)


# --------------------------------------------------------------------------------------------------

# 8. Return the reverse of a number

def reverse_number():

    number = 58321
    rev = 0

    while number > 0:
        digit = number % 10
        rev = rev * 10 + digit
        number //= 10

    return rev

result = reverse_number()
print("Reverse =", result)


# --------------------------------------------------------------------------------------------------

# 9. Return the sum of digits

def digit_sum():

    number = 58342
    sum = 0

    while number > 0:
        digit = number % 10
        sum += digit
        number //= 10

    return sum

result = digit_sum()
print("Digit Sum =", result)


# --------------------------------------------------------------------------------------------------

# 10. Return whether a number is prime

def check_prime():

    number = 37
    count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count == 2:
        return True
    else:
        return False

result = check_prime()

if result:
    print("Prime Number")
else:
    print("Not a Prime Number")


# ==================================================================================================
# 4. NAMED FUNCTION - WITH INPUT & WITH RETURN

# 1. Return the square of a number

def square(number):
    return number * number

result = square(8)
print("Square =", result)


# --------------------------------------------------------------------------------------------------

# 2. Return the largest of two numbers

def largest_of_two(a, b):

    if a > b:
        return a
    else:
        return b

result = largest_of_two(45, 72)
print("Largest =", result)


# --------------------------------------------------------------------------------------------------

# 3. Return the largest of three numbers

def largest_of_three(a, b, c):

    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

result = largest_of_three(45, 72, 31)
print("Largest =", result)


# --------------------------------------------------------------------------------------------------

# 4. Return the factorial of a number

def factorial(number):

    fact = 1

    for i in range(1, number + 1):
        fact *= i

    return fact

result = factorial(5)
print("Factorial =", result)


# --------------------------------------------------------------------------------------------------

# 5. Return the sum of digits

def digit_sum(number):

    sum = 0

    while number > 0:
        digit = number % 10
        sum += digit
        number //= 10

    return sum

result = digit_sum(58342)
print("Digit Sum =", result)


# --------------------------------------------------------------------------------------------------

# 6. Return the reverse of a number

def reverse_number(number):

    rev = 0

    while number > 0:
        digit = number % 10
        rev = rev * 10 + digit
        number //= 10

    return rev

result = reverse_number(58321)
print("Reverse =", result)


# --------------------------------------------------------------------------------------------------

# 7. Return whether a number is palindrome

def check_palindrome(number):

    original = number
    rev = 0

    while number > 0:
        digit = number % 10
        rev = rev * 10 + digit
        number //= 10

    if original == rev:
        return True
    else:
        return False

result = check_palindrome(1221)

if result:
    print("Palindrome")
else:
    print("Not a Palindrome")


# --------------------------------------------------------------------------------------------------

# 8. Return whether a number is prime

def check_prime(number):

    count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count == 2:
        return True
    else:
        return False

result = check_prime(31)

if result:
    print("Prime Number")
else:
    print("Not a Prime Number")


# --------------------------------------------------------------------------------------------------

# 9. Return the number of digits

def count_digits(number):

    count = 0

    while number > 0:
        number //= 10
        count += 1

    return count

result = count_digits(583421)
print("Number of Digits =", result)


# --------------------------------------------------------------------------------------------------

# 10. Return the GCD of two numbers

def gcd(a, b):

    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    return a

result = gcd(48, 18)
print("GCD =", result)

