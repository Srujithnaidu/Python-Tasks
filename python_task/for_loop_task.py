# 1.Find the average of numbers from 1 to N.
#     Example: If N = 5, calculate the average of 1, 2, 3, 4, 5.
n=int(input("Enter n: "))
sum=0
for i in range(1,n+1,1):
    sum+=i
avg=sum/n
print(f"The avg of first {n} numbers is {avg}")


# 2.Find the sum of squares of numbers from 1 to N.
#     Example: If N = 5, calculate 1² + 2² + 3² + 4² + 5².
n=int(input("Enter n: "))
sum=0
for i in range(1,n+1,1):
    sum+=i**2
print(f"The sum of squares of numbers from 1 to {n} is {sum}")



# 3.Find the sum of cubes of numbers from 1 to N.
#     Example: If N = 5, calculate 1³ + 2³ + 3³ + 4³ + 5³.
n=int(input("Enter n: "))
sum=0
for i in range(1,n+1,1):
    sum+=i**3
print(f"The sum of cubes of numbers from 1 to {n} is {sum}")


# 4.Calculate the power of a number without using the ** operator.
#     Example: If base = 2 and power = 5, calculate 2 × 2 × 2 × 2 × 2.
base=int(input("Enter base: "))
power=int(input("Enter power: "))
result=1
for i in range(1,power+1,1):
    result*=base
print(result)


# 5.Display the first N terms of the Fibonacci series.
#     Example: If N = 7, display 0, 1, 1, 2, 3, 5, 8.
n=int(input("Enter n: "))
a=0
b=1
for i in range(1, n + 1, 1):
    print(a)
    c = a + b
    a = b
    b = c

# 6.Display the first N terms of the series:
#     1, 1/2, 1/3, 1/4, ...
#     Example: If N = 4, display 1, 1/2, 1/3, 1/4.
n=int(input("Enter n: "))
if n>=1:
    print("1")
for i in range(2,n+1,1): 
    print(f"1/{i}")


# 7.Display the first N terms of the series:
#     1, 11, 111, 1111, 11111, ...
#     Example: If N = 5, display 1, 11, 111, 1111, 11111.
n=int(input("Enter n: "))
s=""
for i in range(1,n+1,1):
    s=s+"1"
    print(s)


# 8.Display the first N terms of the series:
#     1, 3, 9, 27, 81, ...
#     Each term is obtained by multiplying the previous term by 3.
n=int(input("Enter n: "))
term=1
for i in range(1,n+1,1):
    print(term)
    term*=3
    