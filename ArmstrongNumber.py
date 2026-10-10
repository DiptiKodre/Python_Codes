num = int(input("Enter a number to check if it is an Armstrong number: "))

n = num
sum = 0
len = len(str(n))

while n>0:
    rem = n % 10 # 3
    
    
    sum = sum + (rem ** len )# 3**3 = 27
    n = n // 10 # 153 // 10 = 15

if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


# For a single number n, checking if it is an Armstrong number 
# has a time complexity of O(d) or \(O(\log n)\) (where d is the
#  number of digits) and a space complexity of O(1) because it 
# only uses a few fixed variables.