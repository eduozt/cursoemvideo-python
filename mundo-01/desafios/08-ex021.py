import pygame
pygame.init()
pygame.mixer.music.load('hino-do-flamengo.mp3')
pygame.mixer.music.play()
input("Pressione Enter para sair...")

"""while pygame.mixer.music.get_busy():
    pass"""