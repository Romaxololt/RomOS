#0.5
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
    
    
# Hash #


def sha256(message):
    import struct

    # Initial hash values (pre-processing)
    h0 = 0x6a09e667
    h1 = 0xbb67ae85
    h2 = 0x3c6ef372
    h3 = 0xa54ff53a
    h4 = 0x510e527f
    h5 = 0x9b05688c
    h6 = 0x1f83d9ab
    h7 = 0x5be0cd19

    # Constants K
    k = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    ]

    # Pre-processing: Padding the message
    message = bytearray(message, 'utf-8')
    length = len(message) * 8
    message.append(0x80)
    while (len(message) * 8) % 512 != 448:
        message.append(0x00)
    message += struct.pack('>Q', length)

    # Process the message in 512-bit blocks
    for i in range(0, len(message), 64):
        block = message[i:i+64]
        w = [0] * 64

        # Break the block into 16 32-bit big-endian words
        for j in range(16):
            w[j] = struct.unpack('>I', block[j*4:j*4+4])[0]

        # Extend the first 16 words into the remaining 48 words of the message schedule array
        for j in range(16, 64):
            s0 = (w[j-15] >> 7 | w[j-15] << 25) ^ (w[j-15] >> 18 | w[j-15] << 14) ^ (w[j-15] >> 3)
            s1 = (w[j-2] >> 17 | w[j-2] << 15) ^ (w[j-2] >> 19 | w[j-2] << 13) ^ (w[j-2] >> 10)

            w[j] = (w[j-16] + s0 + w[j-7] + s1) & 0xFFFFFFFF

        # Initialize working variables to current hash value
        a, b, c, d, e, f, g, h = h0, h1, h2, h3, h4, h5, h6, h7

        # Compression function main loop
        for j in range(64):
            s0 = (a >> 2 | a << 30) ^ (a >> 13 | a << 19) ^ (a >> 22 | a << 10)
            maj = (a & b) ^ (a & c) ^ (b & c)
            t2 = s0 + maj
            s1 = (e >> 6 | e << 26) ^ (e >> 11 | e << 21) ^ (e >> 25 | e << 7)
            ch = (e & f) ^ ((~e) & g)
            t1 = h + s1 + ch + k[j] + w[j]

            h = g
            g = f
            f = e
            e = (d + t1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (t1 + t2) & 0xFFFFFFFF

        # Add the compressed chunk to the current hash value
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF
        h5 = (h5 + f) & 0xFFFFFFFF
        h6 = (h6 + g) & 0xFFFFFFFF
        h7 = (h7 + h) & 0xFFFFFFFF

    # Produce the final hash value (big-endian)
    hash_value = f"{h0:08x}{h1:08x}{h2:08x}{h3:08x}{h4:08x}{h5:08x}{h6:08x}{h7:08x}"
    return hash_value



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
        
