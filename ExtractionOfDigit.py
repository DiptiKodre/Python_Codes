num = int (input("Enter a number to extract digits from: "))

while num > 0:
    digit = num % 10
    print(digit)
    num = num // 10

