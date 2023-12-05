#0.2
#0.1
import os
def getpath(argp):
    repertoireACT = os.path.dirname(os.path.abspath(__file__))
    chemin_fichier = os.path.join(repertoireACT, "Task", argp)
    return chemin_fichier

def verifier_chemin(chemin):
    if os.path.exists(chemin):
        return "yes"
    else:
        return "no"

def ThorX(arg):
    if arg.endswith(" __th__"):
        arg1 = arg.replace(" __th__", "")
        arg2 = getpath("TaskF__th__.txt")
        mjolnir(arg1, arg2)
    else:
        arg1 = arg
        arg2 = getpath("TaskF.txt")
        mjolnir(arg1, arg2)

def mjolnir(arg1, arg2):
    with open(arg2, "a")as file:
        file.write(arg1 + "\n")
