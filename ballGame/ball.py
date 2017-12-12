'''
pygame模块测试

pygame的最基本开发框架
小球碰撞实验
'''

import pygame
import sys


pygame.init()

display_width = 800
display_height = 600
speed = [1, 1]
fps = 120
white = (255, 255, 255)
screen = pygame.display.set_mode(
    (display_width, display_height), pygame.RESIZABLE)

# 设置标题和图标
icon = pygame.image.load('static/img/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Python 游戏 --- 壁球小程序')

# pygame 操作时间的对象
clock = pygame.time.Clock()

ball = pygame.image.load('static/img/ball.png')
# 将图片对象替换成正切矩形对象
ballrect = ball.get_rect()

crashed = False


def speed_down(speed):
    if speed > 0:
        new_speed = speed - 1
    else:
        new_speed = speed + 1
    print('new speed is {}'.format(new_speed))
    return new_speed


def speed_up(speed):
    if speed > 0:
        new_speed = speed + 1
    else:
        new_speed = speed - 1
    print('new speed is {}'.format(new_speed))
    return new_speed



# pygame的主寻坏
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        elif event.type == pygame.KEYDOWN:
            # 小球速度控制备部分
            if event.key == pygame.K_LEFT:
                speed[0] = speed_down(speed[0])
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed_up(speed[0])
            elif event.key == pygame.K_UP:
                speed[1] = speed_up(speed[1])
            elif event.key == pygame.K_DOWN:
                speed[1] = speed_down(speed[1])
            # esc键退出功能
            elif event.key == pygame.K_ESCAPE:
                crashed = True
        # 增加屏幕尺寸的动态感应
        elif event.type == pygame.VIDEORESIZE:
            display_width = event.size[0]
            display_height = event.size[1]
            screen = pygame.display.set_mode(
                (display_width, display_height), pygame.RESIZABLE)

    # 增加窗口最小话感知暂停
    if pygame.display.get_active():
        # 将矩形移动
        ballrect = ballrect.move(speed[0], speed[1])
    # 碰撞处理
    if ballrect.left < 0 or ballrect.right > display_width:
        speed[0] = -speed[0]
        if ballrect.right > display_width and ballrect.right + speed[0] > ballrect.right:
            speed[0] = - speed[0]
    if ballrect.top < 0 or ballrect.bottom > display_height:
        speed[1] = -speed[1]
        if ballrect.bottom > display_height and ballrect.bottom + speed[1] > ballrect.bottom:
            speed[1] = - speed[1]
    # 填充背景图像
    screen.fill(white)
    # 将一个图像绘制到另外一个图像上
    # 这里将小球的图像跟随了小球的正切矩形上
    screen.blit(ball, ballrect)
    pygame.display.update()
    # 通过时间间隔来控制刷新
    clock.tick(fps)
