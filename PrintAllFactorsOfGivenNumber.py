
from math import sqrt

#brute force approach
# Time Complexity: O(n)
# Space Complexity: O(k) where k is the number of factors of n 
# (stored in result).
# In worst case (for this problem context),
# this is often written as O(n) upper bound, but more precisely it is O(k).
result = []
n = int(input("Enter a number to print all its factors: "))
# for num in range(1,n+1):
#     if(n%num == 0):
#         result.append(num)
# print(result)


# Better approach
# Time Complexity: O(n)
# The loop runs about n/2 times, and each iteration does constant work. So (O(n/2)) simplifies to (O(n)).

# Space Complexity: O(k)
# result stores all factors, where k is the number of factors of n.
# Worst-case upper bound can be written as O(n), but precise is O(k).
# for num in range(1,(n//2)+1):
#     if(n%num == 0):
#         result.append(num)
# result.append(n) # n is always a factor of itself
# print(result)


#Optimal solution
# Time Complexity:

# Factor scan loop: O(sqrt(n))
# Sorting factors: O(k log k), where k = number of factors collected
# Total: O(sqrt(n) + k log k)
# Space Complexity:

# result stores k factors, so O(k)
# sorted(result) creates a new sorted list, also O(k)
# Overall auxiliary space: O(k)

for num in range(1,int(sqrt(n))+1):
    if(n%num == 0):
        result.append(num)
        if(num != n//num):
            result.append(n//num)
print(sorted(result))

# Code logic:

# Loop num from 1 to int(sqrt(36)) = 6
# If num divides n, add num
# Add paired factor n//num if it is different
# Print sorted result
# Step-by-step:

# Start: result = []

# num = 1
# 36 % 1 == 0, so add 1
# paired factor = 36//1 = 36, different from 1, so add 36
# result = [1, 36]
# num = 2
# 36 % 2 == 0, so add 2
# paired factor = 18, add 18
# result = [1, 36, 2, 18]

# num = 3
# 36 % 3 == 0, so add 3
# paired factor = 12, add 12
# result = [1, 36, 2, 18, 3, 12]

# num = 4
# 36 % 4 == 0, so add 4
# paired factor = 9, add 9
# result = [1, 36, 2, 18, 3, 12, 4, 9]

# num = 5
# 36 % 5 != 0, skip
# result unchanged
# num = 6
# 36 % 6 == 0, so add 6
# paired factor = 36//6 = 6, same value, so do not add again
# result = [1, 36, 2, 18, 3, 12, 4, 9, 6]

# Now print sorted(result):
# [1, 2, 3, 4, 6, 9, 12, 18, 36]

