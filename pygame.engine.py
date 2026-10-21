import random
import sys

import pygame

pygame.init()

W, H = 1300, 700
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Gravity Game")
clock = pygame.time.Clock()
running = True


GRAVITY = 1
JUMP_HEIGHT = -20
Y_VELOCITY = 0
is_grouding = True

standing_surface = pygame.image.load("Mario.png").convert_alpha()
standing_surface = pygame.transform.scale(standing_surface, (50, 66))

mario_left = pygame.transform.flip(standing_surface, True, False)

mario_rect = standing_surface.get_rect(center=(130, 50))    

stars = []
for i in range(50):
    pos_x = random.randint(0, W)
    pos_y = random.randint(0, H)
    stars.append({"posx": pos_x, "posy": pos_y})
    
meterors = [
    (130, 440, 55, (20, 20, 20)),   (310, 400, 65, (30, 30, 30)),
    (470, 460, 80, (20, 20, 20)),   (660, 400, 55, (30, 30, 30)),
    (830, 480, 55, (8, 8, 8)),  (990, 390, 80, (10, 10, 10))
]

flipped = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((10, 0, 30  ))
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        mario_rect.x -= 7
        flipped = False
    if keys[pygame.K_d]:
        mario_rect.x += 7
        flipped = True
    if keys[pygame.K_SPACE] and is_grouding:
        Y_VELOCITY = JUMP_HEIGHT
        is_grouding = False
        
    Y_VELOCITY += GRAVITY
    mario_rect.y += Y_VELOCITY
    is_grouding + False
    
    for x, y, rad, col in meterors:
        
        plat_rect = pygame.Rect(x - rad, y - rad, rad * 2, 20)
        
        if mario_rect.colliderect(plat_rect) and Y_VELOCITY > 0:  # noqa: SIM102
            if mario_rect.bottom <= plat_rect.bottom + 10:
                mario_rect.bottom = plat_rect.top
                Y_VELOCITY = 0
                is_grouding = True
    
    if mario_rect.y > H:
        mario_rect.x, mario_rect.y, Y_VELOCITY = 130, 50, 0
            
    for star in stars:
        pygame.draw.circle(screen, (255, 255, 255), (star["posx"], star["posy"]), 2)    
        
    for x, y, rad, col in meterors:
        pygame.draw.circle(screen, col, (x, y), rad)
    
    if flipped:
        screen.blit(standing_surface, mario_rect)
    else:
        screen.blit(mario_left, mario_rect)
     
    pygame.display.update()
            
    clock.tick(60)
  
pygame.quit()
sys.exit()