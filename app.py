import pygame
import time
import random

# Inicialização
pygame.init()
largura = 600
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Game')

# Cores
branco = (255, 255, 255)
amarelo = (255, 255, 102)
preto = (0, 0, 0)
vermelho = (213, 50, 80)
verde = (0, 255, 0)

# Configurações do jogo
tamanho_bloco = 10
velocidade = 15
clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 25)

def mostrar_pontuacao(pontos):
    value = font_style.render("Pontos: " + str(pontos), True, amarelo)
    tela.blit(value, [0, 0])

def desenhar_cobra(tamanho_bloco, lista_cobra):
    for x in lista_cobra:
        pygame.draw.rect(tela, verde, [x[0], x[1], tamanho_bloco, tamanho_bloco])

def jogo():
    game_over = False
    game_close = False
    
    # Posição inicial
    x1 = largura / 2
    y1 = altura / 2
    
    x1_mudanca = 0
    y1_mudanca = 0
    
    lista_cobra = []
    comprimento_cobra = 1
    
    # Posição da comida
    comidax = round(random.randrange(0, largura - tamanho_bloco) / 10.0) * 10.0
    comiday = round(random.randrange(0, altura - tamanho_bloco) / 10.0) * 10.0

    while not game_over:
        
        while game_close == True:
            tela.fill(preto)
            msg = font_style.render("Perdeu! Pressione Q-Sair ou C-Jogar", True, vermelho)
            tela.blit(msg, [largura / 6, altura / 3])
            mostrar_pontuacao(comprimento_cobra - 1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        jogo() # Reinicia o jogo
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        # Controles
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_mudanca == 0:
                    x1_mudanca = -tamanho_bloco
                    y1_mudanca = 0
                elif event.key == pygame.K_RIGHT and x1_mudanca == 0:
                    x1_mudanca = tamanho_bloco
                    y1_mudanca = 0
                elif event.key == pygame.K_UP and y1_mudanca == 0:
                    y1_mudanca = -tamanho_bloco
                    x1_mudanca = 0
                elif event.key == pygame.K_DOWN and y1_mudanca == 0:
                    y1_mudanca = tamanho_bloco
                    x1_mudanca = 0

        # Verificação de colisão com as paredes
        if x1 >= largura or x1 < 0 or y1 >= altura or y1 < 0:
            game_close = True
        
        x1 += x1_mudanca
        y1 += y1_mudanca
        tela.fill(preto)
        
        # Desenha a comida
        pygame.draw.rect(tela, vermelho, [comidax, comiday, tamanho_bloco, tamanho_bloco])
        
        # Lógica da cobra
        cabeca_cobra = []
        cabeca_cobra.append(x1)
        cabeca_cobra.append(y1)
        lista_cobra.append(cabeca_cobra)
        
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]
            
        # Verifica se a cobra bateu nela mesma
        for x in lista_cobra[:-1]:
            if x == cabeca_cobra:
                game_close = True
                
        desenhar_cobra(tamanho_bloco, lista_cobra)
        mostrar_pontuacao(comprimento_cobra - 1)
        
        pygame.display.update()

        # Verifica se a cobra comeu a comida
        if x1 == comidax and y1 == comiday:
            comidax = round(random.randrange(0, largura - tamanho_bloco) / 10.0) * 10.0
            comiday = round(random.randrange(0, altura - tamanho_bloco) / 10.0) * 10.0
            comprimento_cobra += 1
            
        clock.tick(velocidade)

    pygame.quit()
    quit()

# Inicia o jogo
jogo()
