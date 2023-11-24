from colorama import *

init(autoreset=True)
def main():
    
    logo()
    while True:
        cmd = input(Fore.WHITE + ">>:")
        if cmd.lower() == "exit":
            break
        elif cmd.lower() == "cls":
            import os 
            os.system("cls")
            logo()
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