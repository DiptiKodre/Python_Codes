nums = [12,34,55,67,87,99,11,2,1]

n = len(nums)
largest = float("-inf")
second_largest = float("-inf")

for i in range(0,n):
    if nums[i]>largest:
        second_largest = largest
        largest = nums[i]
    elif nums[i]>second_largest and nums[i]!= largest:
        second_largest = nums[i]

print("Second largest element is:", second_largest)