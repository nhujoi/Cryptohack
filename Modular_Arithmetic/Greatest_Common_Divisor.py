def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
a=66528
b=52920
print(gcd(a, b))