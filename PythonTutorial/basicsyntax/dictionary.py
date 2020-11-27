########################
d ={}

d['one'] = 1
d['two'] = 2

sum = d['one'] + 3
print(sum)
print(d)

d['two'] = 3

print(d)

print(d['two'])
################ NESTED DICTIONARY ####################
print('*' * 50)

cars = {'bmw':{'model':'550i', 'year': 2016},
        'benz':{'model':'E3250', 'year': 2015}
        }

print(cars)
print(cars['bmw']['year'])
print(cars['bmw'])