import random

def elige_palabra(fichero="palabras.txt"):
    """
    Devuelve una palabra aleatoria tomada de un fichero de texto.

    Parámetros:
        fichero: ruta al archivo que contiene las palabras (una por línea).

    Devuelve:
        Una palabra (str) elegida al azar del fichero.
    """
    with open(fichero, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    # Quitar saltos de línea y espacios
    palabras = [linea.strip() for linea in lineas if linea.strip() != ""]
    return random.choice(palabras)


def normalizar(cadena: str) -> str:
    """
    Normaliza una cadena de texto realizando las siguientes operaciones:
        - convierte a minúsculas
        - quita espacios en blanco al principio y al final
        - elimina acentos y diéresis        
    
    Parámetros:
      cadena: cadena de texto que hay que sanear
    
    Devuelve:
      Cadena de texto con la palabra normalizada
    """
    cadena = cadena.lower().strip().replace("á", "a").replace("ä", "a").replace("é", "e").replace("ë", "e").replace("í","i").replace("ï", "i").replace("ó", "o").replace("ö", "o").replace("ú", "u").replace("ü", "u")
    return cadena

def enmascarar(palabra_secreta, letras_usadas=""):
    '''Devuelve una cadena de texto con la palabra enmascarada. 
    Las letras que no están en letras_usadas se muestran como guiones bajos (_).

    Parámetros:
    - palabra_secreta: cadena de texto con la palabra que se debe enmascarar
    - letras_usadas: cadena de texto con las letras que se deben mostrar (por defecto cadena vacía)

    Devuelve:
      Cadena de texto con la palabra enmascarada
    '''
    res = ""
    for c in palabra_secreta:
        if c in letras_usadas:
            res += c
        else:
            res += "_"
    return  res


def ha_ganado(palabra_enmascarada):
    '''Devuelve True si el jugador ha ganado (es decir, si no quedan letras por descubrir en la palabra enmascarada).

    Parámetros:
    - palabra_enmascarada: cadena de texto con la palabra enmascarada 

    Devuelve:
    - True si el jugador ha ganado, False en caso contrario
    '''
    return "_" not in palabra_enmascarada



def mostrar_estado(palabra_enmascarada, letras_usadas , intentos_restantes):

    print("Estado: ", " ".join(palabra_enmascarada))
    if letras_usadas == "":
        print("Letras usadas: ninguna")
    else:
        print("Letras usadas: ", letras_usadas)
    print("Intentos restante: ", intentos_restantes)


def pedir_letra(letras_usadas):
    while True:
        letra = input("Introduce una letra: ").lower()
        if len(letra) != 1 or not letra.isalpha():
            print("Tienes que introducir una única letra")
        elif letra in letras_usadas:
            print("Esa letra ya la has usado anteriormente")
        else:
            return letra

def jugar(palabra_secreta):
    palabra_secreta = normalizar(palabra_secreta)
    if palabra_secreta == "" :
        return None

    intentos_restantes = 6
    letras_usadas = ""
    palabra_enmascarada = enmascarar(palabra_secreta, letras_usadas)
    mostrar_estado(palabra_enmascarada, letras_usadas, intentos_restantes)
    
    while intentos_restantes > 0 and not ha_ganado(palabra_enmascarada):
        letra = pedir_letra(letras_usadas)
        letras_usadas = letras_usadas + letra
        if letra not in palabra_secreta:
            print("Esa letra no se encuentra en la palabra secreta")
            intentos_restantes -= 1
        else:
            print("La letra se encuentra en la palabra secreta")
            palabra_enmascarada = enmascarar(palabra_secreta, letras_usadas)
        mostrar_estado(palabra_enmascarada, letras_usadas, intentos_restantes)

    if not ha_ganado(palabra_enmascarada):
        print("Has perdido")
        print("La palabra secreta era: ", palabra_secreta)
    else:
        print("Has ganado")







# TODO: Implementa la función pedir_letra

# TODO: Implementa la función jugar

# TODO: Escribe el programa principal
