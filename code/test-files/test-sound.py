import pygame

pygame.init()

mixer = pygame.mixer.init()

sound = pygame.mixer.Sound('/home/mateoarbildo/Downloads/music_fx_lofi.mp3')

sound.play()

pygame.event.wait()
