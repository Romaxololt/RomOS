#0.4
#0.2
#0.1
from Thor import ThorX
import subprocess
import os

# Obtenez le chemin absolu du répertoire du script
script_dir = os.path.dirname(os.path.abspath(__file__))

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
    NCl("1")
    Reboot()

os.system("cls")
ThorX("core.py")
subprocess.run("python GT8+.py")