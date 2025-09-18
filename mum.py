# 1 week day
day=int(input("enter the name:"))
if(day==1):
    print("monday")
elif(day==2):
    print("tuesday")
elif(day==3):
    print("wednesday")
elif(day==4):
    print("thursday")
elif(day==5):
    print("friday")
elif(day==6):
    print("sartday")
elif(day==7):
    print("sunday")
else:
    print("error")
# 2write a python program to check the age

n=int(input("entern the age:"))
if n>12:
    print("child")
elif n>12 and n<12:
    print("teen")
else:
    print("adult")

#3write a python program to get the input from user and printing 
num1=input("enter the first num:")
num2=input("enter your secound num:")
print("first num:",num1)
print("secound num:",num2)


#4 to print name
print("munvar")

#5 get theinput from the user add two num
num3=int(input("enter the third num"))
num4=int(input("enter the fourth num"))
sum=num3+num4
print("sum of two num:",sum)

#6primitive data types
a=10
b=2.33
c=True
print("integer is :",a)
print("float is :",b)
print("boolean is :",c)

#7non primitive data type
a=(10,20,30)
b=[10,20,30]
c={10,20,30}
dict1={"one":1,"two":2}
print(a)
print(b)
print(c)
print(dict1)

#8square of anum
a=int(input("enter the num:"))
b=a**2
print(b)

#9 avg of three num
num0=int("enter the num0:")
num9=int("enter the num9:")
num8=int("enter the num8:")
avg=num0+num9+num8/3

# 10 take the num as any user and multiply by 10
num=int(input("enter a num:"))
mult=num*10
print(mult)

#11 nim to sec
a= int(input())
sec=a*60
print(sec)

#12 floating point
a=float(input(""))
b=float(input(""))
num=a*b
print(num)

#13 large of three num
num1=int(input("enter the 1 num:"))
num2=int(input("enter the 2 num:"))
num3=int(input("enter the 3 num:"))
largest=max(num1,num2,num3)
print("largest num:",largest)

#14 arthimatic operator
a=10
b=20
c=30
print("additon of two numbers:",a+b)
print("multipication of two numberas:",a*b)
print("subtraction of two numbers:",a-b)
print("division of two numbers:",a/b)

#15 logical operator
a=10
b=20
print(a>0 and b>15)
print(a>15 and b<5)
print(not(a==10))

#16 grading marks
m = int(input("Enter your marks: "))
if m >= 90:
    print("Grade A")
elif m >= 80:
    print("Grade B")
elif m >= 60:
    print("Grade C")
elif m >= 50:
    print("Grade D")
else:
    print("FAIL")

 #17 Program to check username and password credentials
 user = "munvar"
password = 1234
username = input("Enter your username: ")
if username != user:
    print("Invalid username")
else:
    password_input = int(input("Enter your password: "))
    if password_input == password:
        print("Login successful")
    else:
        print("Invalid password")

 # 18 Simple Calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Choose operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
n = int(input("Enter the operation number (1-4): "))
if n == 1:
    print("Result:", a + b)
elif n == 2:
    print("Result:", a - b)
elif n == 3:
    print("Result:", a * b)
elif n == 4:
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error! Division by zero.")
else:
    print("Invalid operation number")

#19 write a python program to print the days_months
m = int(input("Enter the month number (1-12): "))
if m == 2:
    print("28 or 29 days")
elif m in [1, 3, 5, 7, 8, 10, 12]:
    print("31 days")
elif m in [4, 6, 9, 11]:
    print("30 days")
else:
    print("Invalid month number")

# 20 positive and negitive and zero
a=int(input("enter a num"))
if(a>0):
    print("+positive")
if(a<0):
    print("negitive")
elif(a==0):
    print("zero")

#21 odd and even number
a=int(input("enter the num:"))
if(a%2==0):
    print("even")
else:
    print("odd")

#22 theory marks
theory_marks=int(input("enter theory marks:"))
partical_marks=int(input("enter pratical marks:"))
total_mark= theory_marks+partical_marks
if (theory_marks>=35,
partical_marks>=50 and total_mark>60):
    print("student passed")
else:
    print("student failed")

#23 Write a python  programee get a input from user swap 2 numbers withour 3rd variable
a=10
b=20
a=a+b
b=a-b
print("a",a)
print("b",b)

#24 Write a python  programee get a input from user swap 2 numbers withour 3rd variable
a=10
b=20
temp=a
a=b
b=temp
print("after swapping:",a)
print("after swapping:",b)

#25write a python to square of a number
a=int(input("Enter a number:"))
Square=a*a
print("Square of a number:",Square)

#26find the avg of 3 number you have to get input from the user
a=float(input("Enter First Number:"))
b=float(input("Enter Second Number:"))
c=float(input("Enter Third Number:"))
avg=(a+b+c)/3
print("Average is:",avg)

#27write a python program to take a num as any user and multiplied by 10
a=int(input("Enter a number:"))
b=a*10
print("After multipying with 10:",b)

#28 write a python program to floating points
a=float(input("Enter First Number:"))
b=float(input("Enter Second Number:"))
Product=a*b
print("Product=",Product)

#29 sum of first n natural number
n=(int(input("Enter input=")))
sum=n*(n+1)
print("Sum=",sum)

#30write a python program to check the number is divisible by 5 and 11
a=int(input("enter the number"))
if (a%5==0 and a%11==0):
    print("the number is divisible by 5 and 11")
else:
    print("the number is not dividible")


    
    


