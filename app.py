from sys import argv
from random import random
from src import *

def main_gui():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    font = pygame.font.SysFont("comicsansms", 31)
    points = Points([])
    road = []
    method = State.EDIT
    while running:
        running, points, method, args = handle_events(method, points, [])
        draw_objects(screen, list([road[i], road[i+1]] for i in range(len(road)-1)), points.P, f"Click to add point, [SPACE] to erase points, [B] to start brute-force method, [N] to start closest neighbours method", font)
        clock.tick(60)

        if method == State.CALCULATE:
            if args == 1: road, l = brute_force(points, 0.5, font, screen)
            elif args == 2: road, l = neighbours(points, 0.5, font, screen)
            else: print(args)
            draw_objects(screen, list([road[i], road[i+1]] for i in range(len(road)-1)), points.P, f"Best road length: {round(l, 1)}", font)
            time.sleep(2)
            method = State.EDIT
            road = []
    pygame.quit()

def main_cli():
    points = Points([])
    for i in range(10):
        points.P.append([round(random() * 100, 2), round(random() * 100, 2)])
    print("Points:")
    print(points.P)
    print("\n\nBrute-force method:\n* Searching...")
    t = time.perf_counter()
    road, l = brute_force(points = points, cli=True)
    t = time.perf_counter() - t
    print(f"* Time = {t}\n* Best route length = {l}\n* Best route = {road}")
    print("\nClosest neighbours method:\n* Searching...")
    t = time.perf_counter()
    road, l = neighbours(points = points, cli=True)
    t = time.perf_counter() - t
    print(f"* Time = {t}\n* Best route length = {l}\n* Best route = {road}")

if __name__ == "__main__":
    if len(argv) == 2 and argv[1] == "CLI":
        main_cli()
    else:
        main_gui()
