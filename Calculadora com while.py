""" Calculadora com while """
import os
import time

while True:
    numero_1 = input(f'\nDigite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None

    num_1_float = 0
    num_2_float = 0

    
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except :
        numeros_validos = None

    if numeros_validos is None:
        print('\nUm ou ambos os números são inválidos.')
        time.sleep(3)
        os.system('cls')
        continue

    operadores_permitidos = '+-/*'

    if operador  not in operadores_permitidos:
        print('\nOperador inválido.')
        time.sleep(2)
        
    if len(operador) > 1:
        print('\nDigite apenas um operador.')
        time.sleep(2)
        os.system('cls')
        continue


    soma = num_1_float + num_2_float
    subtracao = num_1_float - num_2_float
    divisao = num_1_float / num_2_float
    multiplicacao = num_1_float * num_2_float

    print(f'\nConfira o resultado abaixo:')

    if operador == '+':
        resultado = soma
        print(f'\n{num_1_float} + {num_2_float}  =  {resultado}')

    elif operador == '-':
        resultado = subtracao
        print(f'\n{num_1_float} - {num_2_float}  =  {resultado}')
        
    elif operador == '/':
        resultado = divisao
        print(f'\n{num_1_float} / {num_2_float}  =  {resultado}')

    elif operador == '*':
        resultado = multiplicacao
        print(f'\n{num_1_float} x {num_2_float}  =  {resultado}')

    else:
        print('Nunca devia chegar aqui.')

    sair = input(f'\nContinuar[ENTER]\nSair[S] ').lower().startswith('s' or 'enter') 


    if sair is True:
        break

print(f'\nSaiu...')
