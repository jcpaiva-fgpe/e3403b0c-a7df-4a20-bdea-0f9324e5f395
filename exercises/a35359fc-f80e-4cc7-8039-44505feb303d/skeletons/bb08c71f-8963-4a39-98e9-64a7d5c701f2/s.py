from re import search
print(search(r"{{gap}}", "15.03.2023, 07.07.2021, 04.03.2019"))

# exp output
# <re.Match object; span=(12, 22), match='07.07.2021'>
