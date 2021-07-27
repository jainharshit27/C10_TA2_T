import pygame, pymunk
import pymunk.pygame_util

pygame.init()

height = 600
width = 690
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#pymunk space
gravity = 1000 # for SA make this 0, for AA2 make it 1000
wind = 0 # for SA change this to value between 100-1000, for AA2 keep the value of SA
space = pymunk.Space()
space.gravity = wind, gravity
draw_options = pymunk.pygame_util.DrawOptions(screen)

body = pymunk.Body(1,100)
shape = pymunk.Circle(body, 25)
body.position = 200, 100
space.add(body, shape)

while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    space.debug_draw(draw_options)
    pygame.display.update()
    
    #space reload
    space.step(1/60)
    clock.tick(60)