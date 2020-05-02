import pygame


class Ingredient(pygame.sprite.Sprite):

    def __init__(self, Id, groups):
        super().__init__()
        # Load resources
        resource = None
        try:
            resource = pygame.image.load("../Images/bread.png")
        except Exception as error:
            print(error)
            pygame.quit()

        self.Id = Id
        self.image = resource
        self.rect = self.image.get_rect()
        self.width, self.height = self.image.get_size()
        self.add(g for g in groups)
        self.dragable = True

    def __str__(self):
        return f'Ingredient, id: {self.Id}'

    def handleclick(self, event):
        print(f"Clicked {self.Id}")

    def isDragable(self):
        return self.dragable

    def handleDrag(self, event):
        self.rect.x += event.rel[0]
        self.rect.y += event.rel[1]
