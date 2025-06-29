def find_max(nums):
    maximum = float("-inf")
    for num in nums:
        if num > maximum:
            maximum = num


    return maximum


def does_name_exist(first_names, last_names, full_name):
    for f_name in first_names:
        for l_name in last_names:
            fl_name = f_name + " " + l_name
            if(fl_name == full_name):
                return True


    return False


def get_avg_brand_followers(all_handles, brand_name):
    total = 0
    for handle_line in all_handles:
        for handles in handle_line:
            if brand_name in handles:
                total += 1

    average_brand_followers = total / len(all_handles)

    return average_brand_followers 

def find_last_name(names_dict, first_name):
    if(first_name in names_dict):
        return names_dict[first_name]

    return None

def binary_search(target, arr):
    low = 0
    high = len(arr)-1
    while(low <= high):
        median = (low + high) // 2
        if(arr[median] == target):
            return True

        elif(arr[median] < target):
            low = median+1

        else:
            high = median-1

    return False


def count_names(list_of_lists, target_name):
    count = 0
    for list in list_of_lists:
        for name in list:
            if name == target_name:
                count+=1

    return count

