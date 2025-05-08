# Databricks notebook source
# Program to Print 1 to N numbers

N = int(input("Enter the Number of N:-"))    #input() से जो इनपुट आता है वो string होता है, इसलिए उसे int() से integer में बदला गया है।
for i in range(1, N + 1):        # if we specify N then it will only print till N-1
    print(i)

# COMMAND ----------

#Program to Print REVERSE of N to 1 numbers?

N = int(input("Enter the Number to Print:-"))
for i in range(N, 0, -1):
    print(i)

# COMMAND ----------

# Program to display Sum of 1 to N Numbers 

N = int(input("Enter the Number:-"))

total = 0

for i in range(1, N + 1):
    total += i
print("The Sum of Number from 1 to", N, "is:-", total)

# COMMAND ----------

#Program to check given number is EVEN or ODD?

N = int(input("Enter The Number:-"))
if N % 2 == 0:
    print("Entered Number is Even")
else:
    print("Entered Number is Odd")


# COMMAND ----------

#Program to display PRIME NUMBERS from 1 to n? 

N = int(input("Enter the Number"))

print("Prime Number from 1 to", N, "are:-")
for num in range(2, N + 1):
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)

# COMMAND ----------

#Program to check whether the given number is PRIME or not? 

N = int(input("Enter the Number:-"))
if num <= 1:
    print(num, "is not a Prime Number")
else:
    is_prime= True
for i in range(2, int(num ** 0.5)+ 1):
    if num % i == 0:
        is_prime = False
        break
    if is_prime:
        print(num,"Is a Prime Number.")
    else:
        print(num, "Is Not a Prime Number")