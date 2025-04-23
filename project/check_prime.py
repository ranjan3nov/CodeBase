while True:
    num = int(input("Enter a number :"))
    prime = True
    for i in range(2, num):
        if(num%1 ==0):
            prime = False

    if prime:
        print("This is prime")
    else:
        print("This is not a prime ")