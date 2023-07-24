from re import sub
txt = "mili panowie Jan Kowalski i Marian Nowak nie wiedzą, kto to w ogóle jest ta cała Genowefa Piszczek!"
print(sub(r"\b[A-Z]\w+\b", "***", txt))
