def  cDown(num):
    counter= []
    for x in range(num,-1,-1):
        counter.append(i)
    return counter
print(cDown(5))

def print_and_return(list):
    print(list[0])
    return list[1]
print (print_and_return([1,2]))

def first_plus_length(list):
    return(list[0] + len(list))
print(first_plus_length([1,2,3,4,5]))

def vgts(list):
    if len(list)<2:
        return False
    rlist = []
    for value in list:
        if value>list[1]:
            rlist.append(value)
    print(len(rlist))    
    return rlist
print(vgts([5,2,3,2,1,4]))
print(vgts([3]))

def length_and_value(size,value):
    rlist = []
    for x in range(size):
        rlist.append(value)
    return rlist
# print(length_and_value(4,7))
print(length_and_value(20,21))
