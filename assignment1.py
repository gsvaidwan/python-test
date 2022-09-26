# Question 1 -  Arthmatic Operators

a=10
b=5
add=a+b
sub=a-b
mul=a*b
div1=a/b
div2=a//b
mod=a%b
power=a**b

print(add,sub,mul,div1,div2,mod,power)

# Question 2 - swaping the value of two variables

a=10
b=5
a,b=b,a
print('a =',a)
print('b =',b)

# Question 3

w = 2
x = 5
y = 7

a = w + y
b = y - w
c = y % x
d = y // w
e = y ** w
f = w * x
g = y / x
print(a,b,c,d,e,f,g)

# Question 4

x=int(input('Enter the first no'))
y=int(input('Enter the second no'))
z=x//y
print('Value is:',z)

# Question 5

x=int(input('Enter the first no'))
if(x%2==1):
    print('Value is odd')
else:
    print('valie is even')

# Question 6

a = True
b = False
print(not(a))
print(not(b))
a = False
b = False
x = not(a)
y = not(b)
print(a or b)
print(x or y)
print(a or x)
print(x or b)
a = False
b = False
x = not(a)
y = not(b)
print(a and b)
print(a and x)
print(y and b) 
print(x and y)

# Question 7
a = 1
b = 20
if a < 10:
    print('Demo string 1')
else:
 print('Demo string 2')

a = 1
b = 20
if a < 10 or b == 20:
 print('Demo string 1')
else:
 print('Demo string 2')
 
a = 1
b = 20
if a < 10 and not(b == 20):
 print('Demo string 1')
else:
 print('Demo string 2')
