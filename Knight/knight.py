import pygame
import sys

TILE = 80

moves = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

def valid(r, c):
    return 0 <= r < 8 and 0 <= c < 8

def knight_tour(start_r, start_c):
    path = [(start_r, start_c)]
    visited = set(path)
    cur_r, cur_c = start_r, start_c

    for _ in range(63):  # 64 squares total
        next_moves = []

        for dr, dc in moves:
            nr, nc = cur_r + dr, cur_c + dc
            if valid(nr, nc) and (nr, nc) not in visited:
                onward = 0
                for dr2, dc2 in moves:
                    rr, cc = nr + dr2, nc + dc2
                    if valid(rr, cc) and (rr, cc) not in visited:
                        onward += 1
                next_moves.append((onward, nr, nc))

        if not next_moves:
            break

        next_moves.sort(key=lambda x: x[0])
        _, cur_r, cur_c = next_moves[0]

        path.append((cur_r, cur_c))
        visited.add((cur_r, cur_c))

    return path

arrow_heads = {
    ( 2,  1): [( -6, -4), (-6, 4)],   # down-right
    ( 1,  2): [( -4, -6), ( 4, -6)],  # right-down
    (-1,  2): [( -4,  6), ( 4,  6)],  # right-up
    (-2,  1): [(  6, -4), ( 6, 4)],   # up-right
    (-2, -1): [(  6,  4), ( 6,-4)],   # up-left
    (-1, -2): [(  4,  6), (-4, 6)],   # left-up
    ( 1, -2): [(  4, -6), (-4,-6)],   # left-down
    ( 2, -1): [( -6,  4), (-6,-4)],   # down-left
}

def square_center(r, c):
    return (c * TILE + TILE//2, r * TILE + TILE//2)

def draw_arrow(surface, start_center, end_center, dr, dc, color=(50,50,50)):
    x1, y1 = start_center
    x2, y2 = end_center

    pygame.draw.line(surface, color, (x1, y1), (x2, y2), 3)

    left_offset, right_offset = arrow_heads[(dr, dc)]

    left_point  = (x2 + left_offset[0],  y2 + left_offset[1])
    right_point = (x2 + right_offset[0], y2 + right_offset[1])

    pygame.draw.polygon(surface, color, [(x2, y2), left_point, right_point])

def run_visualizer(delay):
    pygame.init()

    W = H = TILE * 8
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Knight's Tour Visualizer")

    light = (240, 217, 181)
    dark = (181, 136, 99)

    knight_img = pygame.image.load("knight.png").convert_alpha()
    knight_img = pygame.transform.scale(knight_img, (TILE, TILE))

    def draw_board():
        for r in range(8):
            for c in range(8):
                color = light if (r + c) % 2 == 0 else dark
                pygame.draw.rect(screen, color,
                                 (c * TILE, r * TILE, TILE, TILE))

    waiting_for_click = True
    start_pos = None
    while waiting_for_click:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                waiting_for_click = False
                start_pos = (mx // TILE, my // TILE)
        pygame.display.flip()

    # Compute the tour
    tour = knight_tour(*start_pos)

    clock = pygame.time.Clock()

    # Draw each move with adjustable delay
    for i in range(len(tour)):
        r, c = tour[i]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_board()

        if i > 0:
            for j in range(i):
                r1, c1 = tour[j]
                r2, c2 = tour[j+1]
                start = square_center(r1, c1)
                end   = square_center(r2, c2)
                dr = r2 - r1
                dc = c2 - c1
                draw_arrow(screen, start, end, dr, dc)

        screen.blit(knight_img, (c * TILE, r * TILE))
        pygame.display.flip()
        clock.tick(delay)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

if __name__ == "__main__":
    try:
        delay = float(input("Enter delay (FPS-style, e.g. 4 for 4 frames/sec): "))
        if delay <= 0:
            delay = 4
    except:
        delay = 4

    run_visualizer(delay)

    input("Press Enter to exit...")
