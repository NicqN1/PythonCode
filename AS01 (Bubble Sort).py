
def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

nums = []
for x in range(9):
    numbers = int(input("Enter 9 numbers:"))
    nums.append(numbers)
sort(nums)
print(nums)