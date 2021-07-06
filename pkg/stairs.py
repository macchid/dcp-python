
def staircase2(n, X):

    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x >= 0)

    return cache[-1]


print(staircase(7, {1,3,5,7}))
print(staircase2(7, {1,3,5,7}))