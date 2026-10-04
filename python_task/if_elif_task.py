
# Electricity bill calculator
units=int(input("Enter units consumed: "))
if units<=100:
    bill=units*2
elif units>=101 and units<=200:
    bill=units*4
elif units>=201 and units<=300:
    bill=units*6
else:
    bill=units*8  
print("Total Electricity Bill: ", bill)

#---------------------------------------------------------------

# Leap year or not
year=int(input("Enter a year: "))
if year%400==0 or (year%4==0 and year%100!=0):
    print("Leap Year")
else:
    print("Not a Leap Year")


    # rest algorithm, flowchart , input output and process are in notebook