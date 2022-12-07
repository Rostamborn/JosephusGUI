import pygame
from sys import exit
from JosephusGUI.constants import SCREEN_SIZE, FPS
from JosephusGUI.text_box import TextBox
from JosephusGUI.controller import ProgramController


def main_loop() -> None:
    # this variable is used to handle the user input
    # with basic python string manipulation operations
    # and then sent to the text_box object instance to be rendered
    user_text = ''
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if controller.get_state() == 'menu':
                    # if backspace is pressed, then a character gets deleted
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        # we only allow integers as input,
                        # so we check whether the input given is an integer
                        # and then add it to the user_text
                        if event.unicode in nums:
                            user_text += event.unicode
                    # we send the text entered, to the object instance
                    text_box.update_text(user_text)

                if controller.get_state() == 'game':
                    user_text = ''
                    # going forward or backward using 'n' and 'b'
                    if event.key == pygame.K_n:
                        controller.eliminate()
                    elif event.key == pygame.K_b:
                        controller.revive()

        controller.run()
        # controlling the number of frames per second
        clock.tick(FPS)
        pygame.display.update()


if __name__ == '__main__':
    # initializing the preleminaries

    # this will be used to control the user input and limit it to integers only
    nums = '1234567890'

    pygame.init()
    # initializing the main surface
    screen = pygame.display.set_mode(SCREEN_SIZE)
    text_box = TextBox()
    controller = ProgramController(screen, text_box)
    pygame.display.set_caption('Josephus GUI')
    clock = pygame.time.Clock()

    main_loop()
