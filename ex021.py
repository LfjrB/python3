'''import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''


'''from pygame import *

mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()

while mixer.music.get_busy():
    time.Clock().tick(10)'''

'''import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()'''

import playsound
playsound.playsound('C:/Users/x/Downloads/soundofsilence.mp3', True)


