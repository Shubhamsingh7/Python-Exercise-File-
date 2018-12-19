# Function to print Cube and Square of number from 1 to 100 Using Lambda Function


cube=lambda a:a**3

square=lambda a:a**2




for i in range(1,101):
    print(cube(i),end=" ")
print()
for i in range(1, 101):
    print(square(i),end=" ")