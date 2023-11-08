# Assim como podemos percorrer qualquer sequência ou grupo usando um comando for e um comando in, podemos usar o comando if e um comando in para verificar se um elemento existe dentro da sequência ou grupo
texto = "Uma sequência de caracteres."
conjunto = (1, 2, 3, 4, 0, -1)
if "e" in texto:
    print("O caractere 'e' está na presente no texto")
else:
    print("O caractere 'e' NÃO está na presente no texto")
if 5 in conjunto:
    print("O número 5 está presente no conjunto")
else:
    print("O número 5 NÃO está presente no conjunto")