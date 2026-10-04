# 1.Find the sum of digits in a given number.
# n=int(input("Enter n: "))
# sum=0
# while n!=0:
#     ld=n%10
#     sum+=ld
#     n=n//10
# print(sum)

# 2.Find the average of digits in a given number.
# n=int(input("Enter n: "))
# sum=0
# count=0
# while n!=0:
#     ld=n%10
#     sum+=ld
#     count+=1
#     n=n//10
# print(sum/count)

# 3.Find the sum of the first digit and the last digit of a given number.
# n=int(input("Enter n: "))
# ld=n%10
# while n>0:
#     n=n//10
# print("Sum of first and last digit",ld+n)

# 4
# n=int(input("Enter n: "))
# sum=0
# while n>0:
#     ld=n%10
#     if ld%5==0:
#         sum+=ld
#     n=n//10
# print("Sum of digits divisible by 5 is",sum)

# 5
n=int(input("Enter n: "))
big=0
small=9
while n!=0:
    ld=n%10
    if ld<small:
        small=ld
    else:
        big=ld
    n=n//10
print("Difference between large and biggest is",big-small)