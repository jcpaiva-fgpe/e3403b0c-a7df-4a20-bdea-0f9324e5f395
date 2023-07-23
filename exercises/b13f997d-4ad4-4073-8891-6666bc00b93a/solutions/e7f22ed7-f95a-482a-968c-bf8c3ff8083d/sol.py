from re import findall 
txt = """Administrator - konto@usz.edu.pl, Prof. Łyczko - grzegorz.lyczko@usz.edu.pl, pomoc - help-desk@coca-cola.pl, sklep - elektryczne_owce@allegro.pl"""
print([x[0] for x in findall("(([\w_-]+\.)*[\w_-]+@([\w_-]+\.)+[\w_-]+)", txt)])
