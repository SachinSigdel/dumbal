import pygame
from sys import exit 
 
pygame.init()

screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption("Dumbal")
clock = pygame.time.Clock()

test_surface = pygame.Surface((600,300))
test_surface.fill('White')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #exits the game
            exit() #exits the python program completely

    screen.blit(test_surface,(200,100))

    pygame.display.update() #updates the screen after every move
    clock.tick(60)