from typing import List


amount=10
while(amount>0):
    print("shopping",amount)
    #amount=amount-1
    #amount=amount-1
    #amount-=2
    #amount*=3

a=int(input("Enter the value for list:"))
List1=[a]
for a in List:
    List1
    print(List1)

n=int(input("enter number of elements::"))
L=[]
for i in range(1,n+1):
    x=int(input("Enter value:"))
    L.append(x)
    print(L)


n=int(input("enter number of elements::"))
L=[]
for i in range(n):
    x=int(input("Enter value:"))
    L.append(x)
print(L)
L2=[]
for j in L:
    if(j%2==0):
        L2.append(j)
print("List of even numbers=",L2)