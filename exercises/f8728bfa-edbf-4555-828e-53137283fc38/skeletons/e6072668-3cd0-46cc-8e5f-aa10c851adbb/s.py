from re import sub
txt = "Agent 7:3 zadzwonił pod numer 997:4 i usłyszał 1:3"
print(sub(r"{{gap}}", lambda m: "0"*(int(m.group(2))-len(m.group(1)))+m.group(1), txt))
