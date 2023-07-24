from re import sub
txt = "LEcz już za blisko jesteśmy GOleniowa, by wracać do SZczecina, Drogi PAnie!"
print(sub(r"\b[A-Z][A-Z][a-z]+\b", lambda m: m.group(0).title(), txt))
