import sys, pygame

if __name__ == "__main__":
    pygame.init()

    running = True
    FPS = 30
    FPSClock = pygame.time.Clock()

    test = 0

    while running:



        FPSClock.tick(FPS)
