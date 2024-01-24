import pygame
import os

pygame.init()

mixer = pygame.mixer.init()

os.system('clear')

sound = pygame.mixer.Sound('music_fx_lofi.mp3')

sound.play()

pygame.event.wait()
