from re import findall 
txt = """Al. Papieża Jana Pawła II 22A, 70-453 Szczecin
ul. Cukrowa 8, 71-004 Szczecin
ul. Mickiewicza 64, 71-101 Szczecin
ul. Krakowska 71/79, 71-017 Szczecin"""
print(findall("{{gap}}", txt))

# exp output
# ['70-453', '71-004', '71-101', '71-017']
