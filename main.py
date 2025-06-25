def find_minimum(nums):
    minimum = float("inf")
    if(len(nums)== 0):
        return None

    for i in range(len(nums)):
        if(minimum > nums[i]):
            minimum = nums[i]


    return minimum

def sum(nums):
    sum = 0
    for num in nums:
        sum += num


    return sum

def average_followers(nums):
    followers = 0
    for num in nums:
       followers += num


    return followers/len(nums)
