from re import sub
txt = "makrela roleta sfinks pościel tryb woda kola koala buch"
print(sub(r"{{gap}}", r"\1", txt))
