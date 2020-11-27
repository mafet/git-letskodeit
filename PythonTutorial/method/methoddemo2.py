def sum_of(n1 = 1, n2 =2):
    """
    Get sum of two numbers
    """
    return n1 + n2

def is_metro(city):
    """
    Check if city is in list
    Determines if city is a metro
    """
    l = ["lax", "nyc", "sfo"]
    if city in l:
        return True
    else:
        return False



sum1 = sum_of(5, n2=10)
print(sum1)
x = is_metro("bos")
print('*' * 20)
print(x)


