from re import search
d = search("(\d+)\.(\d+)\.(\d+)", "Jan Kowalski urodzony 12.12.2001 w Dobiegniewie, syn Klary i Melchiora.")
print(f"Dzień: {d.group(1)}, miesiąc: {d.group(2)}, rok: {d.group(3)} (cała data: {d.group(0)})")
