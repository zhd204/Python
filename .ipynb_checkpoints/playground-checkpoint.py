def add(*args):
    total = 0
    for n in args:
        total += n
    return total


t = add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(t)