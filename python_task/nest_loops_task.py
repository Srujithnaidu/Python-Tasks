# Sum of Prime Numbers
# Find the sum of all prime numbers between 20 and 150.

# sum_of_primes=0
# for j in range(20,151,1):
#     number=j
#     count=0
#     for i in range(1,number+1,1):
#         if number%i==0:
#             count+=1
#     if count==2:
#         sum_of_primes+=number
# print(f"Sum of all prime numbers between 20 and 150 is {sum_of_primes}")

# ================================================================================
# Leap Years in a Range(Not Nested Loop Logic)
# Print all leap years between 1900 and 2026.

# for j in range(1900,2027,1):
#     number=j
#     if number%400 or (number%4==0 and number%100!=0):
#         print(f"{number} is a leap year")

# ================================================================================
# Palindrome Numbers
# Print all palindrome numbers between 100 and 500.
for j in range(100,501,1):
    n=j
    original_number=n
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit        
        n=n//10
    if rev==original_number:
        print(original_number, end=" ")


# ============================================================================
# Exactly 3 Factors
# Print all numbers between 10 and 300 that have exactly 3 factors.
# print("Numbers between 10 and 300 that have exactly 3 factors are:")
# for j in range(10,301,1):
#     number=j
#     count=0
#     for i in range(1,number+1,1):
#         if number%i==0:
#             count+=1
#     if count==3:
#         print(number)

# ===========================================================================
# Prime Factors
# Print the prime factors of every number between 20 and 50.




# Armstrong Numbers
# Print all Armstrong numbers between 100 and 999. 
# for j in range(100,1000,1):
#     number=j
#     original_number=number 
#     sum=0
#     while number>0:
#         digit=number%10
#         sum+=digit**3
#         number//=10
#     if sum==original_number:
#         print(original_number)

# ===============================================
# Maximum Factors
# Find the number between 50 and 150 that has the maximum number of factors.
# max=0
# for j in range(50,151,1):
#     number=j
#     factors_count = 0
#     for i in range(1,number+1,1):
#         if number%i==0:
#             factors_count+=1
#     if max<factors_count:
#         max=factors_count
#         max_number=number
# print(f"Number: {max_number} has maximum factors of {max}")
