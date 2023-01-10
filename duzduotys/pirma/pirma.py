def lyginam(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return a / b
    elif a % 2 != 0 and b % 2 != 0:
        return a * b
    else:
        if a > b:
            return a - b
        else:
            return b - a


print(lyginam(4, 8))
print(lyginam(2, 5))
print(lyginam(5, 7))
print(lyginam(3, 9))
print(lyginam(4, 2))