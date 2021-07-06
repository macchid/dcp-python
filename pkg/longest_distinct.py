class UseTracker:
    def __init__(self, k):
        self.k = k
        self.usage = {}

    def add(self, c):
        if self.usage.get(c, 0) == 0:
            self.usage[c] = 1
        else:
            self.usage[c] += 1

    def remove(self, c):
        if self.usage.get(c, 0) < 2:
            self.usage.pop(c)
        else:
            self.usage[c] -= 1

    def is_valid(self):
        return len(self.usage) <= self.k


def largest_substr(chars, k):

    wstart = 0
    maxstart = 0
    maxlength = 1

    chk = UseTracker(k)
    chk.add(chars[0])

    for wend in range(1, len(chars)):
        chk.add(chars[wend])

        while not chk.is_valid():
            chk.remove(chars[wstart])
            wstart += 1

        if wend - wstart + 1 > maxlength:
            maxstart = wstart
            maxlength = wend - wstart + 1

    return ''.join(chars[maxstart:maxstart + maxlength]), maxlength


chars = list("aabacbebebe")
k = 3
seq, length = largest_substr(chars, k)

print(f"The largest sequence of at list {k} distinct charactes is '{seq}' of {length} characters")
        