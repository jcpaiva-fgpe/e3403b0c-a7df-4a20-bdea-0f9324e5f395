from re import sub
txt = "Maja ma ma dwa lata lata"
print(sub(r"{{gap}}", r"\1", txt))

# exp output
# Maja ma dwa lata
