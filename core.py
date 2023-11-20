from colorama import *

init(autoreset=True)
def main():
    
    print(Fore.GREEN + """
  _____                        ____   _____ 
 |  __ \                      / __ \ / ____|
 | |__) |___  _ __ ___   __ _| |  | | (___  
 |  _  // _ \| '_ ` _ \ / _` | |  | |\___ \ 
 | | \ \ (_) | | | | | | (_| | |__| |____) |
 |_|  \_\___/|_| |_| |_|\__,_|\____/|_____/ 
                                            """)
    while True:
        cmd = input(Fore.WHITE + ">>:")
        if cmd.lower() == "exit":
            break

    print("fermeture des programmes et sauvegarde des fichiers")
    #NON COMPLéTé

main()