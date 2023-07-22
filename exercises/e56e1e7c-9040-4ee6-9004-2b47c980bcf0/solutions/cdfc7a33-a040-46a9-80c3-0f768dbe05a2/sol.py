from re import search
print(search("[A-Z].*[A-Z]", "de La Fontaine, Jean").span()[0])
