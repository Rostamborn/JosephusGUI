'''
    sprite for numbers on the nodes
'''
import pygame


class Number(pygame.sprite.Sprite):
    def __init__(self, pos, size, num):
        super().__init__()

        self.pos = pos
        self.size = size
        base_font = pygame.font.Font(
            'assets/fonts/JetBrainsMono-ExtraBold.ttf', size)
        self.image = base_font.render(
                f"{num}", True, 'Black')
        self.rect = self.image.get_rect(center=pos)
