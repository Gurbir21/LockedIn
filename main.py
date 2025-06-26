import math

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
    if(len(nums) == 0):
        return None

    followers = 0
    for num in nums:
       followers += num


    return followers/len(nums)


def get_estimated_spread(audience_followers):
    if(len(audience_followers) == 0):
        return 0

    average_audience_followers = average_followers(audience_followers)

    result = average_audience_followers * (len(audience_followers)  ** 1.2)

    return result

def get_follower_prediction(follower_count, influencer_type, num_months):
    if(influencer_type == 'fitness'):
        follower_count = follower_count * 4 ** num_months

    elif(influencer_type == 'cosmetic'):
        follower_count = follower_count * 3 ** num_months

    else:
        follower_count = follower_count * 2 ** num_months

    return follower_count


def get_influencer_score(num_followers, average_engagement_percentage):
    influencer_score = average_engagement_percentage * math.log(num_followers,2)

    return influencer_score


def num_possible_orders(num_posts):
    possible_orders = 1 
    for i in range(num_posts,1,-1):
       possible_orders *= i


    return possible_orders


def decayed_followers(intl_followers, fraction_lost_daily, days):
    retention_rate = 1-fraction_lost_daily

    decay_folwrs = intl_followers * (retention_rate**days)

    return decay_folwrs

def log_scale(data, base):
    for i in range(len(data)):
        data[i] = math.log(data[i], base)


    return data
