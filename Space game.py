import pygame
from pygame import mixer
import math

# Get screen
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Bullet
img_bullet = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 500
bullet_x_change = 0
bullet_y_change = 15
____visible____ = False

# BG Image
img_bg = pygame.image.load("background (1).jpg")
bg_x = 0
bg_y = 0

# Player
img_player = pygame.image.load("Rocket.png")
player_x = 368
player_y = 530
player_x_change = 0
player_y_change = 0
score = 0
# Enemies
img_enemy = pygame.image.load("enemy.png")
enemy_x = 700
enemy_y = 75
enemy_x_change = 2.5
enemy_y_change = 50

img_enemy2 = pygame.image.load("ufo (1).png")
enemy2_x = 175
enemy2_y = 150
enemy2_x_change = -1.5
enemy2_y_change = 40

img_enemy3 = pygame.image.load("alien.png")
enemy3_x = 100
enemy3_y = 100
enemy3_x_change = 1.0
enemy3_y_change = 45

img_enemy4 = pygame.image.load("space-ship.png")
enemy4_x = 200
enemy4_y = 300
enemy4_x_change = 1.0
enemy4_y_change = 45
# Label
font_name = pygame.font.get_default_font()
font = pygame.font.SysFont("arial", True, False, 15)
text = "Score = " + str(score)
label = font.render(text, True, (100, 250, 125))
label_x = 275
label_y = 445
# Music
mixer.music.load("Background_music (1).mp3")
mixer.music.play(-1)


def ____player____(x, y):
    screen.blit(img_player, (x, y))


def ____label____(x, y):
    screen.blit(label, (x, y))


def ____bg____(x, y):
    screen.blit(img_bg, (x, y))


def ____character____(character, x, y):
    screen.blit(character, (x, y))


def ____shoot_bullet____(x, y):
    global ____visible____
    ____visible____ = True
    screen.blit(img_bullet, (x + 16, y + 10))


pygame.display.set_caption("☄️🚀Space🛸Invasion🚀☄️")

score = 0
is_running = True
while is_running:
    # screen.fill((13, 0, 110))
    ____bg____(bg_x, bg_y)

    def ____collision____(x_1,  y_1,  x_2, y_2):
        distance = math.sqrt(math. pow(x_1 - x_2,  2) + math.pow(y_1 - y_2, 2))
        if distance < 27:
            return True
        else:
            return False
    for event in pygame.event.get():
        # print(str(event.type) + " : " + event.key)
        # print(str(event.type))
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -2.5
            if event.key == pygame.K_RIGHT:
                player_x_change = 2.5
            if event.key == pygame.K_UP:
                player_y_change = -2.5
            if event.key == pygame.K_DOWN:
                player_y_change = 2.5
            if event.key == pygame.K_SPACE:
                if not ____visible____:
                    bullet_x = player_x
                    ____shoot_bullet____(player_x, bullet_y)

        player_x += player_x_change
        # player_y += player_y_change
        enemy_x += enemy_x_change
        enemy2_x += enemy2_x_change
        enemy3_x += enemy3_x_change
        enemy4_x += enemy4_x_change

        if player_x <= 0:
            player_x = 0
        elif player_x >= 736:
            player_x = 736
        if player_y <= 0:
            player_y = 0
        elif player_y >= 546:
            player_y = 545
        if enemy_x <= 0:
            enemy_x_change = 1
            enemy_y += enemy_y_change
        elif enemy_x >= 736:
            enemy_x_change = -1
            enemy_y += enemy_y_change
        if enemy2_x <= 0:
            enemy2_x_change = 3
            enemy2_y += enemy2_y_change
        elif enemy2_x >= 736:
            enemy2_x_change = -3
            enemy2_y += enemy2_y_change
        if enemy3_x <= 0:
            enemy3_x_change = 2
            enemy3_y += enemy3_y_change
        elif enemy3_x >= 736:
            enemy3_x_change = -1
            enemy3_y += enemy3_y_change
        if enemy4_x <= 0:
            enemy4_x_change = 2
            enemy4_y += enemy4_y_change
        elif enemy4_x >= 736:
            enemy4_x_change = -2
            enemy4_y += enemy4_y_change

        if bullet_y <= -120:
            bullet_y = 500
        if ____visible____:
            ____shoot_bullet____(player_x, bullet_y)
            bullet_y -= bullet_y_change
        hit = ____collision____(enemy_x,  enemy_y,  bullet_x,  bullet_y)
        hit2 = ____collision____(enemy2_x,  enemy2_y,  bullet_x,  bullet_y)
        hit3 = ____collision____(enemy3_x,  enemy3_y,  bullet_x,  bullet_y)
        hit4 = ____collision____(enemy4_x,  enemy4_y,  bullet_x,  bullet_y)

        if hit:
            bullet_y = 500
            score += 1
            print(score)
            enemy_x = 700
            enemy_y = 75
        if hit2:
            bullet_y = 500
            score += 1
            print(score)
            enemy2_x = 175
            enemy2_y = 150
        if hit3:
            bullet_y = 500
            score += 1
            print(score)
            enemy3_x = 100
            enemy3_y = 100
        if hit4:
            bullet_y = 500
            score += 1
            print(score)
            enemy4_x = 200
            enemy4_y = 300

        ____character____(img_enemy, enemy_x, enemy_y)
        ____character____(img_enemy2, enemy2_x, enemy2_y)
        ____character____(img_enemy3, enemy3_x, enemy3_y)
        ____character____(img_enemy4, enemy4_x, enemy4_y)
        ____character____(img_player, player_x, player_y)
        ____label____(label_x, label_y)
        pygame.display.update()
