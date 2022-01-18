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
        

def main(width=1080, height=720):
    pg.init()
    screen = pg.display.set_mode((width, height))
    scene = Overworld()
    while True:
        pg.display.update()
        handle_events(scene)
        screen.fill((100,50,0))

if __name__ == "__main__":
    main()
