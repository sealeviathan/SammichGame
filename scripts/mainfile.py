import sys, pygame, ingredient

if __name__ == "__main__":
    # Basic initialization.
    pygame.init()

    running = True
    FPS = 30
    FPSClock = pygame.time.Clock()

    width = 960
    height = 540
    dimensions = (width, height)

    viewport = pygame.display.set_mode(dimensions)
    black = (0, 0, 0)

    # Groups for the sprites to fall into for mass updating.
    G_All = pygame.sprite.Group()
    G_Clicked = pygame.sprite.Group()
    G_Background = pygame.sprite.Group()
    G_Player = pygame.sprite.Group()
    G_Enemies = pygame.sprite.Group()
    G_Neutral = pygame.sprite.Group()
    # add more groups here as needed.

    # Load resources
    try:
        breadresouce = pygame.image.load("../Images/bread.png")
    except Exception as error:
        print(error)
        pygame.quit()
        sys.exit()

    BreadTest = ingredient.Ingredient(breadresouce, G_All)
    BreadTest2 = ingredient.Ingredient(breadresouce, G_All)

    # Be very careful when adding things into this loop! This is the main run loop (limited by FPS).
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                collisions = [s for s in G_All if s.rect.collidepoint(event.pos)]
                if not collisions == []:
                    collisions[0].handleclick()


        viewport.fill(black)
        G_All.draw(viewport)
        pygame.display.flip()
        FPSClock.tick(FPS)
