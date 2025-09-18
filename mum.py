
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
# 3write a python program to check the age

n=int(input("entern the age:"))
if n>12:
    print("child")
elif n>12 and n<12:
    print("teen")
else:
    print("adult")

#2write a python program to get the input from user and printing 
num1=input("enter the first num:")
num2=input("enter your secound num:")
print("first num:",num1)
print("secound num:",num2)


#3 to print name
print("munvar")

#4 get theinput from the user add two num
num3=int(input("enter the third num"))
num4=int(input("enter the fourth num"))
sum=num3+num4
print("sum of two num:",sum)

#5primitive data types
a=10
b=2.33
c=True
print("integer is :",a)
print("float is :",b)
print("boolean is :",c)

#6non primitive data type
a=(10,20,30)
b=[10,20,30]
c={10,20,30}
dict1={"one":1,"two":2}
print(a)
print(b)
print(c)
print(dict1)

#7square of anum
a=int(input("enter the num:"))
b=a**2
print(b)

#8 avg of three num
num0=int("enter the num0:")
num9=int("enter the num9:")
num8=int("enter the num8:")
avg=num0+num9+num8/3

# 9 take the num as any user and multiply by 10
num=int(input("enter a num:"))
mult=num*10
print(mult)

#10 nim to sec
a= int(input())
sec=a*60
print(sec)

#11floating point
a=float(input(""))
b=float(input(""))
num=a*b
print(num)

#12large of three num
num1=("enter the 1 num")
num2=("enter the 2 num")
num3=("enter the 3 num")
largest=max(num1,num2,num3)

#13 arthimatic operator
a=10
b=20
c=30
print("additon of two numbers:",a+b)
print("multipication of two numberas:",a*b)
print("subtraction of two numbers:",a-b)
print("division of two numbers:",a/b)

#14 logical operator
a=10
b=20
print(a>0 and b>15)
print(a>15 and b<5)
print(not(a==10))



