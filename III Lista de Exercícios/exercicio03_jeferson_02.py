# -*- coding: utf-8 -*-

parada = True

while parada:
    nome = raw_input('Nome do usuário: ')
    senha = raw_input('Senha do usuário: ')

    if nome == senha:
        print 'Valor inválido'
    else:
        print 'Valor válido'
        parada = False
