class Influencer:
    def __init__(self, num_selfies, num_bio_links):
        self.num_selfies = num_selfies
        self.num_bio_links = num_bio_links

    def __repr__(self):
        return f"({self.num_selfies}, {self.num_bio_links})"


# dont touch above this line


def vanity(influencer):
    return (influencer.num_bio_links * 5) + influencer.num_selfies

def vanity_sort(influencers):
    return sorted(influencers, key=vanity)


def bubble_sort(nums):
    swapping = True
    end = len(nums)

    while(swapping):
        swapping = False
        for i in range(1,end):
            if(nums[i-1] > nums[i]):
                nums[i], nums[i-1] = nums[i-1], nums[i]
                swapping = True
        end -= 1

    
    return nums

def merge_sort(nums):
    if(len(nums) < 2):
        return nums

    left = nums[:len(nums)//2]
    right = nums[len(nums)//2:]
    left_sort = merge_sort(left)
    right_sort =merge_sort(right)

    return merge(left_sort, right_sort)

def merge(first, second):
    final = []
    i = j = 0
    while i < len(first) and j < len(second): 
        if first[i] < second[j]:
            final.append(first[i])
            i+=1
        else:
            final.append(second[j])
            j+=1

    final += first[i:]
    final += second[j:]
    return final


def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while(nums[j] < nums[j-1] and j != 0):
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j-=1
    return nums

def quick_sort(nums, low, high):
    if low < high:
        p = partition(nums,low,high)
        quick_sort(nums, low, p-1)
        quick_sort(nums, p+1, high)


def partition(nums, low, high):
    i = low-1
    for j in range(low,high):
        if nums[j] < nums[high]:
            i+=1
            nums[j],nums[i] = nums[i],nums[j]

    nums[i+1], nums[high] = nums[high],nums[i+1]

    return i+1


def selection_sort(nums):
    for i in range(len(nums)):
        smallest = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[i]:
                smallest = j
        
        nums[i], nums[smallest] = nums[smallest], nums[i]


    return nums


def fib(n):
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    grandparent = 0
    parent = 1
    current = 0

    for i in range(n):
        current = grandparent + parent
        grandparent = parent
        parent = current

    return current


def power_set(input_set):
    if(len(input_set) == 0):
        return [[]]

    subsets = [[]]

    for num in input_set:
        sets_with_num = [] 
        for subset in subsets:
            new_set = subset + [num]
            sets_with_num.append(new_set)

            
        subsets += sets_with_num # same as subsets.extend(sets_with_num)

    return subsets

def exponential_growth(n, factor, days):
    growth_list = [n]

    for i in range(days):
        n *= factor
        growth_list.append(n)

    return growth_list
            
