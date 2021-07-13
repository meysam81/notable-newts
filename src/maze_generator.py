import pygame

pygame.init()


class Tile:
    """The tiles that levels are based on"""

    def __init__(self, passable: bool = True, enemy: bool = False):
        # we could have different terrains like water to spice up the level design
        self.passable = passable
        self.enemy = enemy


canvas = pygame.display.set_mode((540, 540))
s_s = 60


grid = [[Tile() for i in range(9)] for j in range(9)]


def select_square():
    selected = True
    square_pos_list = []
    while selected:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                while selected:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        x_pos, y_pos = pygame.mouse.get_pos()
                        pygame.draw.rect(
                            canvas, (255, 0, 0),
                            ((x_pos//s_s)*s_s, (y_pos//s_s)*s_s, s_s, s_s))
                        pygame.display.update()
                        pos = (y_pos//s_s, x_pos//s_s)
                        if pos not in square_pos_list:
                            square_pos_list.append(pos)

                        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                            selected = False
    return square_pos_list


def add_obstacle(pos):
    grid[pos[0]][pos[1]].passable = False


def remove_obstacle(pos):
    grid[pos[0]][pos[1]].passable = True


def add_enemy(pos):
    grid[pos[0]][pos[1]].enemy = True


def select_tool():
    selected_tool = add_obstacle
    print("\nselect tool:")
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        if pygame.key.get_pressed()[pygame.K_UP]:
            print("add selected")
            selected_tool = add_obstacle
            break
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            print("delete selected")
            selected_tool = remove_obstacle
            break
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            print("enemy selected")
            selected_tool = add_enemy
            break
    return selected_tool


def draw_stage():
    x, y = 0, 0
    for row in grid:
        for column in row:
            pygame.draw.rect(canvas, (10, 10, 10), (x, y, s_s, s_s), 1)
            x += s_s
        y += s_s
        x = 0


def draw():
    x, y = 0, 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col].enemy:
                pygame.draw.rect(canvas, (100, 10, 10), (x, y, s_s, s_s), 1)
            if grid[row][col].passable:
                pygame.draw.rect(canvas, (10, 10, 10), (x, y, s_s, s_s), 1)
            else:
                pygame.draw.rect(canvas, (200, 200, 200), (x, y, s_s, s_s), 1)
            x += s_s
        y += s_s
        x = 0


# 0: add
# 1: delete
# 2: enemy


while 1:
    canvas.fill((50, 50, 50))
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # draw_stage()
    pygame.display.update()
    # i am reusing the square selection function and
    # because it's not running in the main loop, you can't change tools real time
    selected_tool = select_tool()
    sqrs = select_square()
    for sqr in sqrs:
        selected_tool(sqr)
