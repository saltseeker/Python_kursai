import pygame
from sys import exit




pygame.init()
screen = pygame.display.set_mode((800,400))                     #Screen size
pygame.display.set_caption('Runner')                            #Game tittle
clock = pygame.time.Clock()   
test_font = pygame.font.Font('game/font/Pixeltype.ttf', 50)                                  #Game Font - font type, font size

sky_surface = pygame.image.load('game/graphics/sky.png').convert_alpha()                       #background top image   
ground_surface = pygame.image.load('game/graphics/ground.png').convert_alpha()                      #background bottom image 
text_surface = test_font.render('My Game', False, 'Black')                              #text background - text, anti aliansing(smooth the edges, True or False), color.


snail_surface = pygame.image.load('game/snail/snail1.png').convert_alpha()               #  .convert_alpha() for python that could work with images easer
snail_rect = snail_surface.get_rect(midbottom = (80, 300)) 

player_surface = pygame.image.load('game/player/player_walk_1.png').convert_alpha()
# It's creating a rectangle object that is the same size as the player image. The `midbottom` argument
# is setting the bottom middle of the rectangle to the coordinates (80, 300).
player_rect = player_surface.get_rect(midbottom = (80,300))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))                              #background top image and position y,x
    screen.blit(ground_surface,(0,300))                         #background bottom image and position y,x
    screen.blit(text_surface,(330,50))
    
    screen.blit(snail_surface, snail_rect)
    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(player_surface, player_rect)
    
    if player_rect.colliderect(snail_rect):
        break                                         
    
    pygame.display.update()                                     # display on display screen
    clock.tick(60)                                              #while True -  fix game at 60FPS.