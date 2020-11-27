value = "yellow"

if value == "red":
    print("Stop")
elif value == "yellow":
    print("Prepare to stop")
else:
    print("Go")
a=0
b=0

a = input("Enter value of a:")
b = input("Enter value of b:")
print(type(a))
if int(a) > int(b):
    print("A is greater than B")