import pygame, sys, time, random

velocidade = 15

janela_x = 750
janela_y = 500

existe_erro = pygame.init()

if (existe_erro[1] > 0):
    print('erro ' + existe_erro[1])
else:
    print('Jogo iniciado sem erros.')

#Criando a janela do jogo
pygame.display.set_caption('Snake Game')
janela_jogo = pygame.display.set_mode((janela_x, janela_y))

#cores 
branco = pygame.Color(255, 255, 255)
roxo = pygame.Color(86, 52, 255)
preto = pygame.Color(0, 0, 0)
verde = pygame.Color(14, 90, 50)
amarelo = pygame.Color(255, 195, 27)

controlador_fps = pygame.time.Clock()
tamanho_cobra = 21 # tamanho inicial da cobra

#iniciando as variaveis principais do jogo
def init_vars():
    global pos_cabeca, corpo_cobra, pos_comida, gerar_comida, pontos, direcao
    direcao = 'RIGHT'
    pos_cabeca = [120, 60]
    corpo_cobra = [[120, 60]]
    pos_comida = [random.randrange(1, (janela_x // tamanho_cobra)) * tamanho_cobra,
                  random.randrange(1, (janela_y // tamanho_cobra)) * tamanho_cobra]
    gerar_comida = True
    pontos = 0

init_vars()    

def pontuacao():
    print('Pontuacao')


#loop do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if (evento.key == pygame.K_UP or evento.key == ord('w') and direcao != 'DOWN'):
                direcao = 'UP'
            elif (evento.key == pygame.K_DOWN or evento.key == ord('s') and direcao != 'UP'):
                direcao = 'DOWN'    
            elif (evento.key == pygame.K_RIGHT or evento.key == ord('d') and direcao != 'LEFT'):
                direcao = 'RIGHT'
            elif (evento.key == pygame.K_LEFT or evento.key == ord('a') and direcao != 'RIGHT'):
                direcao = 'LEFT'

    if direcao == 'UP':
        pos_cabeca[1] -= tamanho_cobra
    elif direcao == 'DOWN':
        pos_cabeca[1] += tamanho_cobra
    elif direcao == 'LEFT':
        pos_cabeca[0] -= tamanho_cobra
    else:
        pos_cabeca[0] += tamanho_cobra 

    if pos_cabeca[0] < 0:
        pos_cabeca[0] = janela_x - tamanho_cobra       
    elif pos_cabeca[0] > janela_x - tamanho_cobra:
        pos_cabeca[0] = 0
    elif pos_cabeca[1] < 0:
        pos_cabeca[1] = janela_y - tamanho_cobra
    elif pos_cabeca[1] < janela_y - tamanho_cobra:
        pos_cabeca[1] = 0

pygame.display.update()        