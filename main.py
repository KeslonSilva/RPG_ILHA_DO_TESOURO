print('Bem vindo(a) a ilha do tesouro !')
print('Sua missão é procurar o Tesouro')
print('\n')

lado = str(input('Para qual lado vocÊ quer ir ? DIREITA ou ESQUERDA ? '))
if lado == ('DIREITA'):
    print('GAME OVER')
else:
    print('Muito bem !')
    print('\n')
    print('Agora você está de frente a um lago !\n')
    
    atravessar = input('Você prefere atrevessar o lago NADANDO ou ESPERAR UM BARCO ?\n')

    if atravessar == ('NADANDO'):
        print('GAME OVER')
    else:
        print('Você conseguiu chegar ao outro lado, qual porta você escolhe ?\n')
      
        porta = input('AMARELO, AZUL OU VERMELHO\n')
                
        if porta == ('AMARELO') or ('amarelo') or ('Amarelo'):
            print('Parabéns, você encontrou o TESOURO PERDIDO')
            print('Você VENCEU O GAME !')
        else:
            print('GAME OVER')
                    

    