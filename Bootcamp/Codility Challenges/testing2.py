import heapq
# I'm using heapq to have a better approach to the problem
h = heapq
def solution(A, B, C):
    # initialize an empty list and the result string.
    queue = []
    result = ""
    for letter, value in ('a',A), ('b',B), ('c',C):
        # to discard any value inputs of zero
        if value != 0:
            # I used the negative of the value so h.heappop() could return the smallest value,
            # which is actually the highest
            h.heappush(queue, (-value, letter))
    # I set up holders that will hold the value and letter to prevent diversing
    holdValue = 0
    holdLetter = ''
    # while queue contains values the code will run
    while queue:
        # starts by getting the "smallest" value from the queue
        value, letter = h.heappop(queue)
        # if holdValue != 0,  
        if holdValue:
            # place the data into the queue
            h.heappush(queue, (holdValue, holdLetter))
            # resets the values
            holdValue = 0
            holdLetter = ''
        # if the last 2 items in the String are the same as twice the current letter 
        if result[-2:] == letter * 2:
            # hold the current values into the holders
            holdValue = value
            holdLetter = letter
        # else it will add the letter value into the string and adds up 1 to the current value
        else:
            result += letter
            if value != -1:
                h.heappush(queue, (value + 1, letter))
                
    # returns the final string 
    return result

print(solution(0,0,0))