import pygame
from sys import exit 
 
pygame.init()

screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption("Dumbal")
clock = pygame.time.Clock()

floor = pygame.image.load("./images/board.jpg")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #exits the game
            exit() #exits the python program completely

    screen.blit(floor,(0,0))

    pygame.display.update() #updates the screen after every move
    clock.tick(60)