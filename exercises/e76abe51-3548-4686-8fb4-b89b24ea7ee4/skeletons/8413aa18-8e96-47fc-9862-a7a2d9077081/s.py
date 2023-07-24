from re import sub
txt = "Jan Maria Rokita nie spotkał się nigdy z Johnem Fitzgeraldem Kennedym"
def podmien_i_wyswietl(m):
	s = m.group(0)
	print("Podmieniono", len(s), "znaków.")
	return s.upper()
print(sub(r"{{gap}}", podmien_i_wyswietl, txt))

# exp output
# Podmieniono 3 znaków.
# Podmieniono 5 znaków.
# Podmieniono 6 znaków.
# Podmieniono 6 znaków.
# Podmieniono 12 znaków.
# Podmieniono 8 znaków.
# JAN MARIA ROKITA nie spotkał się nigdy z JOHNEM FITZGERALDEM KENNEDYM
