def max_num(*args):
    return(max(args))

def min_num(*args):
    return(min(args))

def abs_func(args):
    return(abs(args))

a = max_num(1,4,5,6,7,2,10,43,12,434,85,-1000)
b = min_num(6,7,3,2,13,5,64,-21,-76)
c = abs_func(b)
print(str(a) + "   " + str(b))
print("Answer is %s and %s and %s" %(a, b, c))

print(type(99))
print(type(99.9))
print(type("99.9"))
print(type(0.1))

