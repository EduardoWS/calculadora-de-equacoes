from math import sqrt
from time import sleep

semcor = '\033[m'
azul = '\033[1;34m'
vermelho = '\033[1;31m'
branco = '\033[1;30m'
amarelo = '\033[1;33m'
verde = '\033[1;36m'

print('--' * 21)
print(f'{azul} Calculadora de Equações do Segundo Grau {semcor}   v3.1')

pergunta = 'S'

while pergunta != 'N':
    
    print('--' * 21)
    print('Formato de uma Equação do Segundo Grau:')
    print(f'          {azul} ax² + bx + c = 0 {semcor}')
    print()
    
    a = int(input(f'{branco}Digite o valor de A:{semcor} '))

    if a == 0:
        print()
        print(f'{vermelho}Não existe função do segundo grau \ncom A nulo.{semcor}')
        print('--' * 21)
        print()
        pergunta = str(input(f'>> {branco}Novos valores? [S/N]{semcor} ')).upper().strip()
        print()
        if pergunta == 'S':
            continue
        else:
            print('Encerrando...')
            sleep(2)
            print('--' * 21)
            exit()

    b = int(input(f'{branco}Digite o valor de B:{semcor} '))
    c = int(input(f'{branco}Digite o valor de C:{semcor} '))

    delta = (b**2) -4 * a * c

    print()
    print('Carregando...')
    print()
    sleep(2)

    if delta < 0:
        print(f'> {verde}Delta = {delta} {semcor}')
        print(f'{vermelho}Delta é menor que zero!{semcor}')
        print(f'> {amarelo}Se o delta for menor que zero, \na equação não possuirá valores reais.{semcor}')

    elif delta == 0:
        print(f'> {verde}Delta = {delta} {semcor}')
        print(f'{vermelho}Delta é igual a zero!{semcor}')
        print(f'> {amarelo}Se o delta for igual a zero,\na equação terá somente um valor real '
              f'\nou dois resultados iguais.{semcor} ')
        x = -b / (2 * a)
        print()
        print(f'{azul}x = {x} {semcor}')

    elif delta > 0:
        print(f'> {verde}Delta = {delta} {semcor}')
        print(f'{vermelho}Delta é maior que zero!{semcor}')
        print(f'> {amarelo}Se o delta for maior que zero, \na equação terá dois valores reais \ne distintos.{semcor}')
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        print()
        print(f'{azul}x1 = {x1} {semcor}')
        print(f'{azul}x2 = {x2} {semcor}')
    
    print()
    pergunta = str(input(f'>> {branco}Novos valores? [S/N]{semcor} ')).upper().strip()
    print()

print('Encerrando...')
sleep(2)
print('--' * 21)
