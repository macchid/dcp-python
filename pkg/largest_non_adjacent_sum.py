
def largest_non_adjacent(numbers):
    if len(numbers) == 0:
        return 0

    incl = numbers[0]
    excl = 0
    for i in range(1, len(numbers)):
        print(f"incl={incl}, excl={excl}")
        incl, excl = excl + numbers[i], max(excl, incl)

    return max(incl, excl)

print(largest_non_adjacent([5,5,10,40,50,35])) # 80
print(largest_non_adjacent([2,4,6,2,5])) # 13
print(largest_non_adjacent([5,1,1,5])) # 10
print(largest_non_adjacent([2,4,-6,0,5])) # 9