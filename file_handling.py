
file = open("C:\\Users\\gajen\\OneDrive\\Desktop\\data.txt", "r")
print(file.read())

file=open('C:\\Users\\gajen\\OneDrive\\Desktop\\data.txt','r')
for s in file:
    print (s)



f=open("demo_a.txt","w")
data=f.write("this is the write mode.")
f1=open("demo_a.txt","r")
print(f1.read())

file = open("demo.txt", "r")
print (file.read(5))



file = open('demo_a.txt','a')
file.write(" . stp'gmskobnbbnsj")
file=open('demo_a.txt','r')
print(file.read())
file.close()


# Kamajeet code for password manager
file= open("pass_handling1.txt",'a')
T=input("Do you want to enter values y/n::")
while T=='y':
    file.write("\nURL=")
    file.write(input("enter URL::"))
    file.write("  User Name::")
    file.write(input("enter username::"))
    file.write("  Password::")
    file.write(input("enter password::"))
    T=input("Do you want to enter more values y/n::")
file=open('pass_handling1.txt','r')
print(file.read())
file.close()


# nikhil Code for password manager
u = input("Enter the username:")
p = input("Enter the password:")
url = input("Enter the url:")
str = "username: "+u+ " password: " +p+ " url: "+url
file = open('pwd_manager.txt','a')
file.write(str)


with open("demo.txt") as file:
	data = file.read()
	print(data)

f1=open('demo.txt','r')
print(f1.readlines())



f = open("demo.txt", "r")
for i in f.read():
   x = open("demo1.txt", "a")
   x.write(i)

fil = open("demo1.txt", "r")
print(fil.read())

# open and write file 'with' keyword
with open("demo1.txt", "w") as f:
	f.write("writing with 'with' keyowrd")


# Write in a file with next line
L = ["I\n", "Love\n", "Python\n"]
# writing to file
file1 = open('myfile.txt', 'w')
file1.writelines(L)
file1.close()



L = ["I\n", "Love\n", "Python\n"]
with open("filename", 'w') as file:
    text = file.read().strip().split()
    len_chars = sum(len(word) for word in text)
    print(len_chars)


file = open("demo.txt", "r")
data = file.read()
count = len(data)
print('Number of characters in text file :', count)


file = open("demo.txt", "rt")
data = file.read()
words_count= data.split()
print('Number of words in text file :', len(words_count))



# Open the file in write mode
f1 = open("demo.txt", "w")

# Open the input file and get
# the content into a variable data
with open("demo1.txt", "r") as myfile:
	data = myfile.read()

# For Full Reversing we will store the
# value of data into new variable data_1
# in a reverse order using [start: end: step],
# where step when passed -1 will reverse
# the string
data_1 = data[::-1]

# Now we will write the fully reverse
# data in the output1 file using
# following command
f1.write(data_1)
f1.close()


File = open("second.txt", "w") 
with open("pass_handling1.txt", "r") as File1: 
    txt = File1.read() 
rev = txt[::-1] 
File.write(rev) 
File.close()






def fun(a):
	if a <= 3:
		# throws ZeroDivisionError for a = 3
		b = a/(a-3)

	# throws NameError if a >= 4
	print("Value of b = ", b)
	
try:
	# fun(5)
	fun(3)

# note that braces () are necessary here for
# multiple exceptions
except ZeroDivisionError:
	print("ZeroDivisionError Occurred and Handled")
except NameError:
	print("NameError Occurred and Handled")






def f1(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print ("a/b result in 0")
	else:
		print (c)

# Driver program to test above function
# f1(2.0, 3.0)
f1(3.0, 3.0)



try:
	k = 5//2 # raises divide by zero exception.
	print(k)

# handles zerodivision exception
except ZeroDivisionError:
	print("infinite value")

finally:
	# this block is always executed
	# regardless of exception generation.
	print('This is always executed')




def divide(x, y):
    try:
            # Floor Division : Gives only Fractional Part as Answer
        result = x // y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")

    # Look at parameters and note the working of Program
divide(3, 2)





def divide(x, y):
	try:
		# Floor Division : Gives only Fractional Part as Answer
		result = x // y
		print("Yeah ! Your answer is :", result)
	except ZeroDivisionError:
		print("Sorry ! You are dividing by zero ")

# Look at parameters and note the working of Program
divide(3, 0)



try:
	print("code start")
		
	# unsafe operation perform
	print(1 / 0)

# if error occur the it goes in except block
except:
	print("an error occurs")

# final code in finally block
finally:
	print("Done")





# try for unsafe code
try:
	amount = int(input("Enter the amount to be withdrawn:"))
	acc=6000
	if acc-amount < 2000:
		
		# raise the ValueError
		raise ValueError("please add money in your account")
	else:
		print("You are eligible to purchase DSA Self Paced course")
			
# if false then raise the value error
except ValueError as e:
		print(e)
finally:
	print("Thanks")





try:
	a = 10/2
	print (a)
except ArithmeticError:
		print ("This statement is raising an arithmetic exception.")
else:
	print ("Success.")




try:
	a = [1, 2, 3]
	print (a[3])
except LookupError:
	print ("Index out of bound error.")
else:
	print ("Success")



# try:
#     num=3
#     c= num % 2 ==0
    
# except LookupError:
# 		print (c,"Negative Number")
# else:
# 	print ("Number Check Success.")


def f1(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print ("a/b result in 0")
	else:
		print (c)

# Driver program to test above function
# f1(2.0, 3.0)
f1(3.0, 3.0)

try:
	k = 5//2 # raises divide by zero exception.
	print(k)

# handles zerodivision exception
except ZeroDivisionError:
	print("infinite value")



