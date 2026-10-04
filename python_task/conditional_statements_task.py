# if - else

# =================================================================
# 1.Check whether a given number is a 3-digit number or not.
n=int(input("Enter a number: "))
if n >=100 and n<=999:
    print(f"{n} is a 3 digit number")
else:
    print(f"{n} is not a 3 digit number")

# 2.Check whether a given number is divisible by both 3 and 5 or not.
n=int(input("Enter a number: "))
if n%3==0 and n%5==0:
    print(f"{n} is divisible by both 3 and 5")
else:
    print(f"{n} is not divisible by both 3 and 5")

# 3.Check whether a given triangle is a valid triangle or not.
s1=int(input("Enter side1: "))
s2=int(input("Enter side2: "))
s3=int(input("Enter side3: "))
if s1+s2>s3 or s2+s3>s1 or s1+s3>s2:
    print("The given triangle is valid")
else:
    print("The given triangle is Invalid")

# 4.Check whether a given number is a multiple of 10 or not.
n=int(input("Enter a number: "))
if n%10==0:
    print(f"The given number {n} is a multiple of 10")
else:
    print(f"The given number {n} is not a multiple of 10")

# ==========================================================================================
# if - elif - else

# 1.Check the type of triangle based on its sides.
s1=int(input("Enter side1: "))
s2=int(input("Enter side2: "))
s3=int(input("Enter side3: "))
if s1==s2 and s2==s3:
    print("The given triangle is Equilateral Triangle")
elif s1==s2 or s2==s3 or s3==s1:
    print("The given triangle is Isosceles Triangle")
else:
    print("The given triangle is Scalene Triangle")


# 2. Electricity bill based on units consumed
# 0–100: ₹2/unit, 101–200: ₹3/unit, 201–300: ₹5/unit, above 300: ₹7/unit.
units=int(input("Enter units consumed: "))
if units<=100:
    bill=units*2
elif units>=101 and units<=200:
    bill=units*3
elif units>=201 and units<=300:
    bill=units*5
else:
    bill=units*7  
print("Total Electricity Bill: ", bill)

# 3.Display the age category.
# Below 13 → Child, 13–19 → Teenager, 20–59 → Adult, 60 and above → Senior Citizen.
age=int(input("Enter age: "))
if age<13:
    print("Child")
elif age>=13 and age<=19:
    print("Teenager")
elif age>=20 and age<=59:
    print("Adult")
else:
    print("Senior Citizen")

# 4.Calculate the discount based on shopping amount.
# Below ₹1,000 → No discount, ₹1,000–₹4,999 → 10%, ₹5,000–₹9,999 → 20%, ₹10,000 and above → 30%.
amount=int(input("Enter amount: "))
if amount<1000:
    discount_per=0
elif (1000<=amount<=4999):
    discount_per=10
elif (5000<=amount<=9999):
    discount_per=20
else:
    discount_per=30
discount_amount=amount*(discount_per/100)
print(f"The discount amount is {discount_amount}")


# 5.Display the season based on the month number.
#     3–5 → Spring, 6–8 → Summer, 9–11 → Autumn, 12/1/2 → Winter.
month=int(input("Enter month number: "))
if 3<=month<=5:
    print("Spring")
elif 6<=month<=8:
    print("Summer")
elif 9<=month<=11:
    print("Autumn")
elif month==12 or month==1 or month==2:
    print("Winter")
else:
    print("Invalid month number")

# 6.Check whether a given year is a Leap Year or not.
#     Condition 1: year % 400 == 0
#     Condition 2: year % 4 == 0 and year % 100 != 0
year=int(input("Enter a year: "))
if year%400==0 :
    print("Leap Year")
elif (year%4==0 and year%100!=0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# ============================================================================
# Nested if

# 1.Check whether a person is eligible to donate blood.
# Age should be between 18 and 60. If eligible by age, weight should be above 50 kg.
age=int(input("Enter age: "))
weight=int(input("Enter weight: "))
if 18<=age<=60:
    if weight>50:
        print("Eligible to donate blood")
    else:
        print("Not Eligible to donate blood because of weight")
else:
    print("Not eligible because of age")


# 2.Display the grade based on average only if the student has passed in all 4 subjects.
# Input marks for 4 subjects
sub1=int(input("Enter sub1 marks: "))
sub2=int(input("Enter sub2 marks: "))
sub3=int(input("Enter sub3 marks: "))
sub4=int(input("Enter sub4 marks: "))
if sub1 >= 35 and sub2 >= 35 and sub3 >= 35 and sub4 >= 35:
    total = sub1 + sub2 + sub3 + sub4
    average = total / 4
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "D"
    print(f"Passed Average Marks: {average}, Grade: {grade}")
else:
    print("Failed")


# 3.Check whether a student is eligible for a scholarship.
#     Age should be above 18. If eligible by age, score should be above 86.
age=int(input("Enter age: "))
score=int(input("Enter score: "))
if age > 18:
    if score > 86:
        print("Eligible for the scholarship.")
    else:
        print("Not eligible: Score must be above 86.")
        
else:
    print("Not eligible: Age must be above 18.")
