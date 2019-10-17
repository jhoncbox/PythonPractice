import statistics

def sum(i1, i2):
    result = 0
    for i in range(i1, i2):
        result += i
    return result

print(sum(1,10)) 

# -------------------------------

i1 = [1,2,3,4,7,6,5,8,9]

def findMedian(list):    
    print("the median is ", statistics.median(list))

findMedian(i1)
    