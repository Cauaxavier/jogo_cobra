import pygame
from sys import exit
from random import randrange

velocidade = 15

janela_x = 720
janela_y = 480

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
roxo = pygame.Color(128, 50, 255)
preto = pygame.Color(0, 0, 0)
vermelho = pygame.Color(255, 0, 0)
verde = pygame.Color(0, 255, 0)
amarelo = pygame.Color(255, 195, 27)

controlador_fps = pygame.time.Clock()
tamanho_cobra = 30 # tamanho do bloco

#iniciando as variaveis principais do jogo
def init_vars():
    global pos_cabeca, corpo_cobra, pos_comida, gerar_comida, pontos, direcao
    direcao = 'RIGHT'
    pos_cabeca = [120, 60]
    corpo_cobra = [[120, 60]]
    pos_comida = [randrange(1, (janela_x // tamanho_cobra)) * tamanho_cobra,
                  randrange(1, (janela_y // tamanho_cobra)) * tamanho_cobra]
    gerar_comida = True
    pontos = 0

init_vars()    

def pontuacao(escolha, cor, fonte, tamanho):
    pontuacao_fonte = pygame.font.SysFont(fonte, tamanho)
    pontuacao_tela = pontuacao_fonte.render('Pontuação: ' + str(pontos), True, cor)
    pontuacao_certa = pontuacao_tela.get_rect()

    if escolha == 1:
        pontuacao_certa.midtop = (janela_x / 10, 15)
    else:
        pontuacao_certa.midtop = (janela_x / 2, janela_y / 1.25)

    janela_jogo.blit(pontuacao_tela, pontuacao_certa)

#loop do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
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
    elif pos_cabeca[1] > janela_y - tamanho_cobra:
        pos_cabeca[1] = 0

    #comendo a maçã
    corpo_cobra.insert(0, list(pos_cabeca))
    if pos_cabeca[0] == pos_comida[0] and pos_cabeca[1] == pos_comida[1]:
        pontos += 1
        gerar_comida = False
    else:
        corpo_cobra.pop()

    #gerando a comida    
    if not gerar_comida:
        pos_comida = [randrange(1, (janela_x // tamanho_cobra)) * tamanho_cobra,
                      randrange(1, (janela_y // tamanho_cobra)) * tamanho_cobra]
        gerar_comida = True 

    #Gráficos
    janela_jogo.fill(preto)
    for pos in corpo_cobra:
        pygame.draw.rect(janela_jogo, verde, pygame.Rect(
            pos[0] + 2, pos[1] + 2, tamanho_cobra - 2, tamanho_cobra - 2))

    pygame.draw.rect(janela_jogo, vermelho, pygame.Rect(
        pos_comida[0], pos_comida[1], tamanho_cobra, tamanho_cobra))    

    #condições de fim de jogo
    for bloco in corpo_cobra[1:]:
        if pos_cabeca[0]  == bloco[0] and pos_cabeca[1] == bloco[1]:
            init_vars()  

    pontuacao(1, branco, 'consolas', 20)
    pygame.display.update()       
    controlador_fps.tick(velocidade) 