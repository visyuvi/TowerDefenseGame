import pygame as pg


class Enemy(pg.sprite.Sprite):
    def __init__(self, pos, image):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def move(self):
        self.rect.x += 1

    def update(self):
        self.move()