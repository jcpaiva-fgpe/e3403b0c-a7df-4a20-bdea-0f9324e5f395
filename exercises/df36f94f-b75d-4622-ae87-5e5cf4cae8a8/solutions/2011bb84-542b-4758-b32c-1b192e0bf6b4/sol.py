from re import findall, I
txt="""Dzisiaj na wielkiem morzu obłąkany,
Sto mil od brzegu i sto mil przed brzegiem,
Widziałem lotne w powietrzu bociany
Długim szeregiem.
Żem je znał kiedyś na polskim ugorze,
Smutno mi, Boże!"""
print(findall(r"(?=\b(\w+)\b.+?\b\1\b)", txt, I)
