#map, filter, zip and reduce
#map
from functools import reduce
my_list = [1,2,3]
your_list = [10,20,30]
def multiply(item):
    return item*2

print(list(map(multiply, [1,2,3])))

# filter
def odd_no(item):
    return item % 2 != 0

print(list(filter(odd_no, [1,2,3])))

#zip 
#it iterates over the data structures and zip them together
print(list(zip(my_list,your_list)))

#reduce
def accumulator(acc,item):
    print(acc,item)
    return acc + item
print(reduce(accumulator,my_list,0))


