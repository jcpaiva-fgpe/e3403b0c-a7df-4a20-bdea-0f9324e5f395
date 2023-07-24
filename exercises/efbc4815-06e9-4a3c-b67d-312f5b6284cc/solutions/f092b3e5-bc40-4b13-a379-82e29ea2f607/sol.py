from re import finditer
txt = "chętnie rzekłbym coś niecałkiem ckliwego ani czcigodnego"
m = finditer(r"\b\w*c(?![hz])\w*\b",txt)
for mo in m: print(mo.group(0), mo.span()[0], mo.span()[1]-mo.span()[0])
