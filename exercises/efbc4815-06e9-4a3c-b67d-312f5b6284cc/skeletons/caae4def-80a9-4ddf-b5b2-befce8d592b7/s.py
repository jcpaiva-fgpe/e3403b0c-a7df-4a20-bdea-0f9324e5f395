from re import finditer
txt = "chętnie rzekłbym coś niecałkiem ckliwego ani czcigodnego"
m = finditer(r"{{gap}}",txt)
for mo in m: print(mo.group(0), mo.span()[0], mo.span()[1]-mo.span()[0])

# exp output
# coś 17 3
# niecałkiem 21 10
# ckliwego 32 8
# czcigodnego 45 11
