
'''
1 - Reverta a ordem das palavras nas frases, mantendo a ordem das palavras.
a. Input: "Hello, World! OpenAI is amazing."
b. Output: "amazing. is OpenAi World! Hello,"
'''

def reverter_ordem(frase):
    frase = frase.split(' ')
    frase.reverse()
    frase_inversa = ' '.join(frase)   
    return frase_inversa

'''
2 - Remova todos os caracteres duplicados da string abaixo:
a. Input: "Hello, World!"
b. Output: "Helo, Wrd!"
'''

def remover_duplicados(frase):
    frase = frase.lower().split()
    frase_limpa = []
    for palavra in frase:
        palavra+=' '
        for letra in palavra:
            if letra not in frase_limpa or letra==' ':
                frase_limpa.append(letra)
    frase_limpa = ''.join(frase_limpa)
    return(frase_limpa)
        

'''
3 - Encontre a substring palindroma mais longa na string abaixo:
a. Input: "babad"
b. Output: "bab"
'''

def palindromo(palavra):
    maior_s = ""
    for i in range(len(palavra)):
        for j in range(i+1, len(palavra)+1):
            substring = palavra[i:j]
            if substring == substring[::-1] and len(substring) > len(maior_s):
                maior_s = substring
    return maior_s

'''
4 - Coloque em maiúscula a primeira leitra de cada frase na string:
a. Input "hello. how are you? i'm fine, thank you."
b. Output "Hello. How are you? I'm fine, thank you."
'''

def maiuscula(frase):
    frases=[]
    signal = 0
    frase_inicial = frase.capitalize().split()
    for frase in frase_inicial:
        if signal == 1:
            frase = frase.capitalize()
            signal =0
        elif '.' in frase or '?' in frase:
            signal = 1
        frases.append(frase)
    frases = ' '.join(frases)
    return(frases)

'''
5 - Verifique se a string é um anagrama de um palindromo:
a. Input: "racecar"
b. Output: true
'''

def anagrama(palavra):
    palavra_inicial = list(palavra)
    print(palavra_inicial)
    palavra_final = palavra_inicial[::-1]
    if palavra_inicial == palavra_final:
        palavra_inicial.sort()
        palavra_final.sort()
        if palavra_inicial == palavra_final:
            return True
        else:
            return False
    else:
        return False


