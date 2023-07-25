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
print(sub(r"{{gap}}", licznik, txt))

# exp output
# 1. Wstęp
# 2. O obrotach sfer niebieskich
# 3. Zaginiony w akcji
# 4. Czary i mary
# 5. Ratatuj powraca
# 6. Nigdy więcej sera
# 7. Spleśniały bochenek
# 8. Kto zjadł mój plecak?
# 9. Szczęśliwe zakończenie
# 10. Epilog
