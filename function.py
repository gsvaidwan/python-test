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



p=int(input("enter the value:"))
r=int(input("enter the value:"))
t=int(input("enter th evalue:"))
def amount(p,r,t):
    return (p(1+r/100)^t)
print(amount)


p=int(input("Enter the value of Principal Amount:"))
r=int(input("Enter the value of rate of interes:"))
t=int(input("Enter the value of time duration:"))
def c_inrst(p,r,t):
    return p* (pow((1+r/100),t))
print(c_inrst(p,r,t))


def CI(p,r,t):
    c=0
    c = p*(1+ (r/100))**t
    return c

print(CI(100,3,2))



p= int(print("Enter principal amount:"))
r= int(print("Enter rate:"))
t= int(print("Enter time:"))
def com_int(p,r,t):
    ci= int(p*((1+r/100)**t))
    return ci
a= com_int(p,r,t)
print("compount interest::",a)



p= int(input("Enter principal amount:"))
r= int(input("Enter rate:"))
t= int(input("Enter time:"))
def com_int(p,r,t):
    ci= p*((1+r/100)**t)
    return ci
a= com_int(p,r,t)
print("compount interest::",a)



p = int(input("enter principal amt: "))
r = int(input("enter rate of interest: "))
t = int(input("enter time period: "))
def amount(p,r,a):
 ci=p*(1+(r*.01))**t
 print("CI")
print(amount(p,r,t))



def cube(x): 
	return x*x*x

cube_v2 = lambda x : x**3

print(cube_v2(3))


print(cube(3))

M = lambda a, b : a if(a > b) else b

print(M(1, 2))



def f1(n):
	
	if (n == 0):
		return 1
	else:
		return n * f1(n-1)
	
# print the result
print(f1(7))