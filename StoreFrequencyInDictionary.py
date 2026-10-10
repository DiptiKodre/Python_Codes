nums = [11,23,43,12,23,45,67,11,23,23,11,12,23,45,67,89,90,11,23,45,67]
# freq_map = dict()
# for i in range(0,len(nums)):
#     if nums[i] in freq_map:
#         freq_map[nums[i]]+=1
#     else:
#         freq_map[nums[i]]=1
# print(freq_map)
# dry- run of the code:
# nums = [2, 5, 2, 7, 5, 2]

# Initial state:
# freq_map = {}

# Loop runs from i = 0 to i = 5.

# i = 0
# nums[0] = 2
# 2 not in freq_map, so set freq_map[2] = 1
# freq_map becomes: {2: 1}

# i = 1
# nums[1] = 5
# 5 not in freq_map, so set freq_map[5] = 1
# freq_map becomes: {2: 1, 5: 1}

# i = 2
# nums[2] = 2
# 2 is already in freq_map, so increment freq_map[2]
# freq_map becomes: {2: 2}

# i = 3
# nums[3] = 7
# 7 not in freq_map, so set freq_map[7] = 1
# freq_map becomes: {2: 2, 5: 1, 7: 1}

# i = 4
# nums[4] = 5
# 5 is already in freq_map, so increment freq_map[5]
# freq_map becomes: {2: 2, 5: 2, 7: 1}

# i = 5
# nums[5] = 2
# 2 is already in freq_map, so increment freq_map[2]
# freq_map becomes: {2: 3, 5: 2, 7: 1}


hash_map = {}
n = len(nums)
for i in range(0,n):
    hash_map[nums[i]] =hash_map.get(nums[i],0)+1
print(hash_map)

# Time Complexity:
# O(n) on average, where n is the length of nums.
# Reason: loop runs n times, and each dictionary get/update is O(1) average.

# Space Complexity:
# O(k), where k is the number of distinct elements in nums.
# In the worst case (all elements unique), k = n, so space becomes O(n).

# nums = [11,23,43,12,23,45,67,11,23,23,11,12,23,45,67,89,90,11,23,45,67]

# Initial:
# hash_map = {}
# n = 21

# Now loop i from 0 to 20:

# i=0, nums[i]=11
# hash_map[11] = 0+1 = 1
# hash_map = {11: 1}

# i=1, nums[i]=23
# hash_map[23] = 0+1 = 1
# hash_map = {11: 1, 23: 1}

# i=2, nums[i]=43
# hash_map[43] = 0+1 = 1
# hash_map = {11: 1, 23: 1, 43: 1}
# i=3, nums[i]=12
# hash_map[12] = 0+1 = 1
# hash_map = {11: 1, 23: 1, 43: 1, 12: 1}
# i=4, nums[i]=23
# hash_map[23] = 1+1 = 2

# i=5, nums[i]=45
# hash_map[45] = 1

# i=6, nums[i]=67
# hash_map[67] = 1

# i=7, nums[i]=11
# hash_map[11] = 2

# i=8, nums[i]=23
# hash_map[23] = 3

# i=9, nums[i]=23
# hash_map[23] = 4
# i=10, nums[i]=11
# hash_map[11] = 3

# i=11, nums[i]=12
# hash_map[12] = 2

# i=12, nums[i]=23
# hash_map[23] = 5

# i=13, nums[i]=45
# hash_map[45] = 2

# i=14, nums[i]=67
# hash_map[67] = 2

# i=15, nums[i]=89
# hash_map[89] = 1

# i=16, nums[i]=90
# hash_map[90] = 1

# i=17, nums[i]=11
# hash_map[11] = 4

# i=18, nums[i]=23
# hash_map[23] = 6

# i=19, nums[i]=45
# hash_map[45] = 3

# i=20, nums[i]=67
# hash_map[67] = 3