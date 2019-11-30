# A binary gap within a positive integer N is any maximal sequence of consecutive zeros
#  that is surrounded by ones at both ends in the binary representation of N.

# For example, number 9 has binary representation 1001 and contains a binary gap of length 2.
#  The number 529 has binary representation 1000010001 and contains two binary gaps:
#  one of length 4 and one of length 3. The number 20 has binary representation 10100 and
#  contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps.
#  The number 32 has binary representation 100000 and has no binary gaps.

# Write a function:
# def solution(N)

# that, given a positive integer N, returns the length of its longest binary gap.
#  The function should return 0 if N doesn't contain a binary gap.

# For example, given N = 1041 the function should return 5,
#  because N has binary representation 10000010001 and so its longest binary gap is of length 5.
#  Given N = 32 the function should return 0, because N has binary representation '100000' and thus
#  no binary gaps.

# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [1..2,147,483,647].

def solution(n):
    # here we convert the number given to binary,
    # we set [2:] because python gives binary like this
    # 1300 = 0b10100010100, so we take out the initial "0b"
    binary = bin(n)[2:]
    # then we reverse the "binary" string to place the ceros to the begining
    # this is to prevent having ceros that aren't in between '1'
    rbinary = binary[::-1]
    # this while loop will run until the if statement is breaks
    while True:
        # the "if" checks for zeros in the beginning of the string,
        # if the is, replace it with empty space(basically deleting them) only once at the time
        # else, break the program.
        if rbinary[0] == '0':
            rbinary = rbinary.replace('0','',1)
        else:
            break
    # then we can split the rbinary string into a list
    # separated by '1', to get only groups of zeros
    x = rbinary.split('1')
    # return the max count of zeros per each value comparing of the list
    return len(max(x, key=len))

print(solution(1300))
print(solution(28))
print(solution(123432))
print(solution(10))
