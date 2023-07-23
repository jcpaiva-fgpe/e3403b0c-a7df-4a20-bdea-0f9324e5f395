from re import search
d = search("(\d+)\.(\d+)\.(\d+)", "Jan Kowalski urodzony 12.12.2001 w Dobiegniewie, syn Klary i Melchiora.")
print(f"Dzień: {d.group(1)}, miesiąc: {d.group(2)}, rok: {d.group(3)} (cała data: {d.{{gap}}})")

# exp output
# 'Dzień: 12, miesiąc: 12, rok: 2001 (cała data: 12.12.2001)'
