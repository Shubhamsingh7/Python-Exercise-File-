# Program to use Filter map and Reduce

from functools import reduce

a=[]#Decaring a list

n=int(input("Enter the Size of List:"))

for i in range(n):
    a.append(int(input("Enter Value:")))

print(f"List is {a}")
#  use filter method to filter all number greater then 20

great=list(filter(lambda k:k>20,a))
print(f"Result using Filter is {great}")


# Find the Cube of all the Number using map

cube=list(map(lambda k:k**3,great))
print(f"Cube of List items are {cube}")

# Use Reduce Function to find product of list

product=reduce(lambda i,j:i*j,cube)
print(f"Product of list Cube is {product}")