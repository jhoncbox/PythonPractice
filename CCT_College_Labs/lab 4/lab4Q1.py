import statistics

def sum(i1, i2):
    result = 0
    for i in range(i1, i2):
        result += i
    return result

print(sum(1,10)) 

# -------------------------------
# FUNCTION TO GET THE MEDIAN FROM A SET OF NUMBERS
set1 = [1,2,3,4,7,4,8,1,6,6,6,5,8,9]
set2 = [10,43,23,5,7,12,3,23,23,23,123]

def findMedian(list1):    
    print("the median is ", statistics.median(list1))

findMedian(set1)
findMedian(set2)

def findMode(list2):
    print("the mode is ", statistics.mode(list2))

findMode(set1)
findMode(set2)

##MEAN METHOD FROM MUHAMMED
def mean(lyst):
    sum = 0
    for number in lyst:
        sum += number
    if len(lyst) ==0:
        return 0
    else:
        return sum / len(lyst)
## MEDIAN METHOD FROM MUHAMMED
def median(lyst):
    numbers = []
    for number in lyst:
        numbers.append(number)
    numbers.sort()
    if len(numbers) == 0:
        return 0
    else:
        midpoint = len(numbers) // 2
        if len(numbers) % 2 == 1:
            return numbers[midpoint]
        else:
            return (numbers[midpoint] + numbers[midpoint - 1]) /2

## MODE METHOD FROM MUHHAMED
def  mode(lyst):
    theDictionary = {}
    for number in lyst:
        freq = theDictionary.get(number, None)
        if freq == None:
            theDictionary[1] = 1
        else:
            theDictionary[1] = freq + 1
    
    if len(theDictionary) == 0:
        return 0
    else:
        theMaximum = max(theDictionary.values())
        for key in theDictionary:
            if theDictionary[key] == theMaximum:
                return key

def main():
    lyst = [3,1,7,1,4,10]
    print("list ", lyst)
    print("mean ", mean(lyst))
    print("median ", median(lyst))
    print("mode ", mode(lyst))

main()
