# Q.1 Write a program which will find factors of given number and find whether the factor is even or odd

def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
num = 320
print_factors(num)


# Q.2 Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically

my_str = "Hello this Is an Example With cased letters"
# To take input from the user
#my_str = input("Enter a string: ")
# breakdown the string into a list of words
words = [word.lower() for word in my_str.split()]
# sort the list
words.sort()
# display the sorted words
print("The sorted words are:")
for word in words:
   print(word)


# Q.3 Write a program, whichwill find all the numbers between 1000 and 3000 (both included) such that each digit of a number is an even number. The numbers obtained should be printed in a comma separated sequence on a single line
values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(",".join(values))


# Q.4 Write a program that accepts a sentence and calculate the number of letters and digits
s = input("Input a string")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)

# Q.5 Design a code which will find the given number is Palindrome number or not 

num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Number is not a palindrome!")