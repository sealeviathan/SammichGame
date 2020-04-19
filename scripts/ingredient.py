import pygame


class Ingredient(pygame.sprite.Sprite):

    def __init__(self, image_resource):
        super().__init__()
        self.image = image_resource
        self.rect = self.image.get_rect()
        self.width, self.height = self.rect.get_size()
        