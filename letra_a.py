from logging import ERROR


def identifica_letra_a():
    texto_de_input = input('Digite aqui seu texto: ')
    texto_de_input = texto_de_input.lower()
    count = 0
    letra_encontrada = False
    for letra in texto_de_input:
        if letra=='a':
            letra_encontrada = True
            count += 1
    return letra_encontrada, count
resultado = identifica_letra_a()

if resultado[0]:
    print('O texto contém a letra a')
    print('A letra a foi encontrada ' + str(resultado[1]) + ' vezes')
elif not resultado[0]:
    print('O texto não contêm a letra a')
else:
    print('Erro desconhecido.')
