# List and Tuple examples

list1=[1,2,3,4,5,6,7,8]
sum=0
for i in list1:
    sum=sum+i
print(sum)


List = ['Mathematics', 'chemistry', 1997, 2000,10.2]
print(List)



List = ['Mathematics', 'chemistry', 1997, 2000,10.2]
print(List[2])
List2 = [1,2,3,35]
list3=[List,List2]
print(list3)
print(list3[1][3])

List = ['Mathematics', 'chemistry', 1997, 2000,10.2]
for i in List:
	# print(i)
	print(i,end=" ")


List = ['Mathematics', 'chemistry', 1997, 2000]

# Insert at index 2 value 10087
List.insert(2,10087)	
print(List)

l=[1,2,3,4]
l[2]=33
print(l)

List1 = [-1, 2, 3]
List2 = [2, 3, 4, 5]
# Add List2 to List1
List1.extend(List2)		
print(List1)

List = [1, 2, 3, 4, 5] 
list2 =[1,2]
print(List+list2)

List=[1,2,3,4]
print(sum(List))

List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.index(2))

List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.count(2))


List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(len(List))


List = [1, 2, 3, 1, 2, 1, 22, 2, 3, 2, 1]
print(List.index(22))

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
print(min(List))

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
print(max(List))


List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
#Reverse flag is set True
List.sort(reverse=True)
#List.sort().reverse(), reverses the sorted list
print(List)		


List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
print(List.pop())
print(List)

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
print(List.pop(1))
print(List)

List = [2.3, 4.445, 3, 5.33,3, 1.054, 2.5]
List.remove(3)
print(List)

# add element in list from user
n=int(input("enter number of elements::"))
L=[]
for i in range(n):
    x=int(input("Enter value:"))
    L.append(x)
print(L)


List = ['r','a','E','d','S','F','O','R','b','d','E','T','S']
# Print elements of a range
# using Slice operation
Sliced_List = List[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_List)

Sliced_List = List[5:]

print("\nElements sliced from 5th "
	"element till the end: ")
print(Sliced_List)

# Printing elements from
# beginning till end
Sliced_List = List[:]

print("\nPrinting all elements using slice operation: ")
print(Sliced_List)

List = ['R','D','E','K','S','F','N','W','N','Q','E','S']
print("Initial List: ")
print(List[6:])

# Print elements from beginning
# to a pre-defined point using Slice
Sliced_List = List[:-6]
print("\nElements sliced till 6th element from last: ")
print(Sliced_List)

Sliced_List = List[-6:-1]
print("\nElements sliced from index -6 to -1")
print(Sliced_List)

# Printing elements in reverse
# using Slice operation
Sliced_List = List[::-1]
print("\nPrinting List in reverse: ")
print(Sliced_List)

List = ['R','D','E','K','S','F','N','W','N','Q','E','S']
Sliced_List = List[::-2]
print("\nPrinting List in reverse: ")
print(Sliced_List)



# Tuple - stores multiple values and is imutable

Tuple1 = ('Welcome', 7.4, 'Steve',78)
print(Tuple1)
print(Tuple1[1])
print(Tuple1.index(7.4))

t=tuple(['kjbdvjhbdfvb',"kjbjhgjhj"])
print(t)

t=tuple(['kjbdvjhbdfvb',"kjbjhgjhj"])
print(t)

Tuple1 = tuple("jkgjhvjkvhkvg")
print(Tuple1)

Tuple1 = tuple("jkgjhvjkvhkvg")
Tuple2 = tuple(['python', 'greek'])
# print(type(Tuple2))
Tuple3 = (Tuple1, Tuple2)
print("Tuple with nested tuples: ")
print(Tuple3)

Tuple1=(4,) * 3
print("Tuple with repetition: ")
print(Tuple1)

a="steve"
b="for"
c="steve"
# list1=['steve']
# print(list1)
Tuple1=()
Tuple1=a,b,c
print(Tuple1)

Tuple1=('steve','for','steve')
a, b, c = Tuple1
print("\nValues after unpacking: ")
print(a)
print(b)
print(c)

Tuple1 = (0, 1, 2, 3)
Tuple2 = ('Steve', 'For', 'Steve','jhv','rthsh')


Tuple3 = Tuple1 + Tuple2
print(Tuple3)

Tuple1 = tuple('Conor Mcgregor')
print(Tuple1[2:6])
# # Removing First element
print("Removal of First Element: ")
print(Tuple1[1:])

# # Reversing the Tuple
print("\nTuple after sequence of Element is reversed: ")
print(Tuple1[::-1])

# # Printing elements of a Range
print("\nPrinting elements between Range 4-9: ")
print(Tuple1[4:9])

Tuple1 = (0, 1, 2, 3, 4)
del Tuple1
	
print(Tuple1)

aple = (123, 'xyz', 'zara', 'abc')
print(aple)
aList = list(aple)
print ("List elements : ", aList)


# Q. write program to count frequency of elements in tupletup1=(10,67,99,77,90,33,90,90,10,3,77,40)
flag=0
for i in range(0,len(tup1)):
    for j in range(i+1,len(tup1)):
        if tup1[i]==tup1[j]:
            flag+=1
            print("frequrncy of ",tup1[i],"is", flag)
print("frequrncy of rest is 1") 