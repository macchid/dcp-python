import random, math

def distance(x, y):
    return math.sqrt(x**2 + y**2)


def montecarlo_pi(n=5000000):
    inCircle = sum(1 for _ in range(n) if distance(random.uniform(0, 1), random.uniform(0, 1)) <= 1.0)
    print(inCircle, n)
    return round(inCircle/n * 4.0, 3)

print(montecarlo_pi())