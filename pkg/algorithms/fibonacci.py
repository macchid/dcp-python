
def general_fibonacci(n, X):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x >= 0)

    return cache[-1]

def fibonacci(n):
    return general_fibonacci(n-1, {1,2})

if __name__ == "__main__":
    print(f"fibonacci(10) = {fibonacci(36)}")