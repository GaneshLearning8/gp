#eliglibe for vote
# input age
age = int(input("Enter Age : "))
# condition to check voting eligibility
if age >= 18:
    print("You are Eligible for Vote.")
else:
   print("You are Not Eligible for Vote.")

#Even or Odd
num = int(input("Enter number to check even or odd:"))
if num % 2 == 0:
     print(num, "is Even")
        # print("{0} is Even".format(num)) 
else:
    #    print("{0} is Odd".format(num))
    print(num, "is odd")

# Python program to check if year is a leap year or not

year = int(input("Enter a year to verify a leap or not: "))
if (year % 400 == 0) and (year % 100 == 0):
    print(year,"is a leap year")
elif (year % 4 ==0) and (year % 100 != 0):
    print(year,"is a leap year")
else:
    print(year, "is not a leap year")


# Basic calculator program in Python using while loop

print("Calculator Options:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

selectedOption = input("choose calculator options from (1-4): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if selectedOption == "1":
        result = num1 + num2
        operation = "+"
elif selectedOption == "2":
        result = num1 - num2
        operation = "-"
elif selectedOption == "3":
        result = num1 * num2
        operation = "*"
elif selectedOption == "4":
        result = num1 / num2
        operation = "/"
else:
    print("Invalid choice!")


 
print(num1 ,operation, num2 ,"=", result)
  