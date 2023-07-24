from re import sub
txt = "makrela roleta sfinks pościel tryb woda kola koala buch"
print(sub(r"\b(\w+)a", r"\1", txt))
