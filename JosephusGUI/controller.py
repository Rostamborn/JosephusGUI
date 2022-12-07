'''
    controls the program flow
'''
import pygame
from JosephusGUI.constants import SCREEN_SIZE, CIRCLE_SIZE
from JosephusGUI.nodes import Nodes
from JosephusGUI.utils import coordinations, josephus_solver
from JosephusGUI.logging import Logging


class ProgramController():
    def __init__(self, screen, text_box) -> None:
        # the main surface in which everything is rendered on
        self.screen = screen

        # decides which main surface should be shown
        self.state = 'menu'

        # the input number given by the user(default should be one)
        self.node_number = 1
        game_background_pic = pygame.image.load(
                'assets/game_background.jpg')
        self.game_background = pygame.transform.scale(
                game_background_pic, SCREEN_SIZE
                )
        menu_background_pic = pygame.image.load('assets/menu_background.jpg')
        self.menu_background = pygame.transform.scale(
                menu_background_pic, SCREEN_SIZE
                )
        gameover_background_pic = pygame.image.load(
                'assets/gameover_background.jpg')
        self.gameover_background = pygame.transform.scale(
                gameover_background_pic, SCREEN_SIZE
                )
        self.base_font = pygame.font.Font(
                'assets/fonts/JetBrainsMono-ExtraBold.ttf', 32)

        # all of the sprite groups ready to be rendered
        self.text_input = pygame.sprite.GroupSingle()
        self.text_input.add(text_box)
        self.log = pygame.sprite.GroupSingle()
        self.log.add(Logging())
        self.nodes = pygame.sprite.Group()

        # we need these to keep the track of changes and chache the process
        self.eliminated_nodes = []
        self.revert_nodes = []
        self.current_status = [1 for i in range(self.node_number)]

        # global index to know which step we're in
        self.current_index = 0

        # initializing sound using mixer
        self.step_sound = pygame.mixer.Sound('assets/step_sound.mp3')

    def set_state(self, state) -> None:
        self.state = state

    def get_state(self) -> str:
        return self.state

    def get_text_box(self):
        return self.text_input

    # cleans up all the variables used in a single run
    def clean(self):
        self.text_input.sprite.update_text('')
        self.log.sprite.update_text('', '')
        self.nodes.empty()
        self.current_status = [1 for i in range(self.node_number)]
        self.eliminated_nodes = []
        self.revert_nodes = []
        self.current_index = 0
        self.state = 'menu'

    def get_nodes(self):
        return self.nodes

    # we proceed a single step in the overall process by eliminating one node
    def eliminate(self):
        # checking whether we have more than one nodes
        if self.current_status.count(1) <= 1:
            self.state = 'gameover'
        # if we have more than one node, it means we can eliminate and
        # continue the main process
        else:
            sprites = self.nodes.sprites()
            elimination_index = self.current_index+1
            # reseting the index in case we exceed the limit
            if elimination_index >= self.node_number:
                elimination_index = 0
            # first we check whether the pivot is alive or not, then
            # we loop over the next elements to reach the first alive
            # node and eliminate
            # we also need to change the pivot to the index of the eliminated
            # node, for the process to work properly
            while True:
                if self.current_status[self.current_index] == 1:
                    if self.current_status[elimination_index] == 1:
                        self.current_status[elimination_index] = 0
                        # rendering a text which will tell the user
                        # which element has been eliminated
                        self.log.sprite.update_text(
                                str(elimination_index+1), "eliminated")
                        self.eliminated_nodes.append(elimination_index)
                        self.revert_nodes.append(self.current_index)
                        sprites[elimination_index].kill_node()
                        self.current_index = elimination_index
                        self.step_sound.play()
                        break
                    elimination_index += 1
                    if elimination_index >= self.node_number:
                        elimination_index = 0
                else:
                    self.current_index += 1
                    # reseting the index in case we exceed the limit
                    if self.current_index >= self.node_number:
                        self.current_index = 0
                    elimination_index = self.current_index+1
                    if elimination_index >= self.node_number:
                        elimination_index = 0

    # we keep track of the eliminated nodes with a list which
    # is in chronological order
    def revive(self):
        if self.eliminated_nodes != []:
            sprites = self.nodes.sprites()
            index = self.eliminated_nodes.pop()
            self.log.sprite.update_text(
                    str(index+1), "revived")
            self.current_status[index] = 1
            # we change the pivot to the previous one using a list
            # that kept track of all of the pivots in the entire process
            self.current_index = self.revert_nodes.pop()
            sprites[index].revive_node()
            self.step_sound.play()

    # determining which main surface to show
    def run(self) -> None:
        if self.state == 'menu':
            self.run_menu()
        elif self.state == 'game':
            self.run_game()
        elif self.state == 'gameover':
            self.run_gameover()

    # everything that must be rendered in the menu surface
    def run_menu(self) -> None:
        keys = pygame.key.get_pressed()
        self.screen.blit(self.menu_background, (0, 0))
        message_su = self.base_font.render(
                "PLEASE ENTER A REASONABLE NUMBER", True, 'Black')
        message_rect = message_su.get_rect(
                center=(SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2 - 150))
        self.screen.blit(message_su, message_rect)
        self.text_input.draw(self.screen)
        self.text_input.update()
        # by clicking the correct button we procceed to generate the
        # required coordinates and re-initialize node sprite group
        if keys[pygame.K_RETURN]:
            self.state = 'game'
            self.node_number = self.text_input.sprite.get_number()
            print(self.node_number)
            coordinates = coordinations(self.node_number)
            self.current_status = [1 for i in range(self.node_number)]
            size = CIRCLE_SIZE[0] - (self.node_number - 5)
            if size <= 15:
                size = 15
            for i in range(self.node_number):
                self.nodes.add(Nodes(coordinates[i], (size, size)))

    # everything than needs to be rendered in the game surface
    def run_game(self) -> None:
        self.screen.blit(self.game_background, (0, 0))
        self.nodes.draw(self.screen)
        self.nodes.update()
        self.log.draw(self.screen)
        self.log.update()
        message1_su = self.base_font.render(
                "N = Forward", True, 'Black')
        message1_rect = message1_su.get_rect(topleft=(5, 0))
        self.screen.blit(message1_su, message1_rect)
        message2_su = self.base_font.render(
                "B = Backward", True, 'Black')
        message2_rect = message2_su.get_rect(topleft=(5, 30))
        self.screen.blit(message2_su, message2_rect)

    # everything that needs to be rendered in the gameover surface
    def run_gameover(self) -> None:
        keys = pygame.key.get_pressed()
        self.screen.blit(self.gameover_background, (0, 0))
        winner = josephus_solver(self.node_number)
        message_su = self.base_font.render(
                f"NUMBER {winner} WINS", True, 'Black')
        message_rect = message_su.get_rect(
                center=(SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2))
        self.screen.blit(message_su, message_rect)
        message2_su = self.base_font.render(
                "PRESS SPACE", True, 'Black')
        message2_rect = message2_su.get_rect(
                center=(SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2 + 250))
        self.screen.blit(message2_su, message2_rect)

        # if we press the correct button we basically restart the game
        # and to do that we use the clean() method which cleans up all of
        # the important variables
        if keys[pygame.K_SPACE]:
            self.clean()
