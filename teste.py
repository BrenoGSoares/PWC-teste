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

'''
4 - Coloque em maiúscula a primeira leitra de cada frase na string:
a. Input "hello, how are you? i'm fine, thank you."
b. Output "Hello, How are you? I'm fine, thank you."
'''

'''
5 - Verifique se a string é um anagrama de um palindromo:
a. Input: "racecar"
b. Output: true
'''

print(remover_duplicados("Hello, World!"))