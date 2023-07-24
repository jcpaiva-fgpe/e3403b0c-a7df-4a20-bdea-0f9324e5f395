from re import sub
txt = """1. Rębajło, Heliodor - 18,5 s
2. Dziureczko, Apolinary - 19,2 s
3. Truteń, Szymon - 19,3 s
4. Dziamdziara, Gleb - 20,1 s
5. Skowronek, Zdzisław - 20,5 s"""
print(sub(r"{{gap}}", r"\2 \1", txt))
