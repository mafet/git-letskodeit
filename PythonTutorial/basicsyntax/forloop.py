

books = {"Fiction":"Harry Potter", "Text Book": "Advanced Mathematics", "History": "Roman Empire"}


for c,b in books.items():
    print(c)
    print(b)

string = "characters"

for x in string:
    if x == 'c':
        print("C", end = " ")
    else:
        print(x, end = " ")
    print("")

for b in books:
    print(b + " " + books[b])