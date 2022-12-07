'''
    text box sprite in order to handle user input
'''
import pygame
from JosephusGUI.constants import SCREEN_SIZE


class TextBox(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.base_font = pygame.font.Font(
                'assets/fonts/JetBrainsMono-ExtraBold.ttf', 32)
        self.input_text = ''
        self.image = self.base_font.render(self.input_text, True, (0, 0, 0))
        self.rect = self.image.get_rect(
                center=(SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2))

    def update_text(self, text) -> None:
        self.input_text = text
        self.image = self.base_font.render(self.input_text, True, (0, 0, 0))
        self.rect = self.image.get_rect(
                center=(SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2))

    def get_number(self) -> int:
        if self.input_text == '':
            return 1
        else:
            return int(self.input_text)
