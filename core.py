from colorama import *

init(autoreset=True)
def main():
    
    print(Fore.GREEN + r"""
  _____   ____   _____ 
 |  __ \ / __ \ / ____|
 | |__) | |  | | (___  
 |  _  /| |  | |\___ \ 
 | | \ \| |__| |____) |
 |_|  \_\\____/|_____/ 
                                            """)
    while True:
        cmd = input(Fore.WHITE + ">>:")
        if cmd.lower() == "exit":
            break

    print("fermeture des programmes et sauvegarde des fichiers")
    #NON COMPLéTé

main()