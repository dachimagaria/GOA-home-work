


def positive_sum(arr):
    positive_nums = 0
    
    
    for i in arr:
        if i > 0:
            positive_nums += i
            
    return positive_nums

print(positive_sum([1 , 2 , -4  , -6 , 10]))