import ingredient, pygame, sys

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

    cur_id = 1
    cur_drag = None

    # Groups for the sprites to fall into for mass updating.
    G_All = pygame.sprite.Group()
    G_Clickable = pygame.sprite.Group()
    G_Background = pygame.sprite.Group()
    G_Player = pygame.sprite.Group()
    G_Enemies = pygame.sprite.Group()
    G_Neutral = pygame.sprite.Group()
    # add more groups here as needed.







    # BreadTest = ingredient.Ingredient(cur_id, [G_All, G_Clickable, G_Neutral])

    #takes a tuple of (sprite obj, position)
    CreationQueue = []

    # Be very careful when adding things into this loop! This is the main run loop (limited by FPS).
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                collisions = [s for s in G_Clickable if s.rect.collidepoint(event.pos)]
                if not len(collisions) == 0:
                    collisions[0].handleclick(event)
                    if collisions[0].isDragable():
                        cur_drag = collisions[0]
            elif event.type == pygame.MOUSEMOTION:
                if cur_drag is not None:
                    cur_drag.handleDrag(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                if cur_drag is not None:
                    cur_drag = None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    CreationQueue.append([ingredient.Ingredient, (50, 50), [G_All, G_Clickable, G_Neutral]])

        #  [class type, position, *groups]
        if len(CreationQueue) > 0:
            for t in CreationQueue:
                t_obj = CreationQueue.pop()
                cur_id += 1
                print(f'Creating Object {t_obj} with id {cur_id}')

                addme = t_obj[0](cur_id, t_obj[2])
                addme.rect.move(t_obj[1])



        viewport.fill(black)
        G_All.draw(viewport)
        pygame.display.flip()
        FPSClock.tick(FPS)

def LoadScene(name, creationqueue):
    scene = open(name, "r")
    for line in scene.readlines():
        line = line.split()
        if line[0].startswith("Ingredient:"):
            creationqueue.append(ingredient.Ingredient, (0,0), [G_All, G_Clickable, G_Neutral])

def ClearScene():
    G_All.clear()

