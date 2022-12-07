'''
    sprite to log the progress and render it on the surface
'''
import pygame
from JosephusGUI.constants import SCREEN_SIZE


class Logging(pygame.sprite.Sprite):
    def __init__(self, num='', status=''):
        super().__init__()
        self.num = num
        self.status = status
        self.base_font_smaller = pygame.font.Font(
                'assets/fonts/JetBrainsMono-ExtraBold.ttf', 20)
        self.image = self.base_font_smaller.render(
                f"{num} {status}", True, 'Black')
        self.rect = self.image.get_rect(
                center=(SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2))

    def update_text(self, num, status):
        self.num = num
        self.status = status
        self.image = self.base_font_smaller.render(
                f"{num} {status}", True, 'Black')
        self.rect = self.image.get_rect(
                center=(SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2))
