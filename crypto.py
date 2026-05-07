def fonction_hash(message):
    hash_valeur = 0

    for caractere in message:
        hash_valeur = (hash_valeur * 31 + ord(caractere)) % 100000

    return hash_valeur

texte = "olivier"

print("Hash :", fonction_hash(texte))
