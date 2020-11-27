print("With As write Start")
with open("withas.txt", "w") as with_as_write:
    with_as_write.write("This as an example of withas write")

print()
print("With As Read Start")
with open("withas.txt", "r") as with_as_read:
    print(str(with_as_read.read()))