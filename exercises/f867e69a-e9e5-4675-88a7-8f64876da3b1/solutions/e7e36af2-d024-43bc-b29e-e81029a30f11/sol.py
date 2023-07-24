from re import fullmatch
def sprawdz(txt):
	if fullmatch("[A-Za-z_][A-Za-z0-9_]*", txt): print("OK!")
	else: print("Nazwa niedozwolona!")

sprawdz("_+")
sprawdz("_1")
sprawdz("1a")
sprawdz("a1")
