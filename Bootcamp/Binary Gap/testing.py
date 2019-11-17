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
    # return the max count of zeros per each value of the list
    return len(max(x, key=len))


print(solution(1300))
print(bin(1300))

# print((bin(28)[2:])[::-1])


