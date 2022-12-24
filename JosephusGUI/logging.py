'''
    sprite to log the progress and render it on the surface
'''
import pygame
from JosephusGUI.constants import SCREEN_SIZE


class Logging(pygame.sprite.Sprite):
    def __init__(self, num1='', num2=''):
        super().__init__()
        self.num1 = num1
        self.base_font_smaller = pygame.font.Font(
                'assets/fonts/JetBrainsMono-ExtraBold.ttf', 20)
        self.image = self.base_font_smaller.render(
                f"{num1} {num2}", True, 'Black')
        self.rect = self.image.get_rect(
                center=(SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2))

    def update_elimination(self, num1, num2, status):
        self.num1 = num1
        self.num2 = num2
        self.image = self.base_font_smaller.render(
                f"{num1} {status} {num2}", True, 'Black')
        self.rect = self.image.get_rect(
                center=(SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2))

    def update_revival(self, num1, status):
        self.num1 = num1
        self.image = self.base_font_smaller.render(
                f"{num1} {status}", True, 'Black')
        self.rect = self.image.get_rect(
                center=(SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2))
