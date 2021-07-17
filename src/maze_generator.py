import pickle  # nosec

import pygame

import config

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
    selected_tool = add_obstacle
    while True:
        square_pos_list = []
        canvas.fill((40, 40, 40))
        draw()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print("add selected")
                    selected_tool = add_obstacle
                if event.key == pygame.K_d:
                    print("delete selected")
                    selected_tool = remove
                if event.key == pygame.K_e:
                    print("enemy selected")
                    selected_tool = add_enemy
                if event.key == pygame.K_s:
                    print("saving")
                    with open(config.general_settings.new_maze_path(), "wb") as f:
                        pickle.dump(grid, f)
                    f.close()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                while selected:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        x_pos, y_pos = pygame.mouse.get_pos()
                        if selected_tool == add_obstacle:
                            pygame.draw.rect(
                                canvas, (200, 200, 200),
                                ((x_pos//s_s)*s_s, (y_pos//s_s)*s_s, s_s, s_s))
                        if selected_tool == remove:
                            pygame.draw.rect(
                                canvas, (0, 0, 0),
                                ((x_pos//s_s)*s_s, (y_pos//s_s)*s_s, s_s, s_s))
                        if selected_tool == add_enemy:
                            pygame.draw.rect(
                                canvas, (200, 50, 50),
                                ((x_pos//s_s)*s_s, (y_pos//s_s)*s_s, s_s, s_s))

                        pygame.display.update()
                        pos = (y_pos//s_s, x_pos//s_s)
                        if pos not in square_pos_list:
                            square_pos_list.append(pos)

                        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                            for sqr in square_pos_list:
                                selected_tool(sqr)
                            selected = False

        if pygame.mouse.get_pressed()[2]:
            break
        selected = True


def add_obstacle(pos):
    grid[pos[0]][pos[1]].passable = False


def remove(pos):
    grid[pos[0]][pos[1]].passable = True
    grid[pos[0]][pos[1]].enemy = False


def add_enemy(pos):
    grid[pos[0]][pos[1]].enemy = True


def draw():
    x, y = 0, 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col].enemy and not grid[row][col].passable:
                pygame.draw.rect(canvas, (100, 70, 70), (x, y, s_s, s_s), 1)
            elif grid[row][col].enemy and grid[row][col].passable:
                pygame.draw.rect(canvas, (200, 50, 50), (x, y, s_s, s_s), 1)
            elif grid[row][col].passable:
                pygame.draw.rect(canvas, (10, 10, 10), (x, y, s_s, s_s), 1)
            else:
                pygame.draw.rect(canvas, (200, 200, 200), (x, y, s_s, s_s), 1)
            x += s_s
        y += s_s
        x = 0


# a: add
# d: delete
# e: enemy
# s: saving

select_square()
