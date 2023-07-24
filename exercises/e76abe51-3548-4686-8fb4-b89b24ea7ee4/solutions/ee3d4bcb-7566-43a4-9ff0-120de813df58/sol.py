from re import sub
txt = "Jan Maria Rokita nie spotkał się nigdy z Johnem Fitzgeraldem Kennedym"
def podmien_i_wyswietl(m):
	s = m.group(0)
	print("Podmieniono", len(s), "znaków.")
	return s.upper()
print(sub(r"\b([A-Z]\w+)\b", podmien_i_wyswietl, txt))
