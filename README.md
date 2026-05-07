 KIVIDI MALANGA OLIVIER


Cette fonction permet de transformer un message "OLIVIER"en une valeur numérique appelée hash.

Elle parcourt chaque caractère du texte et utilise son code ASCII grâce à ord().

Ensuite, les valeurs sont mélangées avec la formule :

hash_valeur = (hash_valeur * 31 + ord(caractere)) % 100000

Le but est d’obtenir une empreinte du message.

Par exemple :
"abc" et "abd" donneront des hash différents.

Cette méthode n’est pas très sécurisée, mais elle aide à comprendre le fonctionnement d’une fonction de hachage.
