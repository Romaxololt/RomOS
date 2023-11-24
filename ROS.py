from Thor import ThorX
import subprocess
import os

# Obtenez le chemin absolu du répertoire du script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Définissez le répertoire de travail sur le répertoire du script
os.chdir(script_dir)

# Maintenant, le répertoire de travail est configuré correctement

ThorX("core.py")
subprocess.run("python GT8+.py")