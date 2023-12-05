#0.5
version = "alpha 0.3"
import os
listescr = "core.py","Ctone.py","GT8+.py","Logo.ico","ROS.py","Thor.py","Wath_ER.py","Rogit.py","CryptROS.py"
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
set "libraries=requests shutil json base64 datetime"

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
Rogit(installW)
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


