import os
import threading
import time

# Définition de la fonction pour exécuter une tâche
def execute_task(task):
    if task.endswith(" __th__"):
        task = task.replace(" __th__", "")
        thread = threading.Thread(target=execute_task, args=(task,))
        thread.start()
    else:
        # Vérifie si le fichier de script existe avant de l'exécuter
        if os.path.isfile(task):
            os.system(f"python {task}")
        else:
            print(f"Le fichier de script {task} n'existe pas. La tâche est ignorée.") ################# à refaire avec Wath_ER
        remove_task(task)


# Supprime une tâche du fichier de tâches
def remove_task(task):
    with open("taskF.txt", "r") as file:
        lines = file.readlines()
    with open("taskF.txt", "w") as file:
        for line in lines:
            if line.strip() != task:
                file.write(line)

def check_pending_tasks():
    while True:
        with open("taskF.txt", "r") as file:
            tasks = file.readlines()
        pending_tasks = [task.strip() for task in tasks if task.strip() and task.strip() != "__processing__"]
        if pending_tasks:
            return
        time.sleep(1)

# Nombre maximal de threads en parallèle
max_threads = 8

# Lecture des tâches depuis le fichier texte
with open("taskF.txt", "r") as file:
    tasks = file.readlines()

# Exécution des tâches en parallèle
while True:
    with open("taskF.txt", "r") as file:
        tasks = file.readlines()
    pending_tasks = [task.strip() for task in tasks if task.strip() and task.strip() != "__processing__"]
    if not pending_tasks:
        check_pending_tasks()
        continue

    running_threads = []
    for task in pending_tasks:
        while len(running_threads) >= max_threads:
            for thread in running_threads:
                if not thread.is_alive():
                    running_threads.remove(thread)
                    break
        execute_task(task)
        running_threads.append(threading.current_thread())

