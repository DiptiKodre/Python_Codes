num = int(input("Enter a number to check palindrome or not: "))
rev = 0
temp = num
while temp >0 :
    rem = temp % 10 #4  #3. #2 #1
    rev = rev *10 +rem #0*10 + 4 = 4  4*10+3=43 43*10+2=432 432*10+1=4321 
    temp = temp // 10    #123  12 1  0s

if  rev == num:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")

# Time Complexity: (O(\log_{10} n)\) as the loop runs once for each digit in the number.
# Space Complexity: O(1) as memory usage stays constant regardless of input size