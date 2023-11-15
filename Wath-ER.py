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

# Exemple d'utilisation
launchX("core.py")
