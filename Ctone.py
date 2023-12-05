#0.4
#0.30000000000000004
#0.2
#authcode
#0.1
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