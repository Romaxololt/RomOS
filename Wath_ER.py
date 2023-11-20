# Wath_ER Socket ROS V0.1.1
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

def get_line(line_number):
    """obtiens la ligne de Save.txt """
    import os
    repertoireACT = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(repertoireACT, "Save.txt")
    try:
        with open(file_path, 'r') as file:
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
    import json
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
    
def unicryptdec(chaine):
    """enleve les virgule """
    chaine_sans_virgules = chaine.replace(',', '')
    return chaine_sans_virgules

def unicryptkey(chaine):
    """enleve les virgule et les remplace par +"""
    chaine_sans_virgules = chaine.replace(',', '+')
    return chaine_sans_virgules

def writeL(chaine, numero_ligne):
    """écrit une valeur dans une ligne de Save.txt"""
    try:
        # Ouvrir le fichier en mode écriture
        with open("Save.txt", "r") as file:
            lines = file.readlines()
        
        # Vérifier si la ligne spécifiée existe
        if 1 <= numero_ligne <= len(lines) + 1:
            # Insérer la chaîne à la ligne spécifiée
            lines.insert(numero_ligne - 1, chaine + '\n')

            # Réécrire le fichier avec la nouvelle version
            with open("Save.txt", "w") as file:
                file.writelines(lines)
        else:
            print("Le numéro de ligne spécifié est hors de portée.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

def Error(typeE, code):
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

def Decode_with_CryptROS(text):
    """decrypte une valeur (ne pas oublier le systeme de cryptage en position 1)"""
    from CryptROS import decode
    return decode(text)

def Decode_enter_CryptROS():
    """decrypte une valeur (ne pas oublier le systeme de cryptage en position 1)"""
    from CryptROS import decode, get_input
    return decode(get_input())