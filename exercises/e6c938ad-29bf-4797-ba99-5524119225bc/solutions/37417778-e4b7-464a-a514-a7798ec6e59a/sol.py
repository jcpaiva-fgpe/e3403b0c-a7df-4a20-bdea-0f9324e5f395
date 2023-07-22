from re import search
print(search("[0-9][0-9]?", "1. Tel. 110").span()[0])
