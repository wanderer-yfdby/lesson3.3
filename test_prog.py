import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Параметры окна
width = 800
heigth =600
height2 = 400
screen = pygame.display.set_mode((width, heigth))

pygame.display.set_caption("Игруля Тир")
icon = pygame.image.load("img/unnamed.jpg")
pygame.display.set_icon(icon)

# Цвета
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Частота кадров
clock = pygame.time.Clock()
fps = 60

# Параметры целей
target_img = pygame.image.load("img/target.png")
target = target_img
target_size = 80
target_speed = 10
targets = []
score = 0
font = pygame.font.SysFont(None, 36)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def create_target():
    x_pos = random.randint(0, width - target_size)
    y_pos = 0
    targets.append([x_pos, y_pos])


def draw_targets():
    for target in targets:
        pygame.draw.rect(screen, red, (target[0], target[1], target_size, target_size))


def update_targets():
    for target in targets:
        target[1] += target_speed
        if target[1] > height2:
            targets.remove(target)


# Параметры целей
target_img = pygame.image.load("img/target.png")
target = target_img
target_width = 80
target_heigth = 80
target_speed = 2

target_x = random.randint(0, width - target_width)
target_y = random.randint(0, heigth - target_heigth)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


running = True
while running:
    screen.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_heigth:
                target_x = random.randint(0, width - target_width)
                target_y = random.randint(0, heigth - target_heigth)
                score += 1

        # Создание целей
        if random.randint(1, 20) == 1:
            create_target()

        # Отрисовка целей
        draw_targets()
        update_targets()

    # Отображение счета
    draw_text(f"Счет: {score}", font, black, screen, 10, 10)

    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
