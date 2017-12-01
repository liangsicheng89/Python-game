'''
pygame模块测试

pygame的最基本开发框架
小球碰撞实验
'''

import pygame
import sys

pygame.init()

display_width = 600
display_height = 400

speed = [1, 1]
fps = 60
white = (255, 255, 255)
screen = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Python 游戏开发')

# pygame 操作时间的对象
clock = pygame.time.Clock()

ball = pygame.image.load('car.png')
# 将图片对象替换成正切矩形对象
ballrect = ball.get_rect()


crashed = False
# pygame的主寻坏
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0]) - 1)*int(speed[0]/abs(speed[0]))
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1]) - 1)*int(speed[1]/abs(speed[1]))
    # 将矩形移动
    ballrect = ballrect.move(speed[0], speed[1])
    # 碰撞处理
    if ballrect.left < 0 or ballrect.right > display_width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > display_height:
        speed[1] = -speed[1]
    # 填充背景图像
    screen.fill(white)
    # 将一个图像绘制到另外一个图像上
    # 这里将小球的图像跟随了小球的正切矩形上
    screen.blit(ball, ballrect)
    pygame.display.update()
    # 通过时间间隔来控制刷新
    clock.tick(fps)
