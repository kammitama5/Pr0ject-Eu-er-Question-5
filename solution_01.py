nums = range(230000000,260000000)
myList1 = filter(lambda n: (n % 2) | (n % 3) | (n % 4) | (n % 5) | (n % 6) | (n % 7) |
                           (n % 8) | (n % 9) | (n % 10)| (n % 11) | (n % 12) | (n % 13) |
                           (n % 14) | (n % 15) | (n % 16) | (n % 17) | (n % 18) |
                           (n % 19) | (n % 20) == 0, nums)

print(myList1)

#answer is 232792560
