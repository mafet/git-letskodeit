"""Exception are errors we should handle this in our code"""

def exception_handling():
    try:
        a = 10
        b = 20
        c = 0
        d = (a + b) / c
        print(d)
   # except ZeroDivisionError:
    #    print("Zero division is Impossible!")
   # except TypeError:
    #    print("Can't add a string to integer")
    except:
        print("NOOOO!")
    else:
        print("Else is executed")
    finally:
        print("Hooray")


exception_handling()