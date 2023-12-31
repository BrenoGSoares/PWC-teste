
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
        elif '.' in frase or '?' in frase or '!' in frase:
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


def main():
    while True:
        option = input('Escolha um exercício (1 a 5) fora isso a aplicação fecha: ')
        if option == '1':
            print('Reverta a ordem das palavras nas frases, mantendo a ordem das palavras')
            caso_teste = ('Hello, World! OpenAI is amazing.')
            print (caso_teste)
            print(reverter_ordem(caso_teste))
            user = input('Digite a frase: ')
            print(reverter_ordem(user))
        elif option == '2':
            print('Remova todos os caracteres duplicados da string abaixo')
            caso_teste = ('Hello, World!')
            print (caso_teste)
            print(remover_duplicados(caso_teste))
            user = input('Digite a frase: ')
            print(remover_duplicados(user))
        elif option == '3':
            print('Encontre a substring palindroma mais longa na string abaixo')
            caso_teste = ('babad')
            print (caso_teste)
            print(palindromo(caso_teste))
            user = input('Digite a frase: ')
            print(palindromo(user))
        elif option == '4':
            print('Coloque em maiúscula a primeira leitra de cada frase na string')
            caso_teste = ("hello. how are you? i'm fine, thank you")
            print (caso_teste)
            print(maiuscula(caso_teste))
            user = input('Digite a frase: ')
            print(maiuscula(user))
        elif option == '5':
            print('Verifique se a string é um anagrama de um palindromo')
            caso_teste = ('racecar')
            print (caso_teste)
            print(anagrama(caso_teste))
            user = input('Digite a palavra: ')
            print(anagrama(user.lower()))
        else:
            break
main()