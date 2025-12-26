import copy
import random
import pygame


pygame.init()


WIDTH, HEIGHT = 500, 550
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('MAGIC SORT PUZZLE!')
font = pygame.font.Font('freesansbold.ttf', 24)


fps = 60
timer = pygame.time.Clock()
color_choices = [
    'red', 'orange', 'light blue', 'dark blue', 'dark green',
    'pink', 'purple', 'dark gray', 'brown', 'light green', 'yellow', 'white'
]
tube_colors = []
initial_colors = []
new_game = True
selected = False
select_rect = None
tube_rects = []
win = False
levels = [3, 4, 5, 6, 7, 8, 9, 10]  
current_level = 0


def generate_start(tubes_number):
    tubes_colors = [[] for _ in range(tubes_number)]
    available_colors = []
    for i in range(tubes_number - 2):
        for _ in range(4):
            available_colors.append(i)
    for i in range(tubes_number - 2):
        for _ in range(4):
            color = random.choice(available_colors)
            tubes_colors[i].append(color)
            available_colors.remove(color)
    return tubes_number, tubes_colors


def draw_tubes(tubes_num, tube_cols):
    tube_boxes = []
    if tubes_num % 2 == 0:
        tubes_per_row = tubes_num // 2
        offset = False
    else:
        tubes_per_row = tubes_num // 2 + 1
        offset = True
    spacing = WIDTH / tubes_per_row

    # Top row
    for i in range(tubes_per_row):
        for j in range(len(tube_cols[i])):
            pygame.draw.rect(screen, color_choices[tube_cols[i][j]], [5 + spacing * i, 200 - 50 * j, 65, 50], 0, 3)
        box = pygame.draw.rect(screen, 'blue', [5 + spacing * i, 50, 65, 200], 5, 5)
        if select_rect == i:
            pygame.draw.rect(screen, 'green', [5 + spacing * i, 50, 65, 200], 3, 5)
        tube_boxes.append(box)

    # Bottom row
    if offset:
        for i in range(tubes_per_row - 1):
            idx = i + tubes_per_row
            for j in range(len(tube_cols[idx])):
                pygame.draw.rect(screen, color_choices[tube_cols[idx][j]], [5 + spacing * i + spacing / 2, 450 - 50 * j, 65, 50], 0, 3)
            box = pygame.draw.rect(screen, 'blue', [5 + spacing * i + spacing / 2, 300, 65, 200], 5, 5)
            if select_rect == idx:
                pygame.draw.rect(screen, 'green', [5 + spacing * i + spacing / 2, 300, 65, 200], 3, 5)
            tube_boxes.append(box)
    else:
        for i in range(tubes_per_row):
            idx = i + tubes_per_row
            if idx >= tubes_num:
                continue
            for j in range(len(tube_cols[idx])):
                pygame.draw.rect(screen, color_choices[tube_cols[idx][j]], [5 + spacing * i, 450 - 50 * j, 65, 50], 0, 3)
            box = pygame.draw.rect(screen, 'blue', [5 + spacing * i, 300, 65, 200], 5, 5)
            if select_rect == idx:
                pygame.draw.rect(screen, 'green', [5 + spacing * i, 300, 65, 200], 3, 5)
            tube_boxes.append(box)

    return tube_boxes


def calc_move(colors, selected_rect, destination):
    if selected_rect == destination or not colors[selected_rect]:
        return colors

    color_to_move = colors[selected_rect][-1]
    length = 1
    for i in range(len(colors[selected_rect]) - 2, -1, -1):
        if colors[selected_rect][i] == color_to_move:
            length += 1
        else:
            break

    if len(colors[destination]) == 0 or colors[destination][-1] == color_to_move:
        for _ in range(min(length, 4 - len(colors[destination]))):
            colors[destination].append(color_to_move)
            colors[selected_rect].pop()
    return colors


def check_victory(colors):
    for tube in colors:
        if len(tube) not in (0, 4):
            return False
        if len(tube) == 4 and len(set(tube)) != 1:
            return False
    return True


run = True
while run:
    timer.tick(fps)

    
    for y in range(HEIGHT):
        color = (
            (y + pygame.time.get_ticks() // 10) % 256,
            (255 - y + pygame.time.get_ticks() // 15) % 256,
            (y * 2 + pygame.time.get_ticks() // 20) % 256
        )
        pygame.draw.line(screen, color, (0, y), (WIDTH, y))

    
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(80)
    overlay.fill((0, 0, 0))
    screen.blit(overlay, (0, 0))

    
    if new_game:
        tubes, tube_colors = generate_start(levels[current_level])
        initial_colors = copy.deepcopy(tube_colors)
        new_game = False

    
    tube_rects = draw_tubes(tubes, tube_colors)

    
    win = check_victory(tube_colors)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                tube_colors = copy.deepcopy(initial_colors)
            elif event.key == pygame.K_RETURN:
                if win:
                    if current_level < len(levels) - 1:
                        current_level += 1
                    else:
                        current_level = 0
                new_game = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not selected:
                for idx, rect in enumerate(tube_rects):
                    if rect.collidepoint(event.pos):
                        selected = True
                        select_rect = idx
            else:
                for idx, rect in enumerate(tube_rects):
                    if rect.collidepoint(event.pos):
                        tube_colors = calc_move(tube_colors, select_rect, idx)
                        selected = False
                        select_rect = None

    
    if win:
        if current_level < len(levels) - 1:
            victory_text = font.render('You Won! Press Enter for next level!', True, 'white')
        else:
            victory_text = font.render('You Won! Press Enter for new board!', True, 'white')
        victory_text_rect = victory_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(victory_text, victory_text_rect)

    level_text = font.render(f'Level: {current_level + 1}', True, 'white')
    level_text_rect = level_text.get_rect(center=(WIDTH / 2, 40))
    screen.blit(level_text, level_text_rect)

    restart_text = font.render('Space-Restart | Enter-New Board', True, 'white')
    screen.blit(restart_text, (10, 10))

    
    pygame.display.flip()

pygame.quit()
