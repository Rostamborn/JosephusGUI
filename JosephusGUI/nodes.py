'''
    sprite for the regular nodes
'''
import pygame
from JosephusGUI.constants import CIRCLE_SIZE


class Nodes(pygame.sprite.Sprite):
    def __init__(self, pos, circle_size=CIRCLE_SIZE):
        super().__init__()

        self.pos = pos
        node_surface_green = pygame.image.load(
                'assets/green_circle.png').convert_alpha()
        self.node_green = pygame.transform.scale(
                node_surface_green, circle_size)
        node_surface_red = pygame.image.load(
                'assets/red_circle.png').convert_alpha()
        self.node_red = pygame.transform.scale(node_surface_red, circle_size)

        self.image = self.node_green
        self.rect = self.image.get_rect(center=self.pos)

    # changes the image on death
    def kill_node(self):
        self.image = self.node_red

    # changes the image on revival
    def revive_node(self):
        self.image = self.node_green
