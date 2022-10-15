
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