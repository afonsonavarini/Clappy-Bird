import pygame, random, time, sys
from pygame.locals import *
from pygame import font

def text_objects(text, font): # Importa uma configuração de texto
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text): # Faz aparecer o texto
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((largura_tela/2, altura_tela/2))
    tela.blit(TextSurf, TextRect)
    pygame.display.update()

def gameOver(contador):
    background = pygame.image.load("assets/background_gameover.png").convert_alpha()
    tela = pygame.display.set_mode((400, 800))
    tela.fill((0, 0, 255))
    gameover = "Você Perdeu! Pontos: "
    pygame.font.init()
    font = pygame.font.get_default_font()  
    fontsys = pygame.font.SysFont(font, 40)
    textGameOver = fontsys.render("Você Perdeu! Pontos: " +str(contador), 1, (255, 255, 255))
    tela.blit(background, (0, 0))
    tela.blit(textGameOver, (50, 400))
    pygame.display.update()
    time.sleep(2)

def font():
    base_font = pygame.font.Font(None, 32)
    user_text = ""
    text_surface = base_font.render(user_text, True, (255, 255, 255))

def email():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode([400, 800])
    base_font = pygame.font.Font(None, 32)
    user_text = ""

    input_rect = pygame.Rect(20,400,140,32)
    color_active = pygame.Color("lightskyblue3")
    color_passive = pygame.Color("gray15")
    color = color_passive

    active = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
        screen.fill((0,0,0))

        if active:
            color = color_active
        else:
            color = color_passive

        pygame.draw.rect(screen,color,input_rect,2)

        text_surface = base_font.render(user_text, True, (255, 255, 255))
        screen.blit(text_surface,(input_rect.x + 5, input_rect.y +5))

        input_rect.w = max(50,text_surface.get_width() + 10)

        pygame.display.flip()
        pygame.display.update()

    textGameOver = fontsys.render("Email:", 1, (255, 255, 255))
    pygame.display.update()