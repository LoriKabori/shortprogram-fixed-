import pygame
import random
import time

Width = 360
Height = 480
FPS = 30

upvote = (242, 85, 0)
downvote = (52, 139, 207)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("upvote color because you're epic")

clock = pygame.time.Clock

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(upvote)
    pygame.display.flip()
pygame.quit()
