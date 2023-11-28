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
        if cmd.lower() == "exit":
            running = False
        elif cmd.lower() == "cls":
            import os 
            os.system("cls")
            logo()
        elif cmd.replace(" ", "").startswith("-"):
            P1 = cmd.replace("-", "")
            P2 = P1.replace(" ", "")
            ThorX(f"{P2} __th__")

        elif cmd.lower() == "help":
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