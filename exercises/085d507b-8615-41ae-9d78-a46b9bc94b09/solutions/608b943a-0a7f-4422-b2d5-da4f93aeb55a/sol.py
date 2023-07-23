from re import findall 
txt = "Jan Kowalski ur. 12.12.2001 w Zawichoście, Marian Nowak ur. 3.6.1997 w Budowie, Genowefa Piszczek ur. 2.2.1922 w Michałkowicach."
print(findall("\d+\.\d+\.\d+", txt))
