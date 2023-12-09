#1.0
version = "alpha 0.4"
import os
listescr = "core.py","Ctone.py","GT8.py","Logo.ico","ROS.py","Thor.py","Wath_ER.py","Rogit.py","CryptROS.py"
def token():
    ########################################################################################################### TOKEN ##################################################################################################
    chaine = "ghp_,m579q,iMG1GD,POdUdp,9iM7G,QxYzk,U5v4,LFD,xz"
    chaine_sans_virgules = chaine.replace(',', '')
    return chaine_sans_virgules
def copy_file(ros):
    import requests
    import base64
    # Paramètres GitHub
    github_token = token()
    repository_owner = 'Romaxololt'
    repository_name = 'RomOS'

    # URL de l'API GitHub pour le contenu du référentiel
    api_url = f'https://api.github.com/repos/{repository_owner}/{repository_name}/contents/{ros}'

    # En-têtes de la requête avec le token d'authentification
    headers = {
        'Authorization': f'token {github_token}'
    }

    # Effectuer la requête GET pour obtenir le contenu du fichier
    response = requests.get(api_url, headers=headers)

    # Vérifier si la requête a réussi (statut 200 OK)
    if response.status_code == 200:
        # Charger le contenu du fichier dans la variable
        var = response.json()['content']
        var1 = base64.b64decode(var).decode('utf-8')
        return var1
    else:
        # Afficher un message d'erreur si la requête a échoué
        print(f"Erreur {response.status_code}: {response.text}")
        return None
    
def check_key_file():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    key_file_path = os.path.join(script_directory, 'key')

    if os.path.exists(key_file_path):

        with open(key_file_path, 'r') as key_file:
            content = key_file.read()
            donnees = copy_file("key")

            # Remplacez 'VotreChaineDeCaracteres' par la chaîne que vous recherchez
            lignes = donnees.splitlines()

            # Parcourir chaque ligne et effectuer l'opération souhaitée
            keyvalidation = False
            for ligne in lignes:
                if ligne == content:
                    keyvalidation = True
            if not keyvalidation:                    
                print("La clée est incorrecte. Le script s'arrête.")
                import time
                time.sleep(5)
                exit()
    else:
        print("Le fichier 'key' n'est pas présent. Le script s'arrête.")
        import time
        time.sleep(5)
        exit()

check_key_file()
print(f"Bonjour et bienvenue dans le setup d'installation de ROS V {version}.")
print(f"Le lancement de l'installation téléchargera les scripts par défaut suivants : {listescr}")
cmd = input("Appuyez sur une touche pour lancer l'installation. Vous acceptez également les conditions d'utilisation.")
installo = input("entrée le chemin avec un format convenable \n>>")
bat = r"""@echo off
setlocal enabledelayedexpansion

REM Liste des bibliothèques à vérifier et installer si nécessaire
set "libraries=requests shutil json base64 datetime colorama"

REM Vérifier si Python est installé
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python n'est pas installé.
    goto :end
)

REM Afficher la version de Python
echo Version de Python installee:
python --version
echo.

REM Vérifier et installer les bibliothèques
echo Verification des bibliotheques:

for %%i in (%libraries%) do (
    python -c "import %%i" >nul 2>&1
    if %errorlevel% equ 0 (
        echo Bibliotheque %%i : Installee
    ) else (
        echo Bibliotheque %%i : Non installee. Installation en cours...
        python -m pip install %%i
        if %errorlevel% equ 0 (
            echo Installation de %%i reussie.
        ) else (
            echo Echec de l'installation de %%i.
        )
    )
)

:end
pause
"""

def internet():
    import requests
    try:
        # Tentez de faire une requête vers un site Web connu (par exemple, google.com)
        response = requests.get("http://www.google.com", timeout=5)
        # Si la requête réussit (statut code 200), retournez True (connecté)
        return response.status_code == 200
    except requests.ConnectionError:
        # Si une erreur de connexion se produit, retournez False (non connecté)
        return False
def dlNOinternet(installW):
    if os.path.exists(installW):
        print("")
    else:
        print(f"Le chemin '{installW}' n'existe pas.")
        error("NoValidPathFound #001")
    def add_content_to_file(filename, content):
        with open(filename, 'a') as file:
            file.write(content)
    file_contents = {
        'core.py': r'''#1.0
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
    
connection()''',
        'Ctone.py': r'''#1.2
from Thor import *
def one():
    inp = input("Entrée votre commmande (NoExtension ou alors entrée brut au début) \n>> ")
    if inp.startswith("brut"):
        inp = inp.replace("brut ", "")
        ThorX(inp)
    else:
        ThorX(f"{inp}.py")
    one()
one()''',
        'GT8.py': r'''#1.2
import os
import time
import threading
import Wath_ER as we
clock = int(we.get_line(4))
def execute_task(task):
    try:
        os.system(f"python {task}")
    except FileNotFoundError:
        print(f"Erreur : Fichier {task} non trouvé. La tâche est ignorée.")

def Taskmanager():
    
    while True:
        # Lire le fichier TaskF.txt
        with open(chemin_taskF, "r") as file:
            tasks = file.readlines()

        # Supprimer les tâches du fichier
        with open(chemin_taskF, "w") as file:
            file.writelines(tasks[1:])

        # Vérifier s'il y a des tâches à exécuter
        if tasks:
            # Récupérer la première tâche
            task_to_execute = tasks[0].strip()

            # Exécuter la tâche
            execute_task(task_to_execute)
        else:
            # Attente d'une seconde s'il n'y a pas de tâches
            time.sleep(clock)
def Thor():
    while True:
        # Lire le fichier TaskF.txt
        with open(chemin_taskFth, "r") as file:
            tasks = file.readlines()

        # Supprimer les tâches du fichier
        with open(chemin_taskFth, "w") as file:
            file.writelines(tasks[1:])

        # Vérifier s'il y a des tâches à exécuter
        if tasks:
            # Récupérer la première tâche
            task_to_execute = tasks[0].strip()

            # Exécuter la tâche dans un thread séparé
            thor = threading.Thread(target=execute_task, args=(task_to_execute,))
            thor.start()
        else:
            # Attente d'une seconde s'il n'y a pas de tâches
            time.sleep(clock)

if __name__ == "__main__":
    repertoireACT = os.path.dirname(os.path.abspath(__file__))
    chemin_taskF = os.path.join(repertoireACT, "Task", "TaskF.txt")
    chemin_taskFth = os.path.join(repertoireACT, "Task", "TaskF__th__.txt")
    launchthor = threading.Thread(target=Thor)
    launchtaskM = threading.Thread(target=Taskmanager)
    launchtaskM.start()
    launchthor.start()
    
''',
        'ROS.py': r'''#1.1
from Thor import ThorX
import subprocess
import os
import time
print("UEFI#1 _ POST:")
time.sleep(0.5)
# Obtenez le chemin absolu du répertoire du script
script_dir = os.path.dirname(os.path.abspath(__file__))
from Wath_ER import get_line, configenter
# Définissez le répertoire de travail sur le répertoire du script
os.chdir(script_dir)
nom_fichier = "Save.txt"

if not os.path.exists(nom_fichier):
    # Le fichier n'existe pas, le créer
    with open(nom_fichier, 'w') as file:
        print(f"Le fichier {nom_fichier} a été créé.")
def is_file_empty(file_path):
    return os.path.getsize(file_path) == 0

# Exemple d'utilisation
nom_fichier = "Save.txt"

if is_file_empty(nom_fichier):
    print(f"Le fichier {nom_fichier} est vide.\nconfiguration ...")
    from Wath_ER import execution_file,configbasic, Reboot, NCl
    configbasic()
    execution_file()
    configenter()
    NCl("1")
    Reboot()

if get_line(5)=='' or get_line(6)=='':
    configenter()
    
print("exiting UEFI POST completed")
time.sleep(1)
os.system("cls")
ThorX("core.py")
subprocess.run("python GT8.py")''',
        'Thor.py': r'''#0.7
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
''',
        "Wath_ER.py": r'''#1.1
# Wath_ER Socket ROS V0.1.2
def SHORTCREATEROS():
    import os
    import shutil

    def create_shortcut(source_script, shortcut_name, icon_file):
        # Chemin du répertoire actuel
        current_directory = os.path.dirname(os.path.abspath(__file__))

        # Chemin complet du script source
        source_script_path = os.path.join(current_directory, source_script)

        # Chemin complet du fichier ICO
        icon_path = os.path.join(current_directory, icon_file)

        # Vérifier si le fichier ICO est déjà dans le répertoire de destination
        if not os.path.exists(os.path.join(current_directory, icon_file)):
            # Copier l'icône dans le répertoire du script source
            shutil.copy(icon_path, current_directory)

        # Créer le raccourci avec le même nom que le script
        shortcut_path = os.path.join(current_directory, shortcut_name + ".lnk")

        # Créer le raccourci en utilisant le module os
        os.system(f'powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut(\'{shortcut_path}\'); $Shortcut.TargetPath = \'{source_script_path}\'; $Shortcut.IconLocation = \'{os.path.join(current_directory, icon_file)}\'; $Shortcut.Save()"')

        # Déplacer le raccourci dans le répertoire parent
        parent_directory = os.path.dirname(current_directory)
        new_shortcut_path = os.path.join(parent_directory, shortcut_name + ".lnk")
        shutil.move(shortcut_path, new_shortcut_path)

    def CREATEROSSHORT():
        # Nom du script source
        source_script = "ROS.py"

        # Nom du raccourci à créer
        shortcut_name = "ROS"

        # Nom du fichier ICO
        icon_file = "logo.ico"

        # Créer le raccourci avec l'icône spécifiée
        create_shortcut(source_script, shortcut_name, icon_file)
    CREATEROSSHORT()

def get_line(line_number, file="Save.txt"):
    """obtiens la ligne de Save.txt """
    import os
    repertoireACT = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(repertoireACT, file)
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if 1 <= line_number <= len(lines):
                return lines[line_number - 1].strip()  # -1 pour correspondre à l'index 0
            else:
                return f"Erreur : La ligne {line_number} n'est pas valide dans le fichier."
    except UnicodeDecodeError:
        with open(file_path, encoding="utf-8", errors="ignore") as file:
            lines = file.readlines()
            if 1 <= line_number <= len(lines):
                return lines[line_number - 1].strip()  # -1 pour correspondre à l'index 0
            else:
                return f"Erreur : La ligne {line_number} n'est pas valide dans le fichier."
    except FileNotFoundError:
        return f"Erreur : Le fichier '{file_path}' n'a pas été trouvé."
    
def export_list_to_file(line, my_list, file_pathl=False):
    import os
    if file_pathl == False:
        repertoireACT = os.path.dirname(os.path.abspath(__file__))
        file_pathl = os.path.join(repertoireACT, "Save.txt")
    with open(file_pathl, 'r+') as file:
        lines = file.readlines()
        lines[line - 1] = ','.join(map(str, my_list)) + '\n'
        file.seek(0)
        file.writelines(lines)

def import_list_from_file(line, file_pathl=False):
    import os
    if file_pathl == False:
        repertoireACT = os.path.dirname(os.path.abspath(__file__))
        file_pathl = os.path.join(repertoireACT, "Save.txt")
    with open(file_pathl, 'r') as file:
        lines = file.readlines()
        try:
            line_content = lines[line - 1]
            my_list = line_content.strip().split(',')
        except (IndexError):
            print("Erreur lors de l'importation de la liste.")
            my_list = []
    return my_list

def launch(script):
    """
    Lance le script spécifié.

    Parameters:
        script (str): Nom du script à lancer.
    Returns:
        subprocess.CompletedProcess: Informations sur le processus lancé.
    """
    import subprocess
    import os
    
    current_directory = os.getcwd()
    
    # Si le répertoire actuel se termine par "system", ne pas ajouter "system" au chemin
    if current_directory.endswith("system"):
        script_path = os.path.join(current_directory, script)
    else:
        script_path = os.path.join(current_directory, "system", script)

    try:
        # Lance le script dans la console actuelle
        process = subprocess.run(['python', script_path], check=True)
        return process
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors du lancement du script {script}: {e}")
        return None


def launchX(script):
    """
        Lance le script spécifié dans une nouvelle console.

        Parameters:
            script_name (str): Nom du script à lancer.
        Returns:
            subprocess.CompletedProcess: Informations sur le processus lancé.
    """
    import os
    import sys
    import subprocess
    current_directory = os.getcwd()
    if current_directory.endswith("system"):
        
        script = os.path.join(os.getcwd(),script)
    else:
        script = os.path.join(os.getcwd(),"system" ,script)
    try:
        # Vérifie si le système d'exploitation est Windows
        if sys.platform.startswith('win'):
            subprocess.Popen(['start', 'cmd', '/k', 'python', script], shell=True)
        else:
            print("La fonction 'new_console' est uniquement prise en charge sur Windows.")
            return None
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors du lancement du script {script}: {e}")
        return None  
    
def hi():
    return "hi"

# ROGIT Extension #
def R_DL(script):
    from Rogit import download_file
    return download_file(script)

def R_UP(script ):
    from Rogit import update_file
    return update_file(script)

def R_CR(script ):
    from Rogit import create_file
    return create_file(script)

def token():
    token = unicryptdec(get_line(2))
    return token

def download_file(file_name):
    import requests
    import json
    import base64
    import os
    github_token = token()
    repository_owner = 'Romaxololt'
    repository_name = 'RomOS'
    installW = os.path.dirname(os.path.realpath(__file__))
    local_directory = installW
    # Construire l'URL du fichier sur GitHub
    github_api_url = f'https://api.github.com/repos/{repository_owner}/{repository_name}/contents/{file_name}'
    headers = {'Authorization': f'token {github_token}'}
    response = requests.get(github_api_url, headers=headers)

    if response.status_code == 200:
        data = json.loads(response.text)
        content = data['content']
        decoded_content = base64.b64decode(content)

        # Enregistrer le fichier localement
        with open(os.path.join(local_directory, file_name), 'wb') as file:
            file.write(decoded_content)
        return True
    else:
        return False

def update_file(file_name):
    import requests
    import json
    import base64
    import os
    github_token = token()
    repository_owner = 'Romaxololt'
    repository_name = 'RomOS'
    installW = os.path.dirname(os.path.realpath(__file__))
    local_directory = installW
    # Vérifier si le fichier existe localement
    local_path = os.path.join(local_directory, file_name)
    if os.path.exists(local_path):
        # Vérifier si le fichier existe sur GitHub
        github_api_url = f'https://api.github.com/repos/{repository_owner}/{repository_name}/contents/{file_name}'
        headers = {'Authorization': f'token {github_token}'}
        response = requests.get(github_api_url, headers=headers)

        if response.status_code == 200:
            # Supprimer le fichier sur GitHub
            data = json.loads(response.text)
            github_sha = data['sha']
            delete_url = f'https://api.github.com/repos/{repository_owner}/{repository_name}/contents/{file_name}'
            delete_data = {
                'message': 'Suppression du fichier depuis l\'API',
                'sha': github_sha
            }
            response = requests.delete(delete_url, headers=headers, json=delete_data)
            if response.status_code == 200:
                # Mettre à jour le fichier sur GitHub avec la version locale
                with open(local_path, 'rb') as file:
                    content = file.read()
                    update_url = f'https://api.github.com/repos/{repository_owner}/{repository_name}/contents/{file_name}'
                    update_data = {
                        'message': 'Mise à jour du fichier depuis l\'API',
                        'content': base64.b64encode(content).decode('utf-8'),
                        'sha': github_sha
                    }
                    response = requests.put(update_url, headers=headers, json=update_data)

                    if response.status_code == 200:
                        return True
                    else:
                        return False
            else:
                print(f'Erreur lors de la suppression de {file_name} sur GitHub.')
                return False
        else:
            print(f'Le fichier {file_name} n\'existe pas sur GitHub.')
            return False

    else:
        print(f'Le fichier {file_name} n\'existe pas localement.')

def copy_file(ros):
    import requests
    import base64
    # Paramètres GitHub
    github_token = token()
    repository_owner = 'Romaxololt'
    repository_name = 'RomOS'

    # URL de l'API GitHub pour le contenu du référentiel
    api_url = f'https://api.github.com/repos/{repository_owner}/{repository_name}/contents/{ros}'

    # En-têtes de la requête avec le token d'authentification
    headers = {
        'Authorization': f'token {github_token}'
    }

    # Effectuer la requête GET pour obtenir le contenu du fichier
    response = requests.get(api_url, headers=headers)

    # Vérifier si la requête a réussi (statut 200 OK)
    if response.status_code == 200:
        # Charger le contenu du fichier dans la variable
        var = response.json()['content']
        var1 = base64.b64decode(var).decode('latin-1')
        return var1
    else:
        # Afficher un message d'erreur si la requête a échoué
        print(f"Erreur {response.status_code}: {response.text}")
        return None
    
def get_line_Git(ros, line):
    ros1 = copy_file(ros)
    lines = ros1.split('\n')
    ligne = lines[line - 1]
    return ligne

def unicryptdec(chaine):
    """enleve les virgule """
    chaine_sans_virgules = chaine.replace(',', '')
    return chaine_sans_virgules

def unicryptkey(chaine):
    """enleve les virgule et les remplace par +"""
    chaine_sans_virgules = chaine.replace(',', '+')
    return chaine_sans_virgules

def writeL(chaine, numero_ligne, File="Save.txt"):
    """Modifie une valeur dans une ligne de Save.txt"""
    try:
        # Ouvrir le fichier en mode lecture et écriture
        with open(File, "r+", encoding="utf-8") as file:
            lines = file.readlines()

            # Vérifier si la ligne spécifiée existe
            if 1 <= numero_ligne <= len(lines):
                # Modifier la chaîne dans la ligne spécifiée
                lines[numero_ligne - 1] = chaine + '\n'

                # Réécrire le fichier avec la nouvelle version
                file.seek(0)  # Retour au début du fichier
                file.writelines(lines)
                file.truncate()  # Tronquer le fichier au besoin
                return True
            else:
                print("Le numéro de ligne spécifié est hors de portée.")
                return "003"
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return f"004{e}"



def Error(typeE="", code=""):
    """transmet ici le nom de l'erreur et son code"""
    if len(code) == 3:
        print("Erreur Fatal détéctée (!)")
        print(f"erreur de type {typeE}\ncode de l'erreur #{code}")
        print(f"si vous ne comprenez pas l'erreur n'hésitez pas a lancer la derniere version de Astorm et d'entrée votre code ({code})")
        input("appuyer sur une touche pour fermer le programmes\n>>")
    else:
        print("Erreur fatal sans nom de code")
        input("appuyer sur une touche pour fermer le programmes\n>>")
    raise SystemExit

def Crypt_with_one(text):
    """encrypte une valeur avec le systeme de codage one"""
    from CryptROS import encrypt_one
    return encrypt_one(text)

def Crypt_with_SF(text):
    """encrypte une valeur avec le systeme de codage FS"""
    from CryptROS import encrypt_SF
    return encrypt_SF(text)

def Crypt_with_Xor(text, key):
    """encrypte une valeur avec le systeme de cryptage Xor et une clée symétrique"""
    from CryptROS import xor_crypt
    xor_crypt(text, key)

def Decoder_CryptROS(text, key=None):
    """decrypte une valeur (ne pas oublier le systeme de cryptage en position 1)"""
    from CryptROS import decode
    return decode(text, key)

def Decoder_enter_CryptROS():
    """decrypte une valeur (imcompatible avec : xor ) (ne pas oublier le systeme de cryptage en position 1)"""
    from CryptROS import decode, get_input
    return decode(get_input())

def hash(arg):
    """encrypte un valeur non décodable en hash"""
    from CryptROS import sha256
    return sha256(arg)

def remove_start_space(text):
    if text.startswith(' '):
        new = text[1:]
        remove_start_space(new)
    return text

def encrypt_underscore(texte):
    ligne_unique = texte.replace('\n', '_#__#')
    return remove_start_space(ligne_unique)

def decrypt_underscore(texte):
    ligne_unique = texte.replace('_#__#', '\n')
    return remove_start_space(ligne_unique)

def Reboot():
    import os
    import sys
    python = sys.executable
    os.execl(python, python, *sys.argv)

def configlines():
        with open("Save.txt", 'r') as fichier:
            lignes = fichier.readline()
        with open("Save.txt", 'a') as fichier:
        # Ajouter 1000 lignes vides
            if not len(lignes) >= 65536:
                for _ in range(1000):
                    fichier.write('\n')
            else:
                print("Nombre max de ligne atteint dans Save.txt")

def NCl(cmd):
    writeL(cmd, 4)

def execution_file():
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    writeL(script_dir, 3)  

def configbasic():
    writeL("core.py,Ctone.py,GT8.py,ROS.py,Thor.py,Wath_ER.py,CryptROS.py", 1)
    writeL("ghp_,m579q,iMG1GD,POdUdp,9iM7G,QxYzk,U5v4,LFD,xz", 2)

def configenter():
    identifiant = input("entrée votre identifiant :")
    mdp = getpass()
    writeL(identifiant, 5)
    mdp = hash(f"{mdp}")
    writeL(f"id:{identifiant}:{mdp}", 6)

def getpass(prompt="Entrez votre mot de passe :"):
    import msvcrt
    print(prompt, end="", flush=True)
    password = ""
    while True:
        char = msvcrt.getch().decode('utf-8')
        if char == '\r' or char == '\n':
            break
        elif char == '\x08':  # Backspace
            password = password[:-1]
            print('\b \b', end='', flush=True)
        else:
            password += char
            print('*', end='', flush=True)
    print()  # Nouvelle ligne après la saisie du mot de passe
    return password

def maj_system(arg):
    printable = arg
    allfile = import_list_from_file(1)
    allfile = [element for element in allfile if element != "Logo.ico"]
    barre = BarreDeProgression(len(allfile))
    for i in allfile:
        Vi = get_line_Git(i, 1)
        Va = get_line(1, i)
        Vi = Vi.rstrip('\r')
        if printable:print(repr(i));print(repr(Vi));print(repr(Va))
        if Vi != Va:
            import os
            if printable:print(f"{i} n'est pas à jour , mise a jour ...")
            os.remove(i)
            download_file(i)
        else: 
            if printable:print(f"{i}est à jour")
        barre.add(1)
        barre.afficher()

def F1(arg):
    if get_line(1, arg) == get_line_Git(arg, 1):
        return False
    else:
        Vi = get_line_Git(arg, 1).replace('#', '')
        Va = get_line(1, arg).replace('#', '')
        Vi = Vi.rstrip('\r')
        Va = Va.rstrip('\r')
        try:
            vi_float = float(Vi)
            va_float = float(Va)
            return [vi_float, va_float]
        except ValueError:
            # Gérer le cas où la conversion en float échoue
            print(f"Les chaînes ne représentent pas des nombres valides. (erreur pour {arg})")
            return False
        
def UPDrogit(arg):
    Vi, Va = F1(arg)
    return Vi > Va
    
def authentification_rogit(arg):
    if not UPDrogit(arg):
        pass
    else:
        Error("il faut un nombre supérieur", "004")

def maj_info():
    allfile = import_list_from_file(1)
    allfile = [element for element in allfile if element != "Logo.ico"]
    base = 0
    barre = BarreDeProgression(len(allfile))
    for i in allfile:
        upd = UPDrogit(i)
        if upd == True:
            base += 1
            print(f"une mise a jour est disponible pour {i}")
        barre.add(1)
        barre.afficher()
    if base == 0:
        print("tout les systèmes sont a jour")
    else:
        print(f"il y a {base} système{'s' if base > 1 else ''} a mettre a jour\npour les mettres a jour tapez update -a")

class BarreDeProgression:
    def __init__(self, taille, arg=None):
        self.taille = taille
        self.progression = 0
        self.arg = arg

    def add(self, valeur):
        self.progression += valeur

        # Assurez-vous que la progression ne dépasse pas la taille de la barre
        self.progression = min(self.progression, self.taille)

    def afficher(self):
        # Afficher la barre de progression sur une seule ligne
        barre = "#" * self.progression
        espaces = " " * (self.taille - self.progression)
        print(f"\r{'[' if self.arg == 'limit' else ''}{barre}{espaces}{']' if self.arg == 'limit' else ''}", end="", flush=True)

        # Ajouter un saut de ligne lorsque la barre est complète
        if self.progression == self.taille:
            print()


''',
        "Rogit.py": r'''#0.1
def token():
    import Wath_ER
    github_token = (Wath_ER.unicryptdec(Wath_ER.get_line(2)))
    return github_token

def download_file(file_name):
    import os
    import requests
    import json
    import base64
    import Wath_ER as we
    # Remplacez ces valeurs par les vôtres
    github_token = token()
    repository_owner = 'Romaxololt'
    repository_name = 'RomOS'
    local_directory = os.path.dirname(os.path.realpath(__file__))
    # Construire l'URL du fichier sur GitHub
    github_api_url = f'https://api.github.com/repos/{repository_owner}/{repository_name}/contents/{file_name}'
    headers = {'Authorization': f'token {github_token}'}
    response = requests.get(github_api_url, headers=headers)

    if response.status_code == 200:
        data = json.loads(response.text)
        content = data['content']
        decoded_content = base64.b64decode(content)

        # Enregistrer le fichier localement
        with open(os.path.join(local_directory, file_name), 'wb') as file:
            file.write(decoded_content)
        return True
    else:
        print(f'Erreur lors du téléchargement de {file_name} depuis GitHub.')
        return False

def update_file(file_name):
    import os
    import requests
    import json
    import base64
    import Wath_ER as we
    # Remplacez ces valeurs par les vôtres
    repository_owner = 'Romaxololt'
    repository_name = 'RomOS'
    local_directory = os.path.dirname(os.path.realpath(__file__))
    github_token = token()
    # Vérifier si le fichier existe localement
    local_path = os.path.join(local_directory, file_name)
    if os.path.exists(local_path):
        # Vérifier si le fichier existe sur GitHub
        github_api_url = f'https://api.github.com/repos/{repository_owner}/{repository_name}/contents/{file_name}'
        headers = {'Authorization': f'token {github_token}'}
        response = requests.get(github_api_url, headers=headers)

        if response.status_code == 200:
            # Supprimer le fichier sur GitHub
            data = json.loads(response.text)
            github_sha = data['sha']
            delete_url = f'https://api.github.com/repos/{repository_owner}/{repository_name}/contents/{file_name}'
            delete_data = {
                'message': 'Suppression du fichier depuis l\'API',
                'sha': github_sha
            }
            response = requests.delete(delete_url, headers=headers, json=delete_data)
            if response.status_code == 200:
                # Mettre à jour le fichier sur GitHub avec la version locale
                with open(local_path, 'rb') as file:
                    content = file.read()
                    update_url = f'https://api.github.com/repos/{repository_owner}/{repository_name}/contents/{file_name}'
                    update_data = {
                        'message': 'Mise à jour du fichier depuis l\'API',
                        'content': base64.b64encode(content).decode('utf-8'),
                        'sha': github_sha
                    }
                    response = requests.put(update_url, headers=headers, json=update_data)

                    if response.status_code == 200:
                        return True
                    else:
                        return False
            else:
                print(f'Erreur lors de la suppression de {file_name} sur GitHub.')
                return False
        else:
            print(f'Le fichier {file_name} n\'existe pas sur GitHub.')
            return False

    else:
        print(f'Le fichier {file_name} n\'existe pas localement.')

def create_file(file_name):
    import os
    import requests
    import base64
    import Wath_ER as we

    # Remplacez ces valeurs par les vôtres
    repository_owner = 'Romaxololt'
    repository_name = 'RomOS'
    local_directory = os.path.dirname(os.path.realpath(__file__))
    github_token = token()

    # Vérifier si le fichier existe localement
    local_path = os.path.join(local_directory, file_name)
    if os.path.exists(local_path):
        # Vérifier si le fichier existe sur GitHub
        github_api_url = f'https://api.github.com/repos/{repository_owner}/{repository_name}/contents/{file_name}'
        headers = {'Authorization': f'token {github_token}'}
        response = requests.get(github_api_url, headers=headers)

        if response.status_code == 404:
            # Le fichier n'existe pas sur GitHub, nous pouvons le créer
            with open(local_path, 'rb') as file:
                content = file.read()
                create_url = f'https://api.github.com/repos/{repository_owner}/{repository_name}/contents/{file_name}'
                create_data = {
                    'message': 'Création du fichier depuis l\'API',
                    'content': base64.b64encode(content).decode('utf-8')
                }
                response = requests.put(create_url, headers=headers, json=create_data)

                if response.status_code == 201:
                    return True
                else:
                    print(f'Erreur lors de la création du fichier {file_name} sur GitHub.')
                    return False
        else:
            print(f'Le fichier {file_name} existe déjà sur GitHub. Utilisez la fonction update_file pour le mettre à jour.(nous le faisons pour vous :)')
            update_file(file_name)
    else:
        print(f'Le fichier {file_name} n\'existe pas localement.')

def file_exists_on_github(file_name):
    import requests

    # Replace these values with your own
    repository_owner = 'Romaxololt'
    repository_name = 'RomOS'
    github_token = token()

    # Build the URL to check if the file exists on GitHub
    github_api_url = f'https://api.github.com/repos/{repository_owner}/{repository_name}/contents/{file_name}'
    headers = {'Authorization': f'token {github_token}'}
    response = requests.get(github_api_url, headers=headers)
    return response.status_code

def UpdateSysteminGit(arg="all"):
    import Wath_ER as we
    if arg == "all":
        SystemF = import_list_from_file(1)
    else:
        SystemF=arg
    allisgood = len(SystemF) * 200
    barre = we.BarreDeProgression(len(SystemF), "limit")
    final = 0
    for system in SystemF:
        code = file_exists_on_github(system)
        final += code
        if code == 200:
            line = we.get_line_Git(system, 1).replace("#", '')
            line = line.rstrip('\r')
            try:
                authcode = float(line) + 0.1
                authcode = round(authcode, 1)
            except ValueError:
                print(line)
                print(system)
            we.writeL(f"#{authcode}", 1, system)
            update_file(system)
        else:
            create_file(system)
            print(f"{system} created on GitHub")
        barre.add(1)
        barre.afficher()
    if final == allisgood:
        print("All UPD is good")
    else:
        print(f"{final} is the addition of code")
        print(f"{allisgood} is the code you should have")

####################### MACRO de Wath-ER ##############
def export_list_to_file(line, my_list, file_pathl=False):
    import os
    if file_pathl == False:
        repertoireACT = os.path.dirname(os.path.abspath(__file__))
        file_pathl = os.path.join(repertoireACT, "Save.txt")
    with open(file_pathl, 'r+') as file:
        lines = file.readlines()
        lines[line - 1] = ','.join(map(str, my_list)) + '\n'
        file.seek(0)
        file.writelines(lines)

def import_list_from_file(line, file_pathl=False):
    import os
    if file_pathl == False:
        repertoireACT = os.path.dirname(os.path.abspath(__file__))
        file_pathl = os.path.join(repertoireACT, "Save.txt")
    with open(file_pathl, 'r') as file:
        lines = file.readlines()
        try:
            line_content = lines[line - 1]
            my_list = line_content.strip().split(',')
        except (IndexError):
            print("Erreur lors de l'importation de la liste.")
            my_list = []
    return my_list
# create_file crée le fichier sur github depuis votre ordinateur
# update_file met a jour le fichier sur github depuis votre ordinateur
# download_file telecharge le fichier sur votre ordinateur depuis github 
# fileexistongithub verifie l'existence d'un fichier sur github
# Updateallsystemingit installe tout les fichier sur github depuis votre ordinateur 
''',
        "CryptROS.py": r'''#0.8
import Wath_ER
# ONE #
def encrypt_one(var):
    """Cette fonction encrypte le texte de manière sécurisée avec ROS"""

    def asciiE(text):
        """Transcrire la chaîne en ASCII"""
        ascii_text = [ord(char) for char in text]
        return ascii_text

    key = Wath_ER.copy_file("key")
    if key is None:
        Wath_ER.Error("KeyError", "003")

    key1 = Wath_ER.unicryptkey(key)
    # Utiliser eval pour évaluer l'expression
    Fkey = eval(key1)

    def transform_with_key(input_list, Fkey):
        # Nouvelle liste pour stocker les résultats
        result_list = []

        # Boucle for pour parcourir la liste d'entrée
        for num in input_list:
            # Ajouter la valeur de Fkey à chaque élément de la liste
            inc = num + Fkey
            inc2 = inc ** 2
            result_list.append(inc2)
        result_list.insert(0, "__enc__: one")

        return result_list

    var1 = asciiE(var)
    var2 = transform_with_key(var1, Fkey)
    return var2

def decrypt_one(var):
    """Cette fonction decrypte le texte de manière sécurisée avec ROS"""
    def asciiD(text):
        """Transcrire la chaîne en ASCII"""
        ascii_text = ''.join(chr(char) for char in text)
        return ascii_text

    key = Wath_ER.copy_file("key")
    if key is None:
        Wath_ER.Error("KeyError", "003")

    key1 = Wath_ER.unicryptkey(key)
    # Utiliser eval pour évaluer l'expression
    Fkey = eval(key1)

    def transform_with_key(input_list, Fkey):
        # Nouvelle liste pour stocker les résultats
        result_list = []

        # Boucle for pour parcourir la liste d'entrée
        for num in input_list:
            # Ajouter la valeur de Fkey à chaque élément de la liste
            inc = num ** 0.5
            inc2 = inc - Fkey
            inc3 = round(inc2)
            result_list.append(inc3)

        return result_list

    var1 = transform_with_key(var, Fkey)
    var2 = asciiD(var1)
    return var2



# Secure-File #
def obtenir_temps_formatte():
    from datetime import datetime
    now = datetime.now()
    date_formattee = now.strftime("%d%m%Y%H%M%S%f")
    return date_formattee

def encrypt_SF(var):
    """cette fonction encrypt avec le module Secure-File"""
    key = obtenir_temps_formatte()
    def asciiE(text):
        """Transcrire la chaîne en ASCII"""
        ascii_text = [ord(char) for char in text]
        return ascii_text
    def transform_with_key(input_list, Fkey):
        # Nouvelle liste pour stocker les résultats
        result_list = []

        # Boucle for pour parcourir la liste d'entrée
        for num in input_list:
            # Ajouter la valeur de Fkey à chaque élément de la liste
            inc = num + Fkey
            result_list.append(inc)
        result_list.insert(0, f"__enc__: SF({Fkey})")

        return result_list
    
    
    Fkey = eval(key)
    var1 = asciiE(var)
    var2 = transform_with_key(var1, Fkey)
    return var2

def decrypt_SF(var):
    for element in var:
        # Vérification si l'élément commence par '__enc__: SF('
        if isinstance(element, str) and element.startswith('__enc__: SF('):
            # Extraction de la valeur entre les parenthèses
            valeur_SF = element.split('(')[1].split(')')[0]
            break  # Arrêt du parcours après avoir trouvé la première occurrence

    def asciiD(text):
        """Transcrire la chaîne en ASCII"""
        ascii_text = ''.join(chr(char) for char in text)
        return ascii_text
    
    def transform_with_key(input_list, Fkey):
        # Nouvelle liste pour stocker les résultats
        result_list = []

        # Boucle for pour parcourir la liste d'entrée
        for num in input_list:
            # Ajouter la valeur de Fkey à chaque élément de la liste
            inc = num - Fkey
            inc3 = round(inc)
            result_list.append(inc3)

        return result_list
    
    key = eval(valeur_SF)
    var.pop(0)
    var1 = transform_with_key(var, key)
    var2 = asciiD(var1)
    return var2
    
    
# Hash #


def sha256(message):
    import struct

    # Initial hash values (pre-processing)
    h0 = 0x6a09e667
    h1 = 0xbb67ae85
    h2 = 0x3c6ef372
    h3 = 0xa54ff53a
    h4 = 0x510e527f
    h5 = 0x9b05688c
    h6 = 0x1f83d9ab
    h7 = 0x5be0cd19

    # Constants K
    k = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    ]

    # Pre-processing: Padding the message
    message = bytearray(message, 'utf-8')
    length = len(message) * 8
    message.append(0x80)
    while (len(message) * 8) % 512 != 448:
        message.append(0x00)
    message += struct.pack('>Q', length)

    # Process the message in 512-bit blocks
    for i in range(0, len(message), 64):
        block = message[i:i+64]
        w = [0] * 64

        # Break the block into 16 32-bit big-endian words
        for j in range(16):
            w[j] = struct.unpack('>I', block[j*4:j*4+4])[0]

        # Extend the first 16 words into the remaining 48 words of the message schedule array
        for j in range(16, 64):
            s0 = (w[j-15] >> 7 | w[j-15] << 25) ^ (w[j-15] >> 18 | w[j-15] << 14) ^ (w[j-15] >> 3)
            s1 = (w[j-2] >> 17 | w[j-2] << 15) ^ (w[j-2] >> 19 | w[j-2] << 13) ^ (w[j-2] >> 10)

            w[j] = (w[j-16] + s0 + w[j-7] + s1) & 0xFFFFFFFF

        # Initialize working variables to current hash value
        a, b, c, d, e, f, g, h = h0, h1, h2, h3, h4, h5, h6, h7

        # Compression function main loop
        for j in range(64):
            s0 = (a >> 2 | a << 30) ^ (a >> 13 | a << 19) ^ (a >> 22 | a << 10)
            maj = (a & b) ^ (a & c) ^ (b & c)
            t2 = s0 + maj
            s1 = (e >> 6 | e << 26) ^ (e >> 11 | e << 21) ^ (e >> 25 | e << 7)
            ch = (e & f) ^ ((~e) & g)
            t1 = h + s1 + ch + k[j] + w[j]

            h = g
            g = f
            f = e
            e = (d + t1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (t1 + t2) & 0xFFFFFFFF

        # Add the compressed chunk to the current hash value
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF
        h5 = (h5 + f) & 0xFFFFFFFF
        h6 = (h6 + g) & 0xFFFFFFFF
        h7 = (h7 + h) & 0xFFFFFFFF

    # Produce the final hash value (big-endian)
    hash_value = f"{h0:08x}{h1:08x}{h2:08x}{h3:08x}{h4:08x}{h5:08x}{h6:08x}{h7:08x}"
    return hash_value


 # XOR # 

def xor_crypt(message, key):
    # Assurez-vous que la clé est de la même longueur que le message
    key = key * (len(message) // len(key)) + key[:len(message) % len(key)]

    # Convertissez le message et la clé en représentation binaire
    message_binary = ''.join(format(ord(char), '08b') for char in message)
    key_binary = ''.join(format(ord(char), '08b') for char in key)

    # Appliquer l'opération XNOR bit à bit
    encrypted_binary = ''.join('1' if m == k else '0' for m, k in zip(message_binary, key_binary))

    # Convertir le résultat binaire en texte
    encrypted_text = ''.join(chr(int(encrypted_binary[i:i+8], 2)) for i in range(0, len(encrypted_binary), 8))

    return encrypted_text

def xor_decrypt(encrypted_text, key):
    # Appeler la fonction de cryptage car l'opération XNOR est symétrique
    return xor_crypt(encrypted_text, key)


# CryptROS sys #

def decode(var, key=None):
    if "__enc__: one" in var[0].lower():
        var.pop(0)
        return decrypt_one(var)
    elif "__enc__: sf(" in var[0].lower():
        return decrypt_SF(var)
    elif "__enc__: xor(" in var[0].lower():
        return xor_decrypt(var, key)
    else:
        print("erreur de cryptage")

    

def get_input():
    user_input = input("Entrez une liste de nombres ou de chaînes séparés par des virgules, ou entrez une liste entre crochets : ")
    
    # Vérifier si l'entrée commence par '[' et se termine par ']'
    if user_input.startswith('[') and user_input.endswith(']'):
        # Enlever les crochets et essayer de convertir en une liste d'entiers ou de chaînes
        try:
            elements = [eval(elem.strip()) for elem in user_input[1:-1].split(',')]
            return elements
        except Exception as e:
            print(f"Erreur : {e}")
            return None
    else:
        try:
            # Essayez de convertir l'entrée en une liste d'entiers ou de chaînes
            elements = [eval(elem.strip()) for elem in user_input.split(',')]
            return elements
        except Exception as e:
            print(f"Erreur : {e}")
            return None
        '''
        # Ajoutez d'autres fichiers et leurs contenus ici
    }

    # Parcours du dictionnaire et création/ajout de contenu aux fichiers
    for filename, content in file_contents.items():
        add_content_to_file(filename, content)
def Rogit(installW):
    print(f"lancement du téléchargement des dépendances ...\nfichier d'installation : {installW}")
    import requests
    import json
    import base64
    if os.path.exists(installW):
        print("")
    else:
        print(f"Le chemin '{installW}' n'existe pas.")
        error("NoValidPathFound #001")
    # Remplacez ces valeurs par les vôtres
    github_token = token()
    repository_owner = 'Romaxololt'
    repository_name = 'RomOS'
    local_directory = installW

    def download_file(file_name):
        # Construire l'URL du fichier sur GitHub
        github_api_url = f'https://api.github.com/repos/{repository_owner}/{repository_name}/contents/{file_name}'
        headers = {'Authorization': f'token {github_token}'}
        response = requests.get(github_api_url, headers=headers)

        if response.status_code == 200:
            data = json.loads(response.text)
            content = data['content']
            decoded_content = base64.b64decode(content)

            # Enregistrer le fichier localement
            with open(os.path.join(local_directory, file_name), 'wb') as file:
                file.write(decoded_content)
            return "DL"
        else:
            return file_name
    dlist = listescr
    for element in dlist:
        returndl = download_file(element)
        if returndl == "DL":
            print(f"script {element} télécharger")
        else:
            error(f"{element} ScriptNotDownloadedForAnUnknownReason #002")
    # Création du répertoire s'il n'existe pas déjà
    directory_name = "Task"
    if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "system", directory_name)):
        os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), "system", directory_name))

    # Contenu des fichiers texte
    content_task_f = "Contenu du fichier TaskF.txt"
    content_task_f_th = "Contenu du fichier TaskF__th__.txt"

    # Chemins des fichiers
    file_path_task_f = os.path.join("system", directory_name, "TaskF.txt")
    file_path_task_f_th = os.path.join("system", directory_name, "TaskF__th__.txt")

    # Création et écriture dans les fichiers
    with open(file_path_task_f, 'w') as file_task_f:
        file_task_f.write(content_task_f)

    with open(file_path_task_f_th, 'w') as file_task_f_th:
        file_task_f_th.write(content_task_f_th)

    print(f"Le répertoire '{directory_name}' et les fichiers de taches ont été créés avec succès.")

def SHORTCREATEROS():
    import os
    import shutil

    def create_shortcut(source_script, shortcut_name, icon_file):
        # Chemin du répertoire actuel
        current_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "system")

        # Chemin complet du script source
        source_script_path = os.path.join(current_directory, source_script)

        # Chemin complet du fichier ICO
        icon_path = os.path.join(current_directory, icon_file)

        # Vérifier si le fichier ICO est déjà dans le répertoire de destination
        if not os.path.exists(os.path.join(current_directory, icon_file)):
            # Copier l'icône dans le répertoire du script source
            shutil.copy(icon_path, current_directory)

        # Créer le raccourci avec le même nom que le script
        shortcut_path = os.path.join(current_directory, shortcut_name + ".lnk")

        # Créer le raccourci en utilisant le module os
        os.system(f'powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut(\'{shortcut_path}\'); $Shortcut.TargetPath = \'{source_script_path}\'; $Shortcut.IconLocation = \'{os.path.join(current_directory, icon_file)}\'; $Shortcut.Save()"')

        # Déplacer le raccourci dans le répertoire parent
        parent_directory = os.path.dirname(current_directory)
        new_shortcut_path = os.path.join(parent_directory, shortcut_name + ".lnk")
        shutil.move(shortcut_path, new_shortcut_path)

    def CREATEROSSHORT():
        # Nom du script source
        source_script = "ROS.py"

        # Nom du raccourci à créer
        shortcut_name = "ROS"

        # Nom du fichier ICO
        icon_file = "logo.ico"

        # Créer le raccourci avec l'icône spécifiée
        create_shortcut(source_script, shortcut_name, icon_file)
    CREATEROSSHORT()
def error(type="inconnue"):
    print(f"le script a eu une erreur fatal du type : {type}\nsi vous ne comprenez pas votre erreur lancez Wath-ERcmd et inscrivez le code erreur (#xxx)")
    input("appuyer sur une touche pour fermer le setup\n>>")
    raise SystemExit

if installo == "":
    import os

    # Obtenez le chemin absolu du répertoire actuel
    chemin_actuel = os.path.abspath(os.path.dirname(__file__))

    # Nom du dossier que vous souhaitez créer
    nom_dossier = "system"

    # Chemin complet du dossier à créer
    chemin_dossier = os.path.join(chemin_actuel, nom_dossier)

    # Vérifiez si le dossier n'existe pas déjà avant de le créer
    if not os.path.exists(chemin_dossier):
        # Créez le dossier
        os.mkdir(chemin_dossier)
        print(f"Le dossier '{nom_dossier}' a été créé avec succès dans le répertoire actuel.")
    else:
        print(f"Le dossier '{nom_dossier}' existe déjà dans le répertoire actuel.")

    installo = os.path.dirname(os.path.realpath(__file__))
    installW = os.path.join(installo, "system") 
def move_key():
    import shutil
    import os
    actuel = os.path.dirname(os.path.abspath(__file__))
    actkey = os.path.join(actuel, "key")
    new = os.path.join(actuel, "system")
    shutil.move(actkey, new)
# Script Python
# Écriture du contenu dans le fichier .bat
with open('ROSinstaller.bat', 'w') as bat_file:
    bat_file.write(bat)
# Exécution du fichier .bat
import subprocess
subprocess.run(['ROSinstaller.bat'], shell=True)
if internet():
    Rogit(installW)
else:
    print("nous avons détéctée que vous n'etes pas connécté a internet lancement du telechargement sans internet des version de base veuillez a les mettres a jour car il peuvent comporter des bugs")
    dlNOinternet(installW)
print("installation systeme fini configurations finales")
print("installation du raccourcis de ROS")
SHORTCREATEROS()
print("finalisation et auto-configuration du systeme")
from colorama import *
init()
move_key()
print(Fore.BLUE + "installation terminée veuillez patientez 5 secondes pour l'A-D de ce script")
import time 
time.sleep(5)
import sys
chemin_actuel2 = os.path.abspath(os.path.dirname(__file__))
chemin_actuel3 = os.path.join(chemin_actuel2, "ROSinstaller.bat")
if not cmd.lower() == "/G":
    os.remove(chemin_actuel3)
def self_destruct():
    try:
        # Obtenez le chemin absolu du script
        script_path = os.path.abspath(sys.argv[0])

        # Supprimez le fichier du script
        os.remove(script_path)

        print(f"Le script {script_path} a été supprimé avec succès.")
    except Exception as e:
        print(f"Erreur lors de la suppression du script : {e}")
# Appel de la fonction d'autodestruction
if not cmd.lower() == "/G":
    self_destruct()


