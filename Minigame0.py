import sys

import pygame
from pygame.locals import *
import random, time
from Settings import Settings

class character(pygame.sprite.Sprite):
    def __init__(self, path, SCREEN_WIDTH):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.center = (100, 440)
        self.SCREEN_WIDTH = SCREEN_WIDTH

    def move(self, none, score):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < self.SCREEN_WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)

        return score


class rain_drop(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH):
        super().__init__()
        self.image = pygame.image.load("img/Minigames/rain drop.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.SCREEN_WIDTH = SCREEN_WIDTH

    def move(self, snelheid, score):
        self.rect.move_ip(0.5, snelheid)
        if (self.rect.top > 600):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, self.SCREEN_WIDTH - 40), 0)

        return score

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

font_style = pygame.font.SysFont("comicsansms", 20)
font_small = pygame.font.SysFont("comicsansms", 20)

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("The_Escape")

try:
    background = pygame.image.load("img/Minigames/rain drop background.png")
except FileNotFoundError:
    pass





# from rain_drop import rain_drop
#
# from character import character


def gameloop():
    gamer_over = False
    game_close = False

    P1 = character("img/Main Character/Stand.png", SCREEN_WIDTH)
    E1 = rain_drop(SCREEN_WIDTH)
    E2 = rain_drop(SCREEN_WIDTH)

    enemies = pygame.sprite.Group()
    enemies.add(E1, E2)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(P1)
    all_sprites.add(E1, E2)

    INC_SPEED = pygame.USEREVENT + 1
    pygame.time.set_timer(INC_SPEED, 1000)

    snelheid = 1
    SCORE = 0
    SPEED = 10
    SPEED2 = 10

    while not gamer_over:
        snelheid += 0.01
        while game_close:
            SCREEN.fill(RED)
            message("You Lost! Press P=Play Again or ESC=Quit", BLACK)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        gameloop()
                    elif event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                        # pygame.quit()
                        if SCORE > 20:
                            pygame.quit()
                            return None
                        else:
                            gameloop()

        for event in pygame.event.get():
            if event.type == INC_SPEED:
                SPEED += 0.5
            if event.type == QUIT:
                game_over = True

        SCREEN.blit(background, (0, 0))
        scores = font_small.render(str(SCORE), True, BLACK)
        SCREEN.blit(scores, (10, 10))

        for entity in all_sprites:
            SCREEN.blit(entity.image, entity.rect)
            SCORE = entity.move(snelheid, SCORE)

        if pygame.sprite.spritecollideany(P1, enemies):
            music = pygame.mixer.Sound('sounds/rain_drop.mp3')
            music.set_volume(Settings.getMusicVolume())
            pygame.mixer.Channel(2).play(music)
            time.sleep(0.5)

            pygame.display.update()
            game_close = True
            for entity in all_sprites:
                entity.kill()
            time.sleep(2)

        pygame.display.update()
        FramePerSec.tick(FPS)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    SCREEN.blit(mesg, [SCREEN_WIDTH / 65, SCREEN_HEIGHT / 2])





