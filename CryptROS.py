#0.2
#0.1
import Wath_ER
# ONE #
def encrypt_one(var):
    """Cette fonction encrypte le texte de manière sécurisée avec ROS"""

    def asciiE(text):
        """Transcrire la chaîne en ASCII"""
        ascii_text = [ord(char) for char in text]
        return ascii_text

    key = Wath_ER.copy_file("key")
    if key is None:
        Wath_ER.Error("KeyError", "003")

    key1 = Wath_ER.unicryptkey(key)
    # Utiliser eval pour évaluer l'expression
    Fkey = eval(key1)

    def transform_with_key(input_list, Fkey):
        # Nouvelle liste pour stocker les résultats
        result_list = []

        # Boucle for pour parcourir la liste d'entrée
        for num in input_list:
            # Ajouter la valeur de Fkey à chaque élément de la liste
            inc = num + Fkey
            inc2 = inc ** 2
            result_list.append(inc2)
        result_list.insert(0, "__enc__: one")

        return result_list

    var1 = asciiE(var)
    var2 = transform_with_key(var1, Fkey)
    return var2

def decrypt_one(var):
    """Cette fonction decrypte le texte de manière sécurisée avec ROS"""
    def asciiD(text):
        """Transcrire la chaîne en ASCII"""
        ascii_text = ''.join(chr(char) for char in text)
        return ascii_text

    key = Wath_ER.copy_file("key")
    if key is None:
        Wath_ER.Error("KeyError", "003")

    key1 = Wath_ER.unicryptkey(key)
    # Utiliser eval pour évaluer l'expression
    Fkey = eval(key1)

    def transform_with_key(input_list, Fkey):
        # Nouvelle liste pour stocker les résultats
        result_list = []

        # Boucle for pour parcourir la liste d'entrée
        for num in input_list:
            # Ajouter la valeur de Fkey à chaque élément de la liste
            inc = num ** 0.5
            inc2 = inc - Fkey
            inc3 = round(inc2)
            result_list.append(inc3)

        return result_list

    var1 = transform_with_key(var, Fkey)
    var2 = asciiD(var1)
    return var2



# Secure-File #
def obtenir_temps_formatte():
    from datetime import datetime
    now = datetime.now()
    date_formattee = now.strftime("%d%m%Y%H%M%S%f")
    return date_formattee

def encrypt_SF(var):
    """cette fonction encrypt avec le module Secure-File"""
    key = obtenir_temps_formatte()
    def asciiE(text):
        """Transcrire la chaîne en ASCII"""
        ascii_text = [ord(char) for char in text]
        return ascii_text
    def transform_with_key(input_list, Fkey):
        # Nouvelle liste pour stocker les résultats
        result_list = []

        # Boucle for pour parcourir la liste d'entrée
        for num in input_list:
            # Ajouter la valeur de Fkey à chaque élément de la liste
            inc = num + Fkey
            result_list.append(inc)
        result_list.insert(0, f"__enc__: SF({Fkey})")

        return result_list
    
    
    Fkey = eval(key)
    var1 = asciiE(var)
    var2 = transform_with_key(var1, Fkey)
    return var2

def decrypt_SF(var):
    for element in var:
        # Vérification si l'élément commence par '__enc__: SF('
        if isinstance(element, str) and element.startswith('__enc__: SF('):
            # Extraction de la valeur entre les parenthèses
            valeur_SF = element.split('(')[1].split(')')[0]
            break  # Arrêt du parcours après avoir trouvé la première occurrence

    def asciiD(text):
        """Transcrire la chaîne en ASCII"""
        ascii_text = ''.join(chr(char) for char in text)
        return ascii_text
    
    def transform_with_key(input_list, Fkey):
        # Nouvelle liste pour stocker les résultats
        result_list = []

        # Boucle for pour parcourir la liste d'entrée
        for num in input_list:
            # Ajouter la valeur de Fkey à chaque élément de la liste
            inc = num - Fkey
            inc3 = round(inc)
            result_list.append(inc3)

        return result_list
    
    key = eval(valeur_SF)
    var.pop(0)
    var1 = transform_with_key(var, key)
    var2 = asciiD(var1)
    return var2
    




# CryptROS sys #

def decode(var):
    if "__enc__: one" in var[0].lower():
        var.pop(0)
        return decrypt_one(var)
    elif "__enc__: sf(" in var[0].lower():
        return decrypt_SF(var)
    else:
        print("erreur de cryptage")

    

def get_input():
    user_input = input("Entrez une liste de nombres ou de chaînes séparés par des virgules, ou entrez une liste entre crochets : ")
    
    # Vérifier si l'entrée commence par '[' et se termine par ']'
    if user_input.startswith('[') and user_input.endswith(']'):
        # Enlever les crochets et essayer de convertir en une liste d'entiers ou de chaînes
        try:
            elements = [eval(elem.strip()) for elem in user_input[1:-1].split(',')]
            return elements
        except Exception as e:
            print(f"Erreur : {e}")
            return None
    else:
        try:
            # Essayez de convertir l'entrée en une liste d'entiers ou de chaînes
            elements = [eval(elem.strip()) for elem in user_input.split(',')]
            return elements
        except Exception as e:
            print(f"Erreur : {e}")
            return None
        
