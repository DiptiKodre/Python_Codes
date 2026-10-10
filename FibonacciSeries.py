def fibo(n):
    if n <= 0:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
n = int(input("Enter number of terms to print fibonacci series :"))
print("Fibonacci series is : ")
for i in range(n):
    print(fibo(i), end = " ")