from re import findall 
txt="""O! cichy jestem jak wy! o Atrydzi!
Których popioły śpią pod świerszczów strażą —
Ani mię teraz moja małość wstydzi,
Ani się myśli tak jak orły ważą.
Głęboko jestem pokorny i cichy
Tu, w tym grobowcu sławy, zbrodni, pychy!"""
print(findall(r"{{gap}}", txt))

# exp output
# ['Atrydzi', 'świerszczów', 'teraz', 'wstydzi', 'zbrodni']
