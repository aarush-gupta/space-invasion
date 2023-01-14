import pygame
# from tkinter import *
# import random
# from pygame import mixer
# import math
# im a puppy
# Get screen
pygame.init()
screen = pygame.display.set_mode((800, 600))

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
enemy4_y = 500
enemy4_x_change = 1.0
enemy4_y_change = 45

img_enemy5 = pygame.image.load("space-ship.png")
enemy5_x = 200
enemy5_y = 300
enemy5_x_change = -1.0
enemy5_y_change = 45

font_name = pygame.font.get_default_font()
font = pygame.font.SysFont("arial", True, False, 15)
text = "Score = " + str(score)
label = font.render(text, True, (100, 255, 125))
label_x = 250
label_y = 450


def ____player____(x, y):
    screen.blit(img_player, (x, y))


def ____label____(x, y):
    screen.blit(label, (x, y))


def ____bg____(x, y):
    screen.blit(img_bg, (x, y))


def ____character____(character, x, y):
    screen.blit(character, (x, y))


pygame.display.set_caption("☄️🚀Space🛸Invasion🚀☄️")


is_running = True
while is_running:
    # screen.fill((13, 0, 110))
    ____bg____(bg_x, bg_y)

    for event in pygame.event.get():
        # print(str(event.type) + " : " + event.key)
        print(str(event.type))
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
            if event.key == pygame.K_UP:
                player_y_change = -5
            if event.key == pygame.K_DOWN:
                player_y_change = 5

        player_x += player_x_change
        player_y += player_y_change

        enemy_x += enemy_x_change
        enemy2_x += enemy2_x_change
        enemy3_x += enemy3_x_change
        enemy4_x += enemy4_x_change
        enemy5_x += enemy5_x_change

        if player_x <= 0:
            player_x = 0
        elif player_x >= 736:
            player_x = 736
        if player_y <= 0:
            player_y = 0
        elif player_y >= 546:
            player_y = 545
        if enemy_x <= 0:
            enemy_x = 0.75
            enemy_y += enemy_y_change
        elif enemy_x >= 736:
            enemy_x_change = -0.75
            enemy_y += enemy_y_change
        if enemy2_x <= 0:
            enemy2_x = 3
            enemy2_y += enemy2_y_change
        elif enemy2_x >= 736:
            enemy2_x_change = -3
            enemy2_y += enemy2_y_change
        if enemy3_x <= 0:
            enemy3_x = 1
            enemy3_y += enemy3_y_change
        elif enemy3_x >= 736:
            enemy3_x_change = -1
            enemy3_y += enemy3_y_change
        if enemy4_x <= 0:
            enemy4_x = 2
            enemy4_y += enemy4_y_change
        elif enemy4_x >= 736:
            enemy4_x_change = -2
            enemy4_y += enemy4_y_change
        if enemy5_x <= 0:
            enemy5_x = 2.3
            enemy5_y += enemy5_y_change
        elif enemy5_x >= 736:
            enemy5_x_change = -2.3
            enemy5_y += enemy5_y_change
        score += 1
        ____character____(img_enemy, enemy_x, enemy_y)
        ____character____(img_enemy2, enemy2_x, enemy2_y)
        ____character____(img_enemy3, enemy3_x, enemy3_y)
        ____character____(img_enemy4, enemy4_x, enemy4_y)
        ____character____(img_enemy5, enemy5_x, enemy5_y)
        ____character____(img_player, player_x, player_y)
        ____label____(label_x, label_y)

        pygame.display.update()
