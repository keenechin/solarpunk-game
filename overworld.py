import pygame as pg 
from scene import Scene
import numpy as np
from dataclasses import dataclass
from enum import IntEnum

@dataclass
class Player():
    x : float 
    y : float
    dx : float = 0
    dy : float = 0
    color = pg.Color((0,0,0))
    speed = 1.0
    size = 0.1
    
class Material(IntEnum):
    DIRT = 0
    WATER = 1


class Overworld(Scene):
    def __init__(self, screen):
        self.screen = screen
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.names = { 
                    Material.DIRT : "dirt",
                    Material.WATER : "water"
                }

        self.colors = {
                    Material.DIRT : pg.Color((100,50,0)),
                    Material.WATER : pg.Color((0, 100, 200))
                }
        self.map = self.get_map()
        self.num_rows, self.num_cols = np.shape(self.map)
        self.block_size = int(self.width/self.num_cols)

        self.player = Player(
                                x=0 * self.block_size,
                                y=3 * self.block_size, 
                                dx=0,
                                dy=0
                             )
    def get_map(self):
        map = np.array([[1, 1, 1, 1, 1, 1], 
                        [1, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 1, 1],
                        [0, 0 ,0, 1, 1, 1],
                        [0, 0, 0, 0, 0, 0]])
        return map


    def keydown_handler(self, event):
        player = self.player
        block_size = self.block_size
        fps = 60
        if event.key == pg.K_w:
            player.dy = -player.speed * block_size/fps
        if event.key == pg.K_s:
            player.dy = player.speed * block_size/fps
        if event.key == pg.K_a:
            player.dx = -player.speed * block_size/fps
        if event.key == pg.K_d:
            player.dx = player.speed * block_size/fps

    def keyup_handler(self, event):
        player = self.player
        block_size = self.block_size
        fps = 60
        if event.key == pg.K_w:
            player.dy = 0
        if event.key == pg.K_s:
            player.dy = 0
        if event.key == pg.K_a:
            player.dx = 0
        if event.key == pg.K_d:
            player.dx = 0

    def px_to_block(self, r, c):
        return [int(r//self.block_size), int(c//self.block_size)]



    def update(self):
        player = self.player
        startx = player.x
        starty = player.y
        player.x += player.dx
        player.y += player.dy
        player.y = np.clip(player.y, 0+player.size, self.height-player.size)
        player.x = np.clip(player.x, 0-player.size, self.width-player.size)
        pos = self.px_to_block(player.y, player.x)
        blockMat = self.map[pos[0], pos[1]]
        if blockMat == Material.WATER:
            player.x = startx
            player.y = starty
            

    def render(self):  
        screen = self.screen
        num_rows = self.num_rows
        num_cols = self.num_cols
        width =  self.block_size
        height = self.block_size
        for r, row in enumerate(self.map):
            for  c, mat in enumerate(row):
                left = int((c * width))
                top = int((r * height))
                pg.draw.rect(screen,
                             self.colors[mat],
                             pg.Rect(left, top, width, height))
        player = self.player
        pg.draw.circle(screen, player.color, (player.x, player.y), self.block_size * player.size) 
        
                


    


