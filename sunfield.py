import pygame as pg
import sys
from overworld import Overworld

def handle_events(scene):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.KEYDOWN:
            scene.keydown_handler(event)

        if event.type == pg.KEYUP:
            scene.keyup_handler(event)
        
        if event.type == pg.MOUSEBUTTONDOWN:
            scene.clickdown_handler(event)

        if event.type == pg.MOUSEBUTTONUP:
            scene.clickup_handler(event)

        if event.type == pg.MOUSEMOTION:
            scene.motion_handler(event)
        

def main(width=600, height=600):
    pg.init()
    clock = pg.time.Clock()
    screen = pg.display.set_mode((width, height))
    scene = Overworld(screen)
    fps = 60
    while True:
        pg.display.update()
        handle_events(scene)
        screen.fill(pg.Color(255,255,255))
        scene.update()
        scene.render()
        clock.tick(fps)

if __name__ == "__main__":
    main()
