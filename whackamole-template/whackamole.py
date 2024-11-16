import pygame
import random


def main():

    try:

        pygame.init()
        mole_image = pygame.image.load("mole.png")
        mole_pos = (0, 0)
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        while running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mole_rect = mole_image.get_rect(topleft = mole_pos)

                    if mole_rect.collidepoint(event.pos):
                        mole_pos = (random.randrange(0, 20) * 32, random.randrange(0, 16) * 32)

            screen.fill("light green")
            screen.blit(mole_image, mole_pos)

            for i in range(32, 640, 32):
                pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, 512))
            for i in range(32, 512, 32):
                pygame.draw.line(screen, (0, 0, 0), (0, i), (640, i))

            pygame.display.flip()
            clock.tick(60)



    finally:

        pygame.quit()


if __name__ == "__main__":
    main()
