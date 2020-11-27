a = 10

def test_method():
    global a
    print("Value of a inside the method is " + str(a))
    a = 2
    print("New value of a inside the method is " + str(a))


print("Value of global variable is " + str(a))
test_method()
print("New value of global variable is " + str(a))