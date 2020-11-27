"""
My solution
"""
def tax_return(gross, state):
    income = gross - (gross * 0.10)
    tax_rate = 0
    if state == "CA":
        tax_rate = 0.15
    elif state == "NY":
        tax_rate = 0.9
    elif state == "WA":
        tax_rate = 0.11
    elif state == "TX":
        tax_rate = 0.05
    else:
        tax_rate = .10
    total_net = income - (gross * tax_rate)
    return total_net

"""
Nicer solution
"""
def tax_return2(gross, state):
    net = gross - (gross * 0.10)
    states = {"CA": 15, "NY": 9, "WA": 11, "TX": 5}
    if state in states:
        net = net - (gross * states[state] / 100)
        return net
    else:
        print("State not in list")
        return None


print(tax_return(5000, "CA"))
print(tax_return2(5000, "CA"))


def what_car(model):
    cars = {"Honda" : 7, "Kia" : 7, "Mazda" : 8, "Maserati" : 10, "Toyota" : 9}
    rating = 0
    if model in cars:
        rating = str(cars[model])
        print("Rating of " + str(rating))
        return rating
    else:
        print("Your car sucks")
        return None


what_car("KIa")
