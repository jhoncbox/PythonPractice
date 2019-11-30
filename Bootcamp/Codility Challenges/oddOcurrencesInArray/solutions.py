def solution(A):
    resp = []
    for v1 in A:
        if v1 not in resp:
            resp.append(v1)
        elif v1 in resp:
            resp.remove(v1)
    return resp[0]


test_list = [9,3,9,3,9,7,9,3,3,]

print(test_list)
print(solution(test_list))

def solution(A, B):
    A.sort()
    B.sort()
    i = 0
    for a in A:
        if i < len(B)-1 and B[i] < a:
            i += 1
        if a == B[i]:
            return a
    return -1