import pygame, sys, random, time

pygame.init()

# constanten
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
gray = (128, 128, 1280)
WIDTH = 400
HEIGHT = 500
background = white
player = pygame.image.load("img/Main Character/Stand.png")
fps = 60

DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
DISPLAYSURF.fill(background)

font = pygame.font.SysFont("monospace", 15)
timer = pygame.time.Clock()

score = 0
high_score = 0

# variabelen
player_x = 170
player_y = 400
platforms = [[175, 480, 70, 10], [85, 370, 70, 10], [265, 370, 70, 10], [175, 260, 70, 10], [85, 150, 70, 10],
             [265, 150, 70, 10], [175, 40, 70, 10]]
jump = False
y_change = 0
x_change = 0
player_speed = 3

# scherm
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("springend mannetje")


# def check_collisions (rect_list, j):
def check_collisions(rect_list, j):
    global player_x
    global player_y
    global y_change
    for i in range(len(rect_list)):
        if rect_list[i].colliderect([player_x + 20, player_y + 60, 35, 5]) and jump == False and y_change > 0:
            j = True
    return j


# update player y position every loop
def update_player(y_pos):
    global jump
    global y_change
    jump_height = 10
    gravity = .4
    if jump:
        y_change = -jump_height
        jump = False
    y_pos += y_change
    y_change += gravity
    return y_pos


# handle movement of platforms as game progresses

def update_platforms(my_list, y_pos, change):
    global score
    if y_pos < 250 and change < 0:
        for i in range(len(my_list)):
            my_list[i][1] -= change
    else:
        pass
    for item in range(len(my_list)):
        if my_list[item][1] > 500:
            my_list[item] = [random.randint(0, 320), random.randint(-50, -10), 70, 10]
            score += 1
    return my_list


font = pygame.font.SysFont("comicsansms", 15)
font_small = pygame.font.SysFont("comicsansms", 10)
font_style = pygame.font.SysFont("comicsansms", 15)
game_over = font.render("Game Over!", True, black)
game_close = False
score_text = pygame.font.SysFont("comicsansms", 15)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    DISPLAYSURF.blit(mesg, [WIDTH / 3.5, HEIGHT / 2])

def gameloop():
    global player, player_x, player_y, platforms, jump, x_change, y_change, score
    standard_values = player, player_x, player_y, platforms, jump, x_change, y_change, score
    running = True
    game_over = False
    game_close = False

    while running == True:
        timer.tick(fps)
        screen.fill(background)
        screen.blit(player, (player_x, player_y))
        blocks = []
        score_text = font.render("Score: " + str(score), True, black)
        DISPLAYSURF.blit(score_text, (280, 0))

        if player_y > 500:
            game_close = True
            DISPLAYSURF.fill(red)
            pygame.display.update()

            while game_close:

                message("You Lost! Press ESC-Quit", black)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:

                            if score > 12:
                                return None
                            else:
                                game_close = False
                                player, player_x, player_y, platforms, jump, x_change, y_change, score = standard_values
                                gameloop()

        for i in range(len(platforms)):
            block = pygame.draw.rect(screen, black, platforms[i], 0, 3)
            blocks.append(block)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_close = True
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -player_speed
                if event.key == pygame.K_RIGHT:
                    x_change = player_speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_change = 0
                if event.key == pygame.K_RIGHT:
                    x_change = 0

        jump = check_collisions(blocks, jump)
        player_x += x_change
        player_y = update_player(player_y)
        platforms = update_platforms(platforms, player_y, y_change)
        if x_change > 0:
            player = pygame.image.load("img/Main Character/Stand.png")
        elif x_change < 0:
            player = pygame.transform.flip(pygame.image.load("img/Main Character/Stand.png"), 1, 0)

        pygame.display.flip()
    pygame.quit()

# gameloop()
