from re import fullmatch
def sprawdz(txt):
	if fullmatch("{{gap}}", txt): print("OK!")
	else: print("Nazwa niedozwolona!")

sprawdz("_+")
sprawdz("_1")
sprawdz("1a")
sprawdz("a1")

# exp output
# Nazwa niedozwolona!
# OK!
# Nazwa niedozwolona!
# OK!
