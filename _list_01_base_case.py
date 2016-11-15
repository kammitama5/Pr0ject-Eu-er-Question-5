nums = range(1,100)
myList1 = filter(lambda n: (n % 2) | (n % 3)  == 0, nums)

print(myList1)
