class Dog:
	
	# Class Variable
	animal = 'dog'	
	
	# The init method or constructor
	def __init__(self, breed):
		
		# Instance Variable
		self.breed = breed			

	# Adds an instance variable
	def setColor(self, color):
		self.color = color
	
	# Retrieves instance variable	
	def getColor(self):	
		return self.color

# Driver Code
Rodger = Dog("pug")
Rodger.setColor("brown")
print(Rodger.getColor())

class Test:
	
	# A sample method
	def f1(self):
		print("hello")

# Driver code
obj = Test()
obj.f1()






# parent class
class Person:	
		# _init_ is known as the constructor		
		def __init__(self, name, idnumber):
				self.name = name
				self.idnumber = idnumber
		def display(self):
				print(self.name)
				print(self.idnumber)

# child class
class Employee( Person ):		
		def __init__(self, name, idnumber, salary, post):
				self.salary = salary
				self.post = post

				# invoking the _init_ of the parent class
				Person.__init__(self, name, idnumber)

				
# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")	

# calling a function of the class Person using its instance
a.display()





# Python example to show the working of multiple
# inheritance
class Base1(object):
	def __init__(self):
		self.str1 = "abc1"
		print("Base1")

class Base2(object):
	def __init__(self):
		self.str2 = "abc2"		
		print("Base2")

class Derived(Base1, Base2):
	def __init__(self):
		
		# Calling constructors of Base1
		# and Base2 classes
		Base1.__init__(self)
		Base2.__init__(self)
		print("Derived")
		
	def printStrs(self):
		print(self.str1, self.str2)
		

ob = Derived()
ob.printStrs()



class Person:
	
	# Constructor
	def __init__(self, name):
		self.name = name

	# To get name
	def getName(self):
		return self.name

	# To check if this person is an employee
	def isEmployee(self):
		return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

	# Here we return true
	def isEmployee(self):
		return True

# # Driver code
emp = Person("abc1") # An Object of Person
print(emp.getName(), emp.isEmployee())

emp11 = Employee("abc2") # An Object of Employee
print(emp11.getName(), emp11.isEmployee())