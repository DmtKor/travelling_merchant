import pygame
from enum import Enum
import time

class State(Enum):
    EDIT = 1
    CALCULATE = 2

def draw_objects(screen, lines, points, text, font):
    screen.fill("cyan")
    for line in lines:
        pygame.draw.line(screen, (10,10,10), line[0], line[1], 2)
    for point in points:
        pygame.draw.circle(screen, (200, 125, 125), point, 25)
    if text != "":
        text = font.render(text, True, (10, 10, 10))
        screen.blit(text, (30, 20))
    pygame.display.flip()

def handle_events(method, points, args):
    running = True
    args = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if method == State.EDIT:
            if event.type == pygame.MOUSEBUTTONDOWN:
                points.P.append(pygame.mouse.get_pos())
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                points.P = []
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                method = State.CALCULATE
                args = 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                method = State.CALCULATE
                args = 2
        if method == State.CALCULATE:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                args = -1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                args = 1
    return running, points, method, args

def algorithm_gui_update(screen, road, points, text, font, speed):
    draw_objects(screen, list([road[i], road[i+1]] for i in range(len(road)-1)), points.P, text, font)
    ev = handle_events(State.CALCULATE, [], 0)
    if not ev[0]:
        pygame.quit()
    speed = speed + 0.1 * ev[3]
    if speed <= 0:
        speed = 0.1
    time.sleep(speed)
    return speed