from re import search
print(search("{{gap}}", "Jan Kowalski urodzony 12.12.2001 w Dobiegniewie, syn Klary i Melchiora."))

# exp output
# <re.Match object; span=(22, 32), match='12.12.2001'>
