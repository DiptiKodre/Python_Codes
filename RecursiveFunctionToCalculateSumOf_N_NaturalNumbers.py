def sum_of_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_numbers(n-1)

n = int(input("Enter a number to find sum of natural numbers: "))
print(sum_of_numbers(n))