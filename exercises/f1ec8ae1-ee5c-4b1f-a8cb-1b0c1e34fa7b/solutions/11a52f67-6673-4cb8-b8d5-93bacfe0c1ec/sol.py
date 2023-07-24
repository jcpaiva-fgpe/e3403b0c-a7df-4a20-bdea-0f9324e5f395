from re import sub
txt = """1. Wstęp
2. O obrotach sfer niebieskich
5. Zaginiony w akcji
6. Czary i mary
3. Ratatuj powraca
4. Nigdy więcej sera
7. Spleśniały bochenek
9. Kto zjadł mój plecak?
10. Szczęśliwe zakończenie
11. Epilog"""

def licznik(s):
	licznik.n += 1
	return str(licznik.n) + '. '
licznik.n = 0
print(sub(r"\b\d+\. ", licznik, txt))
