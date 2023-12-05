#0.8
from Thor import *
def one():
    inp = input("Entrée votre commmande (NoExtension ou alors entrée brut au début) \n>> ")
    if inp.startswith("brut"):
        inp = inp.replace("brut ", "")
        ThorX(inp)
    else:
        ThorX(f"{inp}.py")
    one()
one()