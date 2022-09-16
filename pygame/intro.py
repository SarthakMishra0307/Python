import pygame as p

p.init()

screen = p.display.set_mode([500,500])

running = True
while running:

    
    screen.fill((21,9,7))

    p.draw.circle(screen,(0,0,255),(250,250),75)

    p.display.flip()

p.quit()