from multiprocessing.dummy.connection import Listener


print("Hello")

# Operators
print(1+2)
print(3-2)
print(10/2)
print(1*2)
print(11%3)
print(11//3)
print(11**2)
amount=10

# Write the program for calculator
#result=0
val1=float(input('Enter the Value 1 :'))
val2=float(input('Enter the Value 2 :'))
op=input('Enter the any of the operator (+,-,*,/):')
if op=='+':
    result=val1+val2
elif op=="-":
    if val1>val2:
        result=val1-val2
    else:
        result=val1-val2
elif op=="*":
    result=val1*val2
elif op=='/':
    if val2==0:
        print('Pls enter the value other than 0')
    else:
        result=val1/val2
else:
    print('Pls enter the any of the other operator (+,-,*,/)')
print("The result is :", result)



#relational  --- <,>,<=,>=,!=,==
print(4>3)
print(5<=4)
print(5>=4)
print(10!=10)
print(4==3)

# assignment

a=10
b=10
print(id(a))
print(id(b))
print("Total value is:",a+b)

# identity   is, is not
a=10
b=20
print(a is b)
print(a is not b)

# membership
a="Python"
print("h" in a)
print('j' in a)
print('j' not in a)

# Enter value by user

#Count as string just concontation
n=input("Enter the value of n:")
m=input("Enter the value of m:")
print("Result is:", n+m)

#Convert in datatype like integer
n=int(input("Enter the value of n:"))
m=int(input("Enter the value of m:"))
print("Result is:", n+m)

radius=int(input("Enter the value of radius:"))
pi=3.14
area=pi*radius*radius
print("Result of Area is:", area)

p=int(input("Enter the principal amount"))
r=int(input("Enter the rate of interest"))
t=int(input("Enter the time duration"))
interest_result=p*r*t/100
print("Result of interest is:", interest_result)

pp=int(input('Enter the value'))
if(pp>=0):
    print('number is positive')
else:
    print('number is negative')

n=int(input("enter a number:"))
if(n<0):
    print("number is negative")
elif(n==0):
    print("number is zero")
else:
    print("number is positive")

n=int(input('Enter the value of n:'))
if(n%2==0):
    print("Number is even")
else:
    print('Number is odd')


n=int(input("Enter the value:"))
if(n>10):
    print('result is ok')
elif(n==10):
    print('good')
else:
    print('condition is not true')

# Loop
amount=10
while(amount>0):
    print("shopping",amount)
    amount=amount-1
    #amount=amount-1
    #amount-=2
   # amount*=3

x=5
y='Abhimanyu'
print(type(x))
print(type(y))

# Variables are case sensative

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

# Unpack Variable

#x=y=z='car'
car=('Maruti','Mahendra','Tata')
x,y,z=car
print(x)
print(y)
print(z)

x='Abhimanyu'
def myfunc():
        print('My Name is',x)
myfunc()

count = 10
while count > 0:
  print(count)
  count = count - 1

amount = 50
while (amount>=10):
    print("reverse",amount)
    amount -=1

# loop control statement - Jumping statement
for count in range(10,0,-1):
  print(count)

for i in range(10):
    if i ==5:
        break
    print(i)

for i in range(10):
    if i ==5:
        continue
    print(i)

for i in range(3,17):
    print(i+i)

for i in range(3,17):
    print(i+3, end=" ")

sum=0
for i in range(3,38):
    sum=sum+i
print("sum=", sum)

sum=0
while (i in range(3,38)):
    sum=sum+i
print(sum)

# print odd no. from range output in qube
for a in range(2,40):
    if(a%2==0):
        print('Cube of number is:',a*a*a)

for n in range(2,40):
    if(n%2==0):
        print("cube of number is-",n*n*n)


# Functions

def f1():
    print('hello')
f1()
    
def f3():
    for i in range(10):
        print(i)
f3()

def add(a,b):   #formal arguments
    return a+b

print(add(10,20))   #actual arguments


a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
def add1(a,b):
    return a+b
print(add1(a,b))

def f4(a,b=3):
    return a>b
print(f4(2,1))


#positional arguments

def f2(a,b):
    return a-b
print(f2(b=10,a=2))

#variable-length

def f3(a,*b):
    print("single variable",a)
    print('multiple values',b)
f3(10,20,30,40,50,60)


a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
def add1(a,b):
    return a+b

# print(add1(a,b))
if add1(a,b)>30:
    print("hello")
else:
    print('hi')

p=int(input("Enter the value of Principal Amount:"))
r=int(input("Enter the value of rate of interes:"))
t=int(input("Enter the value of time duration:"))
def c_inrst(p,r,t):
    return p* (pow((1+r/100),t))
print(c_inrst(p,r,t))

txt='Abhimanyu Singh'
#x=txt.capitalize()
x=txt.casefold()
print(x)

x=('tup1','tup2','tup3')
y=list(x)
y[1]='tup4'
x=tuple(y)
print(x)

List = ['r','a','E','d','S','F','O','R','b','d','E','T','S']
Sliced_List = Listener[5:]
print("\nElements sliced from 5th "
	"element till the end: ")
print(Sliced_List)

# To find the greater no. in list
L1 = [1,2,3,4]
for i in L1:
    if i>3:
        print('Greater No.', i)
    
n=int(input("enter number of elements::"))
L=[]
for i in range(n):
    x=int(input("Enter value:"))
    L.append(x)
print(L)
Greatest= L[0]
for i in range(1,n):
    if(L[i]>=Greatest):
        Greatest=L[i]
print("Greatest Element::", Greatest)


# prgram for division for 3 & 7 in List items

n=int(input("enter number of elements::"))
L=[]
for i in range(n):
    x=int(input("Enter value:"))
    L.append(x)
print(L)
N1= L[0]
for i in range(1,n):
    if(L[i]/3 and L(i)/7):
        N1=L[i]
print("Division Element::", N1)


l=[411,256,3,4,576]
n=0
for i in l:
    if(i%2==0):
        n=n+i
print(n)


