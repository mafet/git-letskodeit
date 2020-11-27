
numbers =[1, 2, 3, 5, 6, 7]


print(numbers[0]+numbers[1])

numbers[0] = 5

print("*"*20)
sum = numbers[0]+numbers[1]

print(sum)


print("*"*20)
print(len(numbers))
### Insert at the end of list ###
numbers.append(4)

print(numbers)


print("*"*20)

### Insert at the top of list ###
numbers.insert(0, 8)

print(numbers)

print("*"*20)

###Find index###

print(numbers.index(3))

##Remove Last item###

new = numbers.pop()
print(str(new) + ' ' + str(numbers))

### Slice list ##
slicing = numbers[2:len(numbers)]
print(slicing)

### Count
print(numbers.count(9))