'''
pygame模块测试
'''

import pygame

pygame.init()

display_width = 800
display_height = 600

white = (255,255,255)
gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('A bit Racey')

clock  = pygame.time.Clock()

carImg = pygame.image.load('car.png')


def car(x,y):
    '''
    显示汽车的图片
    '''
    gameDisplay.blit(carImg,(x,y))

x =(display_width * 0.45)
y = (display_height * 0.8)




crashed = False

while not crashed:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)
    gameDisplay.fill(white)
    car(x,y)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()