from functools import reduce

nums =[1,2,3,4,5,6]

total =reduce(lambda a,b: a+b, nums)
print(nums)
print(total)