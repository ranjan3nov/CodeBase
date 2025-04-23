num = int(input("Enter a natural number "))

n = 1;
sum = 0

while n<=num:
    sum = sum+n
    n +=1
print(f"The Sum of first {num} natural number is : {str(sum)}")