# ---------------------------------------- BREAK ------------------------------------------

# 1. Find the first even digit from the left in 753914286.

number = int(input("Enter a number: "))
rev = 0
while number > 0:
    digit = number % 10
    rev = rev * 10 + digit
    number = number // 10
even = None
while rev > 0:
    digit = rev % 10
    if digit % 2 != 0:
        rev = rev // 10
        continue
    even = digit
    break
if even is not None:
    print(even)
else:
    print("No even digit found.")


# ==========================================================================================

# 2. Find the first prime number between 50 and 100.
for j in range(50, 101, 1):
    number = j
    count = 0
    for i in range(1, number + 1, 1):
        if number % i == 0:
            count += 1
    if count == 2:
        print(number)
        break


# ==========================================================================================

# 3. Find the first number whose digit sum is 10.
i = 1
while i >= 1:
    sum = 0
    num = i
    while num > 0:
        digit = num % 10
        sum += digit
        num = num // 10
    if sum == 10:
        print(i)
        break
    i += 1


# ==========================================================================================

# 4. Find the first number with exactly 3 divisors between 1 and 100.
for j in range(1, 101, 1):
    number = j
    count = 0
    for i in range(1, number + 1, 1):
        if number % i == 0:
            count += 1
    if count == 3:
        print(number)
        break


# ==========================================================================================

# 5. Stop when 3 consecutive odd numbers occur between 1 and 50.
count = 0
for i in range(1, 51, 1):
    if i % 2 != 0:
        count += 1
        print(i)
    else:
        count = 0
    if count == 3:
        break


# ==========================================================================================

# 6. Find the first palindrome between 10 and 500.
for i in range(10, 501, 1):
    number = i
    rev = 0
    while number > 0:
        digit = number % 10
        rev = rev * 10 + digit
        number = number // 10
    if i == rev:
        print(i)
        break


# ==========================================================================================

# 7. Find the first perfect number between 1 and 1000.
for j in range(1, 1001, 1):
    number = j
    sum = 0
    for i in range(1, number, 1):
        if number % i == 0:
            sum += i
    if sum == number:
        print(number)
        break


# ==========================================================================================

# 8. Print the first 5 even numbers.
count = 0
for i in range(1, 100, 1):
    if i % 2 == 0:
        print(i)
        count += 1
    if count == 5:
        break


# ==========================================================================================

# 9. Print the first 5 prime numbers.
count = 0
for j in range(2, 100, 1):
    number = j
    divisor_count = 0
    for i in range(1, number + 1, 1):
        if number % i == 0:
            divisor_count += 1
    if divisor_count == 2:
        print(number)
        count += 1
    if count == 5:
        break


# ==========================================================================================

# 10. Print the first 3 numbers divisible by 7.
count = 0
for i in range(1, 100, 1):
    if i % 7 == 0:
        print(i)
        count += 1
    if count == 3:
        break

# -------------------------------------- CONTINUE ------------------------------------------

# 1. Print 1–30, skipping even numbers.
for i in range(1, 31, 1):
    if i % 2 == 0:
        continue
    print(i)


# ==========================================================================================

# 2. Print 1–40, skipping multiples of 4.
for i in range(1, 41, 1):
    if i % 4 == 0:
        continue
    print(i)


# ==========================================================================================

# 3. Print 1–30, skipping numbers from 10–20.
for i in range(1, 31, 1):
    if i >= 10 and i <= 20:
        continue
    print(i)


# ==========================================================================================

# 4. Print 1–50, skipping multiples of 3.
for i in range(1, 51, 1):
    if i % 3 == 0:
        continue
    print(i)


# ==========================================================================================

# 5. Extract 502304, skipping digit 0.
number = 502304
while number > 0:
    digit = number % 10
    number = number // 10
    if digit == 0:
        continue
    print(digit)


# ==========================================================================================

# 6. Extract 5832461, printing only even digits.
number = 5832461
while number > 0:
    digit = number % 10
    number = number // 10
    if digit % 2 != 0:
        continue
    print(digit)


# ==========================================================================================

# 7. Extract 1432578, skipping odd digits.
number = 1432578
while number > 0:
    digit = number % 10
    number = number // 10
    if digit % 2 != 0:
        continue
    print(digit)


# ==========================================================================================

# 8. Print 1–200, skipping multiples of 3 or 5.
for i in range(1, 201, 1):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)


# ==========================================================================================

# 9. Print 1–500, skipping numbers with odd digit sum.
for i in range(1, 501, 1):
    number = i
    sum = 0
    while number > 0:
        digit = number % 10
        sum += digit
        number = number // 10
    if sum % 2 != 0:
        continue
    print(i)


# ==========================================================================================

# 10. Print 1–500, skipping numbers containing digit 0.
for i in range(1, 501, 1):
    number = i
    found_zero = False
    while number > 0:
        digit = number % 10
        number = number // 10
        if digit == 0:
            found_zero = True
            break
    if found_zero:
        continue
    print(i)

# ------------------------------- BREAK + CONTINUE -----------------------------------------

# 1. Print 1–50, skip multiples of 3, stop at 40.
for i in range(1, 51, 1):
    if i == 40:
        break
    if i % 3 == 0:
        continue
    print(i)


# ==========================================================================================

# 2. Print odd numbers, skip evens, stop at the first multiple of 7.
for i in range(1, 51, 1):
    if i % 7 == 0:
        break
    if i % 2 == 0:
        continue
    print(i)


# ==========================================================================================

# 3. Extract 5830421, skip odd digits, stop at 0.
number = 5830421
while number > 0:
    digit = number % 10
    number = number // 10
    if digit == 0:
        break
    if digit % 2 != 0:
        continue
    print(digit)


# ==========================================================================================

# 4. Extract 8325147, print digits until 5.
number = 8325147
while number > 0:
    digit = number % 10
    number = number // 10
    if digit == 5:
        break
    print(digit)


# ==========================================================================================

# 5. Search from 51, skip non-multiples of 9, stop at the first multiple of 9.
for i in range(51, 101, 1):
    if i % 9 != 0:
        continue
    print(i)
    break
