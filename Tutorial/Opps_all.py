# Object Orientate ..
# Here we create class , Constructor and so..

class Employee():
    company = "Funimation"  # this Is A class attribute
    salary = 5000
    bonus = 500

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"the Employee with name of {self.name} will Cum in Our Company")

    # dont have to define all variable which use,,,
    def printDetails(self): # this self variable have to pass,, self indicate the instance .... Like telling print the details of the self's
        print(f"Employee Details\n the Name of the employee is: {self.name}, and id is : {self.id}")
    
    # We can Other parameters except Self but still then Self have to pass
    def funtion(self,number):
        print(f"Hello Trash People! I,{self.name} Form Now on Rule Over all of you Till {number}")
    
    @staticmethod  # Use this Create Static Method which don;t take any parameters
    def greet():
        print("hallo My Asshole Co-Worker")
    
    # We Can Create Method that Change the Class Attributes not Instance
     # def changeSalary(self, sal): # this Also Do same but Not Use
    #     self.__class__.salary = sal

    @classmethod
    def changeSalary(cls, money):  # in Class method pass 'cls' as self
        cls.salary = money

    # this Also Work Like getter 
    @property  # Usin this, can Change any method to property.. It Work Like a property
    def totalSalary(self):
        return self.salary + self.bonus

    # setter --- as totalSalary is property NOw then it Take value also As property....
    @totalSalary.setter
    def totalSalary(self, monthSalary):  
        self.bonus = monthSalary - self.salary  #  it do  : what value given to totalSalary , the bonus will adjust Corresponding that As The salary fixed


'''
# Create the Object of the CLass    
employee1 = Employee() #--> Create the instance of the class .. when Constructor not present
employee2 = Employee()  

employee1.name  = "Souze"
employee1.id = 1
employee1.funtion(10)
employee1.printDetails() # This syntax originally look -> Employee.printDetails(employee1) : self::employee1


print(employee1.company)
print(employee2.company) # both Shown as it Predefine
Employee.company = "Chunchlyroll"
print(employee1.company)  # -----> Here Direct Change the class Attribute
print(employee2.company) 

print(employee1.salary)
print(employee2.salary)
# ----> Now Only CHange the Instance Attributes....
employee1.salary =10000
employee2.salary = 10100
print(employee1.salary)
print(employee2.salary)


# Normally if We don't use self parameters in any function at define time, then it will show ERROR, 
# But if we want to crete a Void function (like Greet())which dont take any parameters and don't return anything only print ,,,
### ---> For those functions ,,, we have to create them as static Method 
# FOr that Use this --> @staticmethod
# => At Calling time if this Don't have upper Syntax then it show error
employee1.greet() 


# ----------------Constructor : as u know ,crate with this: __init__(parameters) ===========

employee3 = Employee("Akane", 20)
employee3.id = 69
# employee3.printDetails()

# print(f"Salary of Akane : {employee3.salary}")
# print(f"Salary which Set in Employee Class: {Employee.salary}")
# # Change the Salary Attribute Of Class not This instance
# employee3.changeSalary(3000)  #::--> Employee ka Salary ka Value 3000 ho gya 
# print(f"Salary of Akane : {employee3.salary}")
# print(f"Salary which Set in Employee Class: {Employee.salary}")

#================= PROPERTIES =================
#--------------- Getter and setter -------------------

print(f"Before set the totalSalary, the salary is: {employee3.salary}")
print(f"Before set the totalSalary, the Bonus is: {employee3.bonus}")
#setter 
employee3.totalSalary = 6000
# getter
print(employee3.totalSalary) # it Define As Function but can use it as Property

# As the totalSalary given the Bonus also Calculates Per employee/Instance
print(f"AFter set the totalSalary, the salary is: {employee3.salary}")
print(f"AFter set the totalSalary, the Bonus is: {employee3.bonus}")
'''


class Sample: 
    def __init__(slf, name):
        slf.name = name

obj = Sample("Harry") 
print(obj.name) 
# Even If we Change the self to Slf or anything else it will not effect just have to present something in that take self's place

'''

'''
# 1. -------==> Single Inheritance
class ParentClass():
    location = 'Chaipat,Daspur2,Ps'
    def __init__(self, name,age):
        self.name = name
        self.age = age
        print(f"the Name is {self.name}, age is {self.age}")

    @staticmethod
    def greet():
        print("From Parent Class")

class ChildClass(ParentClass): # in this wat Can Inherit Other Classes
    language = "Python"

    def getLanguage(self):
        print(f"The language is {self.language}")
    
    def __init__(self, name, age,year):
        super().__init__(name, age)  # Using Super() Call The Constructor of parent class..
        self.year = year
        print(f"I study in Collage in {self.year} on {self.language}")

child = ChildClass("soumyajit", 19, 2)
child.greet()

# 2. -------==> Multiple Inheritance -- One child inheriting from more than one parent

class Father1():
    pass

class Father2():
    pass


 #Which One Write First in (Bracket ) That one get More priority in Case Of OverWrite Attribute or Method
class ChildClass(Father1, Father2): # this Child Class Inherits from 2 class ;;; SO this class can Use Both Class Method ... 
    pass


# 3. -------==> MultiLevel Inheritance -- Tree Type -- grandpa -> Father -> children

class GrandParent:
    country = "India"

    def __init__(self):
        print("I am Grand PArent ...\n")

    def takeBreath(self):
        print("I am Grand parent so breathing...")
    
    @staticmethod
    def Moan():
        print(" OwO OmO :)")

class Parent(GrandParent):
    company = "Honda"

    def __init__(self):
        super().__init__() # --> It called Grandparent constructor
        print("I am FAther...\n")

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    
    def takeBreath(self):
        super().takeBreath() # --> Called The takeBreath method of Grand class
        print("I am Father so I am Have heavy breath..")

class ChildClass(Parent): # this Class Also Access all Method
    company = "Fiverr"

    def __init__(self):
        super().__init__()  #--> It Called Parent Class Constructor
        print("I am Child...\n")

    def getSalary(self):  # Override the Method
        super().Moan() # Called Method of GrandParent class 
        print(f"No salary to programmers")
    
    def takeBreath(self):
        super().takeBreath()
        print("I am a Child so I am breathing++..")

# p = GrandParent()
# p.takeBreath() 

# e = Parent()
# e.takeBreath() 

pr = ChildClass() 
pr.takeBreath() 
pr.getSalary()

#+====================== Operator Overloading =================
#by Using Dunder

class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):  # Used for Add other instances's properties with own of same class
        print("Lets add")
        return self.num + num2.num

    def __sub__(self, num2):
        print("Lets multiply")
        return self.num - num2.num

    def __mul__(self, num2):
        print("Lets multiply")
        return self.num * num2.num

    def __truediv__(self, num2):
        print("Lets multiply")
        return self.num / num2.num

    def __floordiv__(self, num2):
        print("Lets multiply")
        return self.num // num2.num
    
    def __str__(self):
        return f"Decimal Number: {self.num}"
    
    def __len__(self):
        return 1

n1 = Number(17)
n2 = Number(6)
sum = n1 + n2
mul = n1 * n2
floorDivision = n1 // n2
print(floorDivision)
print(n1)
print(sum)
print(mul)
print(len(n1))

# {{{{{{{{{{{{{{{{{{ Example }}}}}}}}}}}}}}}}}}

class Vector:
    def __init__(self, vec):
       self.vec = vec
    
    def __str__(self):
        str1 = "" 
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index +=1
        return str1[:-1]

    def __add__(self, vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)
    
    def __mul__(self, vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum
    
    def __len__(self):
        return len(self.vec)

v1 = Vector([1, 4, 6, 6])
v2 = Vector([1, 6, 9])
print(len(v1))
print(len(v2))