#lambda
#using lambda to make our code look simple

#!.finding square root of a list of numbers using lambda
my_list = [5,4,8]
new_list = list(map(lambda num: num**2, my_list))
print(new_list)

#2.orting list with lambda
a = [(0,2),(4,3),(10,-1),(9,9)]
a.sort(key=lambda x: x[1])
print(a)