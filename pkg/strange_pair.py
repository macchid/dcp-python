tupler = lambda x,y: (x, y)

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    return pair(tupler)[0]

def cdr(pair):
    return pair(tupler)[1]

print(car(cons(3,4)))
print(cdr(cons(3,4)))