from time import sleep
from random import randint

print('''PRONTO PARA JOGAR JOKEMPO?
[0] Pedra
[1] Papel
[2] Tesoura''')
jokempo = ('pedra','papel','tesoura')
computador = randint(0,2)
jogada = int(input('Escolha sua jogada:' ))
print('JO ...')
sleep(1.5)
print('KEN...')
sleep(1.2)
print('POO...')
print('O computador escolheu : {}'.format(jokempo[computador]))
print('>' *20)
print('Voce escolheu {}'.format(jokempo[jogada]))
if computador ==0:
    if jogada ==0:
        print('o resultado é EMPATE')
    elif jogada ==1:
        print('O jogador VENCEU')

    elif jogada ==2:
        print('O jogador PERDEU')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 1:
    if jogada ==1:
        print('O resultado é empate')
    elif computador ==1:
     if jogada ==2:
         print('O jogador VENCEU')
    elif computador ==1:
        print('O jogador VENCEU')
    else:
        print('jogada inválida')
elif computador ==2:
    if jogada ==0:
        print('O jogador venceu')
    elif jogada ==1:
        print('O computador venceu')
    elif jogada ==2:
        print('o resultado é EMPATE')
print('Fim da partida')
