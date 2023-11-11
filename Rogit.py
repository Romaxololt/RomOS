def download_file(file_name):
    import os
    import requests
    import json
    import base64
    # Remplacez ces valeurs par les vôtres
    github_token = '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'
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
    else:
        print(f'Erreur lors du téléchargement de {file_name} depuis GitHub.')

def update_file(file_name):
    import os
    import requests
    import json
    import base64
    # Remplacez ces valeurs par les vôtres
    github_token = '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'
    repository_owner = 'Romaxololt'
    repository_name = 'RomOS'
    local_directory = os.path.dirname(os.path.realpath(__file__))
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
                        print("")
                    else:
                        print(f'')
            else:
                print(f'Erreur lors de la suppression de {file_name} sur GitHub.')
        else:
            print(f'Le fichier {file_name} n\'existe pas sur GitHub.')

    else:
        print(f'Le fichier {file_name} n\'existe pas localement.')

def create_file(file_name):
    import os
    import requests
    import base64

    # Remplacez ces valeurs par les vôtres
    github_token = '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'
    repository_owner = 'Romaxololt'
    repository_name = 'RomOS'
    local_directory = os.path.dirname(os.path.realpath(__file__))

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
                    print(f'')
                else:
                    print(f'Erreur lors de la création du fichier {file_name} sur GitHub.')
        else:
            print(f'Le fichier {file_name} existe déjà sur GitHub. Utilisez la fonction update_file pour le mettre à jour.(nous le faisons pour vous :)')
            update_file(file_name)
    else:
        print(f'Le fichier {file_name} n\'existe pas localement.')

def file_exists_on_github(file_name):
    import requests

    # Replace these values with your own
    github_token = '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'
    repository_owner = 'Romaxololt'
    repository_name = 'RomOS'

    # Build the URL to check if the file exists on GitHub
    github_api_url = f'https://api.github.com/repos/{repository_owner}/{repository_name}/contents/{file_name}'
    headers = {'Authorization': f'token {github_token}'}
    response = requests.get(github_api_url, headers=headers)
    return response.status_code

def UpdateAllSysteminGit():
    SystemF = ["core.py", "Ctone.py", "ErreurLST.txt", "GT8+.py", "Log.txt", "Logo.ico", "RomaOSetup.py", "ROS.py", "Thor.py", "Wath-ER.py"]
    allisgood = len(SystemF) * 200
    final = 0
    for system in SystemF:
        code = file_exists_on_github(system)
        final += code
        if code == 200:
            update_file(system)
            print(f"{system} updated on GitHub")
        else:
            create_file(system)
            print(f"{system} created on GitHub")
    if final == allisgood:
        print("All UPD is good")
    else:
        print(f"{final} is the addition of code")
        print(f"{allisgood} is the code you should have")
# create_file crée le fichier sur github depuis votre ordinateur
# update_file met a jour le fichier sur github depuis votre ordinateur
# download_file telecharge le fichier sur votre ordinateur depuis github 
# fileexistongithub verifie l'existence d'un fichier sur github
# Updateallsystemingit installe tout les fichier sur github depuis votre ordinateur 

