#0.6
#0.5
#0.4
#0.3
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
    
