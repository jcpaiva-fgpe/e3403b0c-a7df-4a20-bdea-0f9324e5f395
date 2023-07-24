from re import sub
txt = "Jan Maria Rokita nie spotkał się nigdy z Johnem Fitzgeraldem Kennedym"
print(sub(r"\b([A-Z]\w+)\b\s\b([A-Z])\w+\b\s\b([A-Z]\w+)\b", r"\1 \2. \3", txt))
