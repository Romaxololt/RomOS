#1.1
from colorama import *
import Wath_ER as we
from Thor import ThorX
import subprocess
import os

init(autoreset=True)

def connection():
    identifiant = we.get_line(5)
    print(f"identifiant : {identifiant}")
    mdporother = we.getpass("entrée votre mot de passe >>")
    mdpact = we.get_line(6)
    mdporother = mdporother.rstrip('\r')
    mdpact = mdpact.rstrip('\r')
    if mdpact.startswith(f"id:{identifiant}:"):
        mdpact = mdpact.replace(f"id:{identifiant}:", '')
        if mdpact == we.hash(f"{mdporother}"):
            os.system('cls')
            main()
        else:
            print(Fore.RED + "mot de passe incorect")
            connection()
    else:
        we.Error("Erreur de mdp", "005")

def main():
    import os
    os.system("cls")
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
            subprocess.run(P1)
        elif cmd.lower() == "clock":
            if cmd.lower().endswith(" -r"):
                new_clock = int(input("entree la nouvelle clock en chiffre >> "))
                we.NCl(new_clock)
                we.Reboot()
            else:
                clock = we.get_line(4)
                print(f"la clock actuelle est de {clock} seconde")
                print("pour la changer utiliser la commande avec -r a la fin ")
        elif cmd.startswith("-"): # launch script
            P1 = cmd.replace("-", "")
            P2 = P1.replace(" ", "")
            ThorX(f"{P2} __th__")
        elif cmd.lower().startswith("update"):
            if cmd.lower().endswith(" -a"):
                print("mise a jour des systemes basiques ...")
                we.maj_system(False)
                print("fin de la mise a jour")
            if cmd.lower().endswith(" -p"):
                print("mise a jour des systemes basiques ...")
                we.maj_system(True)
                print("fin de la mise a jour")
            if cmd.lower().endswith(" -i"):
                we.maj_info()
        elif cmd.lower().startswith("ros "):
            cmd = cmd.replace("ros ", '')
            print(f"téléchargement de {cmd}")
            we.download_file(cmd)
        elif cmd.lower().startswith("vrs"):
            cmdend = cmd.replace("vrs ", '')
            Vi, Va = we.F1(cmdend)
            print(f"la version la plus récentes de {cmdend} est {Vi} et la version actuelle est {Va}")
        elif cmd.lower() == "reboot":
            we.Reboot()
        elif cmd.lower() == "help": # commande d'aide
            print(Fore.BLUE + "liste des commandes disponibles : \n" + Fore.WHITE + "exit : quitter le systeme\ncls : nettoyer la console\n-(nom d'un script) : lance le script ")
        else:
            print(Fore.RED + f"""Erreur votre commande "{cmd}" est inconnue""")

    print("fermeture des programmes et sauvegarde des fichiers")
    #NON COMPLéTé
def logo():
    logo =r"""

██████╗  ██████╗ ███████╗
██╔══██╗██╔═══██╗██╔════╝
██████╔╝██║   ██║███████╗
██╔══██╗██║   ██║╚════██║
██║  ██║╚██████╔╝███████║
╚═╝  ╚═╝ ╚═════╝ ╚══════╝
                         
"""
    print(Fore.GREEN + logo)
    
connection()