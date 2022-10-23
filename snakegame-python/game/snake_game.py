import pygame
from pygame.locals import * 
from sys import exit
from random import randint

pygame.init()

#sonografia

pygame.mixer.music.set_volume(0.1)
musica_de_fundo = pygame.mixer.music.load('BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_coin.wav')
#barulho_colisao.set_volume()

largura = 640
altura = 480

x_cobra = largura//2
y_cobra = altura//2

velocidade = 5
x_controle = velocidade
y_controle = 0


x_maca = randint(40, 600)
y_maca = randint(50, 430)


fonte = pygame.font.SysFont('arial', 30, bold=True, italic=True)
pontos = 0

tela = pygame.display.set_mode((largura, altura)) #objeto recebendo l e H
pygame.display.set_caption('cobrinha')
relogio = pygame.time.Clock()
lista_cobra = []
comprimento_inicial = 5
morreu = False

def aumenta_cobra(lista_cobra):
    for xy in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 0), (xy[0], xy[1], 20,20))

def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu

    pontos = 0
    comprimento_inicial = 5

    x_cobra = largura//2
    y_cobra = altura//2

    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    morreu = False

    



#o jogo está sempre dentro de um loop infinito
while True:    
    relogio.tick(30)
    tela.fill((255,255,255))

    mensagem = f'Score: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0, 0, 255))
    
    for event in pygame.event.get(): #checa se esse evento ocorreu
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0
    
    x_cobra = x_cobra + x_controle
    y_cobra += y_controle
    #vai desenhar objetos na tela
    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra, y_cobra, 20, 20)) #onde vai ser desenhado, cor, tupla com posiçãoxy do retangulo
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca, y_maca, 20, 20))
    
    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos +=1
        barulho_colisao.play()
        comprimento_inicial +=1

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 20 , True, True)
        mensagem = 'Fim de Jogo! Pressione R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (0,0,0))
        ret_texto = texto_formatado.get_rect()

        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()

    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0 :
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0


    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]
    
    aumenta_cobra(lista_cobra)


    tela.blit(texto_formatado, (435, 30))
    pygame.display.update() 
  
