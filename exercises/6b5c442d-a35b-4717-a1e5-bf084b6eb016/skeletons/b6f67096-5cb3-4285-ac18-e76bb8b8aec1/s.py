from re import sub
txt = "LEcz już za blisko jesteśmy GOleniowa, by wracać do SZczecina, Drogi PAnie!"
print(sub(r"{{gap}}", lambda m: m.group(0).title(), txt))

# exp output
# Lecz już za blisko jesteśmy Goleniowa, by wracać do Szczecina, Drogi Panie!
