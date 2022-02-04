# #MRO method resolution order
# class A:
#     num = 10

# class B(A):
#     pass

# class C(A):
#     num = 1

# class D(B,C):
#     pass
# print(D.mro())


def multiply(list):
    new_list= []
    for num in list:
        new_list.append(num*2)
    print(new_list)
multiply([1,2,3])


def divide(list):
    new_list = []
    for num in list:
        new_list.append(num//2)
    return new_list

print(divide([8,16,24]))


        