
print('Test to see if your number is in the fibonacci sequence')


def calculadora_fibonacci():
    numero_para_teste = int(input("Number to be tested: "))
    indice1 = 1
    indice2 = 0
    fibo = False
    fibo_anterior = []
    if numero_para_teste == 0:
        print('Your number is in the fibonacci sequence')
        print('Your number is: ' + str(numero_para_teste))
        fibo = True
    else:
        while indice2 < numero_para_teste:
            indice2 = indice1 + indice2
            fibo_anterior.append(indice2)

            indice1 = indice2 - indice1
            if numero_para_teste == indice2:
                print('Your number is in the fibonacci sequence')
                print('Your number is: ' + str(numero_para_teste))
                fibo = True
                break
        if fibo == False:
            print('Your number is not in the fibonacci sequence')
    print("Previous and current fibonacci numbers:" + str(fibo_anterior))
sair = False

while True:
    calculadora_fibonacci()
    sim_ou_nao = input('Do you wish to continue? (Y/N)? ').lower()
    if sim_ou_nao != 'y':
        break