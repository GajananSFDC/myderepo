# Databricks notebook source
Players = ["Sachin","Rickey","Saurav","Adam","Danial"]
for x in Players:                                               #For Loop 
    print(x)

# COMMAND ----------

Players = ["Sachin", "Rickey", "Saurav", "Adam", "Danial"]
for x in Players:
    if x == "Sachin":
        break
print(x)

# COMMAND ----------

for x in range(3, 20, 5):           # 3 is starting point 20 is ending point and 5 is the difference in between
    print(x)

# COMMAND ----------

for x in range(0, 10):              # Range from 0  to 9 
    if x == 5:                      #it will stop before 5(because it start from 0 )
        break
    print(x)
else:
    print("Print Anything")

# COMMAND ----------

#Nested Loop 

color = ["Red", "yellow","White"]
flower = ["Rose", "Lily", "MaryGold"]

for x in color:
    for y in flower:
        print(x,y)

# COMMAND ----------

# MAGIC %md
# MAGIC # Functions in Python

# COMMAND ----------

def greet(name):
    return f"Hello, {name}!"

print(greet("Gaju"))


# COMMAND ----------

name = input("Enter Your Name")                 #Taking Input From User
print("Hello", name)


# COMMAND ----------

name = input("Enter Your Name")
print (f"Hello, {name}!")

# COMMAND ----------

#Lambda Function 
add = lambda a,b:a+b
print(add(24,52))

# COMMAND ----------

u_input = input("Enter your name:")
print("Your name is :", u_input)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Lambda Function 

# COMMAND ----------

print("We Will do Calculation Using Lambda Function")
add = lambda a,b: a+b
sub = lambda a,b:a-b
mult = lambda a,b:a*b
divide = lambda a,b:a/b
print(add(12,20))
print(sub(20,10))
print(mult(5,5))
print(divide(50,5))

# COMMAND ----------

class MyFirstClass:
    var = "Gajanan"
print(type(MyFirstClass))

# COMMAND ----------

# MAGIC %md
# MAGIC ## Class and Object

# COMMAND ----------

class Flower:
  def __init__(self,name,colour):   #self is Keyword which refer to current Object 
    self.name = name
    self.colour = colour

obj1 = Flower("Rose","Pink")
print("The Name Of Flower is:-", obj1.name)
print("The Colour of That Flower is:-", obj1.colour)

obj2 = Flower("MaryGold","Yellow")
print("The Name Of Second Flower is:-", obj2.name)
print("The Colour of Second Flower is:-", obj2.colour)


# COMMAND ----------

class Flower:
  def __init__(name,colour):             #We Can Skip the Self Keyword if and Only if Single Object is there in Program
      
    obj1 = Flower("Rose","Pink")
print("The Name Of Flower is:-", obj1.name)
print("The Colour of That Flower is:-", obj1.colour)



# COMMAND ----------

class Calculator:
    def add(self, a, b):
        result = a + b
        print("Addition is:", result)

# Create an object of Calculator
calc = Calculator()

# Call the add method
calc.add(15, 62)
