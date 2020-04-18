import sys, pygame

if __name__ == "__main__":
    # Basic initialization.
    pygame.init()

    running = True
    FPS = 30
    FPSClock = pygame.time.Clock()

    width = 640
    height = 480
    dimensions = (width, height)

    viewport = pygame.display.set_mode(dimensions)
    black = 0, 0, 0

    # Groups for the sprites to fall into for mass updating.
    G_Background = pygame.sprite.Group()
    G_All = pygame.sprite.Group()
    G_Player = pygame.sprite.Group()
    G_Enemies = pygame.sprite.Group()
    G_Neutral = pygame.sprite.Group()
    # add more groups here as needed.

    # Be very careful when adding things into this loop! This is the main run loop (limited by FPS).
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

        viewport.fill(black)

        pygame.display.flip()
        FPSClock.tick(FPS)
