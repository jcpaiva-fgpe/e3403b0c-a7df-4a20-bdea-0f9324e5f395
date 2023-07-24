from re import sub
txt = "Maja ma ma dwa lata lata"
print(sub(r"\b(\w+)\b\s\1", r"\1", txt))
