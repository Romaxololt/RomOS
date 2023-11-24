from colorama import *

init(autoreset=True)
def main():
    
    print(Fore.GREEN + r"""

██████╗  ██████╗ ███████╗
██╔══██╗██╔═══██╗██╔════╝
██████╔╝██║   ██║███████╗
██╔══██╗██║   ██║╚════██║
██║  ██║╚██████╔╝███████║
╚═╝  ╚═╝ ╚═════╝ ╚══════╝
                         
""")
    while True:
        cmd = input(Fore.WHITE + ">>:")
        if cmd.lower() == "exit":
            break

    print("fermeture des programmes et sauvegarde des fichiers")
    #NON COMPLéTé

main()