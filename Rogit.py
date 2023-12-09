#0.2
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
#fl = [""]
#fl = "all"
