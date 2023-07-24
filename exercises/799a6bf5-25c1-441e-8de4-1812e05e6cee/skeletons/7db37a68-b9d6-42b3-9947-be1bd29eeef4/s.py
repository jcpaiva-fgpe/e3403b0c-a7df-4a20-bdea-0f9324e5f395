from re import sub
txt = "Inflacja średnioroczna wzrosła wtedy do 40% [Henrykowski 1962], a ceny bochenka chleba przekroczyły 1,5-krotność pensji robotnika wykwalifikowanego [Zięba 1963]."
print(sub(r"{{gap}}", r"(\1, \2)", txt))
