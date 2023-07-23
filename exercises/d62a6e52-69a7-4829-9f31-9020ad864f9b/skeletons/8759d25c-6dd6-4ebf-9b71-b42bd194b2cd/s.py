from re import findall 
print(findall(r"({{gap}})", "Mika, Lilia, Olek, Bratek, Rafał, Nagietek, Rózia"))

# exp output
# [('Lilia', 'i'), ('Rafał', 'a'), ('Nagietek', 'e')]