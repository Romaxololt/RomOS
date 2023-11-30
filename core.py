from colorama import *
import Wath_ER as we
from Thor import ThorX

init(autoreset=True)
def main():
    
    logo()
    running = True
    while running:
        # elif cmd.lower() == "":
        cmd = input(Fore.WHITE + ">>:")
        if cmd.lower() == "exit": # quitter le systeme
            running = False
        elif cmd.lower() == "cls": # clear la console
            import os 
            os.system("cls")
            logo()
        elif cmd.startswith("-s "): # run commance
            P1 = cmd.replace("-s ", "")
            import subprocess
            subprocess.run(P1)
        elif cmd.lower() == "clock":
            if cmd.endswith(" -r"):
                new_clock = int(input("entree la nouvelle clock en chiffre >> "))
                we.NCl(new_clock)
        elif cmd.startswith("-"): # launch script
            P1 = cmd.replace("-", "")
            P2 = P1.replace(" ", "")
            ThorX(f"{P2} __th__")
        elif cmd.lower() == "help": # commande d'aide
            print(Fore.BLUE + "liste des commandes disponibles : \n" + Fore.WHITE + "exit : quitter le systeme\ncls : nettoyer la console\n-(nom d'un script) : lance le script ")

    print("fermeture des programmes et sauvegarde des fichiers")
    #NON COMPLéTé
def logo():
    print(Fore.GREEN + r"""

██████╗  ██████╗ ███████╗
██╔══██╗██╔═══██╗██╔════╝
██████╔╝██║   ██║███████╗
██╔══██╗██║   ██║╚════██║
██║  ██║╚██████╔╝███████║
╚═╝  ╚═╝ ╚═════╝ ╚══════╝
                         
""")
main()