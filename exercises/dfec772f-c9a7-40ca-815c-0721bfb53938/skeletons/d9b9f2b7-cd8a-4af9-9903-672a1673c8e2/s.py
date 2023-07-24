from re import sub
txt = "Jan Maria Rokita nie spotkał się nigdy z Johnem Fitzgeraldem Kennedym"
print(sub(r"{{gap}}", r"\1 \2. \3", txt))
