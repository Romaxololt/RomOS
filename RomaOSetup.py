version = "alpha 0.1"
import os
print("\n")
print(f"Bonjour et bienvenue dans le setup d'installation de ROS V {version}.")
print("Le lancement de l'installation téléchargera les scripts par défaut suivants : GT8, Internet, TaskF, ROS, Wath-ER, Core, CryptoRoma, Configurator, IslandX, AStorm.")
input("Appuyez sur une touche pour lancer l'installation. Vous acceptez également les conditions d'utilisation.")
installW = input("entrée le chemin avec un format convenable \n>>")
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
    github_token = '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'
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

    def update_file(file_name):
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
                            return "A"
                        else:
                            return "E"
                else:
                    print(f'Erreur lors de la suppression de {file_name} sur GitHub.')
                    return "E"
            else:
                print(f'Le fichier {file_name} n\'existe pas sur GitHub.')
                return "E"

        else:
            print(f'Le fichier {file_name} n\'existe pas localement.')
    dlist = "core.py","Ctone.py","ErreurLST.txt","GT8+.py","Log.txt","Logo.ico","ROS.py","Thor.py","Wath-ER.py","Rogit.py"
    for element in dlist:
        returndl = download_file(element)
        if returndl == "DL":
            print(f"script {element} télécharger")
        else:
            error(f"{element} ScriptNotDownloadedForAnUnknownReason #002")
if installW == "":
    installW = os.path.dirname(os.path.realpath(__file__))
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
def VerifConfig():
    print("")
def error(type="inconnue"):
    print(f"le script a eu une erreur fatal du type : {type}\nsi vous ne comprenez pas votre erreur lancez Wath-ERcmd et inscrivez le code erreur (#xxx)")
    input("appuyer sur une touche pour fermer le setup\n>>")
    raise SystemExit
VerifConfig()
Rogit(installW)
print("installation systeme fini configurations finales")
print("installation du raccourcis de ROS")
SHORTCREATEROS()
input("installation terminée lancer ROS.py !")