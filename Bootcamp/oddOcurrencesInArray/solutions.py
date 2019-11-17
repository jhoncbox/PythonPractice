def solution(A):
    resp = []
    for v1 in A:
        if v1 not in resp:
            resp.append(v1)
        elif v1 in resp:
            resp.remove(v1)
    yield resp


test_list = [9,3,9,3,9,7,9]

print(test_list)
print(solution(test_list))