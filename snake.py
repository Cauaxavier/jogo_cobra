import pygame
import sys
import time
import random

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
janela_jogo = pygame.display.set_mode(janela_x, janela_y)

#cores 
branco = pygame.Color(255, 255, 255)
roxo = pygame.Color(39, 10, 137)
preto = pygame.Color(0, 0, 0)
verde = pygame.Color(14, 90, 50)
amarelo = pygame.Color(237, 185, 46)

controlador_fps = pygame.time.Clock()
tamanho_cobra = 21 # tamanho inicial da cobra

#iniciando as variaveis principais do jogo
def init_vars():
    global pos_corpo, corpo_cobra, pos_comida, gerar_comida, pontos, direcao
    direcao = 'RIGHT'
    pos_corpo = [120, 60]
    corpo_cobra = [[120, 60]]
    pos_comida = [random.randrange(1, (janela_x // tamanho_cobra)) * tamanho_cobra,
                  random.randrange(1, (janela_y // tamanho_cobra)) * tamanho_cobra]
    gerar_comida = True
    pontos = 0

init_vars()    
