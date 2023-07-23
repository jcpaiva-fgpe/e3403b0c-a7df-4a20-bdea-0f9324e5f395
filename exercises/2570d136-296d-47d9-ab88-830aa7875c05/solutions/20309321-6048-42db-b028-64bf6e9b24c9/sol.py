from re import findall 
txt = """mapy - https://www.google.com/maps, Wimbledon - https://www.youtube.com/Wimbledon, copilot - https://github.com/features/copilot, Verne - https://lubimyczytac.pl/autor/6737/juliusz-verne"""
print([x[0] for x in findall("(https?:\/\/([\w_-]+\.)+[\w_-]+(\/[\w_-]+)*\/?)", txt)])

# exp output
# ['https://www.google.com/maps', 'https://www.youtube.com/Wimbledon', 'https://github.com/features/copilot', 'https://lubimyczytac.pl/autor/6737/juliusz-verne']
