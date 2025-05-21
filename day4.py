#wap to make a ticket calculator
'''age=int(input("Enter your age:"))
if age < 12:
    print("your ticketis free")
elif age >= 12 and age < 60:
    membership = input("Do you have a membership? (yes/no):")
    if membership.lower() == "yes":
        print("your ticket is 150")
    else:
        print("your ticket is 200")
elif age >= 60:
    print("congratulation you get senior citizen discount 😉 and your ticket is 100😘")
else:
    print("Invalid age entered")
   
'''

#wap to calculate electricity bill
'''
eletricity_usage = int(input("Enter the number of units consumed: "))
if eletricity_usage <= 100:
    bill = eletricity_usage * 5
    print(f"Your bill is: {bill}")
elif eletricity_usage <= 200:
    bill = 100 * 5 + (eletricity_usage - 100) * 8
    print(f"Your bill is: {bill}")

elif eletricity_usage <= 300:
    bill = 100 * 5 + 100 * 8 + (eletricity_usage - 200) * 10
    print(f"Your bill is: {bill}")
'''


"""
#wap to make to take speed and license status as input and calculate fine

license_status = input("Do you have a license? (yes/no): ")
speed = int(input("Enter the speed: "))
if license_status.lower() == "yes":
    if speed <= 60:
        print("You are within the speed limit. No fine.")
    elif speed <= 61-80:
        print("You are over the speed limit. Your fine is 500.")
    
if license_status.lower() == "no":
    if speed <= 60:
        print("You are within the speed limit. No fine.")
    elif speed <= 61-80:
        print("You are over the speed limit. Your fine is 1000.")
    
"""

#wap to check if a number is positive, negative or zero
"""

num=int(input("Enter a number: "))
if num==0:
    print("The number is zero")
elif num>0:
    print("The number is positive")
else:
    print("The number is negative")

"""
#wap to check if a number is even or odd
"""
num = int(input("Enter a number: "))
if num%2==0:
    print("The number is even")
else:
    print("The number is odd")    
"""

#wap to accept the age of 4 people and find the youngest one
'''
age1 = int(input("Enter the age of person 1: "))
age2 = int(input("Enter the age of person 2: "))
age3 = int(input("Enter the age of person 3: "))
age4 = int(input("Enter the age of person 4: "))
if age1 < age2 and age1 < age3 and age1 < age4:
    print("The youngest person is person 1 with age", age1)
elif age2 < age1 and age2 < age3 and age2 < age4:   
    print("The youngest person is person 2 with age", age2)
elif age3 < age1 and age3 < age2 and age3 < age4:
    print("The youngest person is person 3 with age", age3)
elif age4 < age1 and age4 < age2 and age4 < age3:
    print("The youngest person is person 4 with age", age4)
else:
    print("All persons are of the same age")
'''
#wap to accept the age of 4 people and find the olderst one
'''
age1 = int(input("Enter the age of person 1: "))
age2 = int(input("Enter the age of person 2: "))
age3 = int(input("Enter the age of person 3: "))
age4 = int(input("Enter the age of person 4: "))
if age1 > age2 and age1 > age3 and age1 > age4:
    print(f"The oldest person is person 1 with age: {age1}")
elif age2 > age1 and age2 > age3 and age2 > age4:   
    print(f"The oldest person is person 2 with age: {age2}")
elif age3 > age1 and age3 > age2 and age3 > age4:
    print(f"The oldest person is person 3 with age: {age3}")
elif age4 > age1 and age4 > age2 and age4 > age3:
    print(f"The oldest person is person 4 with age: {age4}")
else:
    print("All persons are of the same age")
'''

#wap for providing salary and year of service and calculate the bonus amount.

