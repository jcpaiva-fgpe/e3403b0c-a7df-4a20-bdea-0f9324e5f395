from re import sub
slownik = {"Ja": "I", "idę": "am going", "do domu": "home", "teraz": "now"}
txt = 'Ja idę do domu teraz'
f = "|".join(slownik.keys())
print(sub(f, lambda m: slownik[{{gap}}], txt))