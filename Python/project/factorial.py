# n! = 1X2X3X.....X n 
num = int(input("Enter a number : "))

fact = 1
# using While Loop
""" while(num != 1):
    fact = fact * num
    num = num - 1
print(f"The factorial of {num} is {fact}") """

#using for in range

for i in range(1, num+1):
    fact = fact*i
print(f"The factorial of {num} is {fact}")