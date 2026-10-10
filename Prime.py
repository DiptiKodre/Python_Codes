n = int(input("Enter a number to check whethher it is prime or not : "))


if n<=1:
    print(n,"is not a prime number")

elif n == 2:
    print(n,"is a prime number")
    
elif n>=2:
    for i in range(2,n):
        if (n%i) == 0:
            print(n,"is not a prime number")
            break
        else:
            print (n, "is a prime number")
            break
else:
    print(n, "is not a prime number")
