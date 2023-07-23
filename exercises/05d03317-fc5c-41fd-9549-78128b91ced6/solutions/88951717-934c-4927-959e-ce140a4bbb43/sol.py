from re import findall 
txt = "Mili panowie Jan Kowalski i Marian Nowak nie wiedzą, kto to w ogóle jest ta cała Genowefa Piszczek!"
print(findall("[A-Z]\w+\s[A-Z]\w+", txt))
