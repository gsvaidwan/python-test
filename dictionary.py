d={1:2,3:4,5:6}
# n=int(input("Enter the key to be checked:"))
for i in d:
    print(i,':',d[i])


#Check the key is exist or not from user
d={1:2,3:4,5:6}
n=int(input("Enter the key to be checked:"))
for i in d:
    if n==d:
        print("present")
        break
    else:
        print("not present")


a={}
for  x in range(3):
	k=input('enter new key:')
	v=input('enter new value:')
	a[k]=v
print(a)



d={1:2,3:4,5:6}
n=int(input("Enter the key to be checked:"))
# print(d)
# print(d[3])
flag=0
for i in d:
	# print(i)
	if(i==n):

		flag=1
		break
		# print(i, "is present in the dictionary")
	# print(i,":",d[i])
if flag==0:
	print ("not present")
else:
	print("present")



Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Steve',
		'A' : {8 : 'Steve', 2 : 'For', 3 : 'Steve'},
		'B' : {1 : 'Steve', 2 : 'Life'}}
# Deleting a Key value
del Dict[6]
print("Deleting a specific key: ")
print(Dict)


Dict = {1: 'Steve', 'name': 'For', 3: 'Steve'}

# Deleting a key
# using pop() method
pop_ele = Dict.pop(3)
print(pop_ele)
print(Dict)


Dict = {1: 'Steve', 'name': 'For', 3: 'Steve'}

# Deleting an arbitrary key
# using popitem() function
pop_ele = Dict.popitem()
print(pop_ele)
print(Dict)


Dict = {1: 'Steve', 'name': 'For', 3: 'Steve'}


# Deleting entire Dictionary
Dict.clear()
print("\nDeleting Entire Dictionary: ")
print(Dict)


original = {1:'abc', 2:'def'}

# copying using copy() function
new = original.copy()
print(new)

# removing all elements from the list
# Only new list becomes empty as copy()
# does shallow copy.
# new.clear()
original.clear()
print('new: ', new)
print('original: ', original)




original = {1:'one', 2:'two'}

# copying using =
new = original
del new[1]
# removing all elements from new list
# and printing both
# new.clear()
print('new: ', new)
print('original: ', original)

text1 = {1: "efgs", 2: "for"}
text2 = text1

# Using clear makes both text1 and text2
# empty.
text1.clear()

print('After removing items using clear()')
print('text1 =', text1)
print('text2 =', text2)

text1 = {1: "one", 2: "two"}
text2 = text1

# This makes only text1 empty.
text1 = {}

print('After removing items by assigning {}')
print('text1 =', text1)
print('text2 =', text2)


Dictionary1 = { 'A': 'dict1', 'B': 'For' }
Dictionary2 = { 'B': 'dtyjdtyj46745785' }

# Dictionary before Updation
print("Original Dictionary:")
print(Dictionary1)

# update the value of key 'B'
Dictionary1.update(Dictionary2)
print("Dictionary after updation:")
print(Dictionary1)



Dictionary1 = {'A':'Steve', 2:'For', 'C':'For'}
print(Dictionary1.values())
print(Dictionary1.keys())




lis = [{ "name" : "Nandini", "age" : 20},
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]

# using sorted and lambda to print list sorted
# by age
print ("The list printed sorting by age: ")
print (sorted(lis, key = lambda i: i['age']))




# Set


set1={1,2,3,4,5,6,6}
print(set1)

set1=set((1,2,3,4,5,5))
print(set1)

string="python"
l=list(string)
t=tuple(string)
s=set(string)
print(l)
print(t)
print(s)

set1 = set("iufitfyif")
# set1=set([1,2,3,4,1,2,3])
print("\nSet with the use of String: ")
print(set1)

set1 = set(["shdfhy", "shdrthv", "srhrths","srhrths"])
print("\nSet with the use of List: ")
print(set1)

set1={1,2,3,4,5,5}
for i in set1:
	print(i)

# add the no. of range in set
set1=set()
for i in range(10, 51):
	set1.add(i)
print("Set after Addition of elements from 1-5: ")
print(set1)

set1 = set([ 4, 5, (6, 7)])
set1.update((10, 11))
print("\nSet after Addition of elements using Update: ")
print(set1)

#set1=set((1,2,3,4,5,5))
set1=set()
n=int(input('Enter the value :'))
for i in set1:
	print(i)



set1 = set([156, 2, 33, 4, 5, 6, 7, 8,5, 9, 10, 11, 12])
print("Initial Set: ")
print(set1)

print(set1.pop())
print(set1)


set1 = set([156, 2, 33, 4, 5, 6, 7, 8,5, 9, 10, 11, 12])
set1.remove(5)
# set1.remove(6)
print("\nSet after Removal of two elements: ")
print(set1)


set1 = set([156, 2, 33, 4, 5, 6, 7, 8,5, 9, 10, 11, 12])
set1.remove(55)
# set1.discard(98687)
print("\nSet after Discarding two elements: ")
print(set1)

#Creating a set
set1 = set([1,2,3,4,5])
print("\n Initial set: ")
print(set1)
