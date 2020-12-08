from random import randint

pc = randint(0, 10)

print('Tente me ganhar... Acabei de pensar em um número de 0 a 10!\n')
print('Será que você consegue me ganhar?\n')

chutes = 0

while True:
    player = int(input('Qual seu palpite? '))
    chutes += 1
    if player == pc:
        print("Parabéns, você me venceu!")
        break
    if player < pc:
            print('\nTente um número maior, te restam {} tentativas!\n'.format(4 - chutes))
    if player > pc:
            print('\nTente um número menor, te restam {} tentativas!\n'.format(4 - chutes))
    if chutes == 4:
            print(f"Você perdeu, eu estava pensando no número {pc}!")
            break
       

        

