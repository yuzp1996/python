# -*- coding: utf-8 -*- 

import sys, pygame
from pygame.locals import *
from random import randrange

#这是Weight类 主要是pygame的使用
class Weight(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = weight_image
        self.rect = self.image.get_rect()
        self.reset()
   
    def reset(self):
        self.rect.top = -self.rect.height
        self.rect.centerx = randrange(screen_size[0])
    
    def update(self):
        self.rect.top += 2
        if self.rect.top > screen_size[1]:
            self.reset()

#初始化Weight类
pygame.init()
screen_size = 800, 600
pygame.display.set_mode(screen_size, FULLSCREEN) #覆盖整个屏幕
pygame.mouse.set_visible(0) #参数为1则出现鼠标

weight_image = pygame.image.load('weight.jpg')
weight_image = weight_image.convert()

sprites = pygame.sprite.RenderUpdates() #这是一个组，把其他的组件放入到组里
sprites.add(Weight())

screen = pygame.display.get_surface()
bg = (255, 255, 255)
screen.fill(bg)
pygame.display.flip()

def clear_callback(surf, rect):
   surf.fill(bg, rect)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
    sprites.clear(screen, clear_callback)
    sprites.update()
    updates = sprites.draw(screen)
    pygame.display.update(updates)


























