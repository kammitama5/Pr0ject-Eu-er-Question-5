# for all values <500 000
# factorize. If factors are
# ==[1..20]
# print number

from math import sqrt
def factor(n):
    factors = set()
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            factors.add(x)
            factors.add(n//x)
            if n % 2 == 0:
                 if n % 3 == 0:
                     if n % 4 == 0:
                         if n % 5 == 0:
                             if n % 6 == 0:
                                 if n % 7 == 0:
                                     if n % 8 == 0:
                                         if n % 9 == 0:
                                            if n % 10 == 0:
                                                if n % 11 == 0:
                                                    if n % 12 == 0:
                                                        if n % 13 == 0:
                                                            if n % 14 == 0:
                                                                if n % 15 == 0:
                                                                     if n % 16 == 0:
                                                                        if n % 17 == 0:
                                                                            if n % 18 == 0:
                                                                                if n % 19 == 0:
                                                                                     if n % 20 == 0:
                                                                                         return sorted(factors)

for i in range(50000000, 60000000):print("%i: factors: %s" % (i, factor(i)))