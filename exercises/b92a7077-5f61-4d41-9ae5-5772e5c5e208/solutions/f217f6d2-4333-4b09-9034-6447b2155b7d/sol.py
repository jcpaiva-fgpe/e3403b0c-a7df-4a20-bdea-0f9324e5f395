from re import findall 
txt = """(pierwszy) nie (drugi) też nie (trzeci) i to też nie (czwarty) już!"""
print(findall(r"\(.+?\)", txt))
