import pygame as pg
from pygame import key, mouse
from abc import ABC

class Scene(ABC):
    def keydown_handler(self, event):
        print(f"{key.name(event.key)} pressed")  

    def keyup_handler(self, event):
        print(f"{key.name(event.key)} released")  

    def clickdown_handler(self, event):
        print(f"mouse{event.button} clicked")  

    def clickup_handler(self, event):
        print(f"mouse{event.button} released ")

    def motion_handler(self, event):
        vel = (event.rel[0] ** 2 + event.rel[1] **2) ** 0.5
        if vel > 100:
            print(f"mouse pos: {event.pos}, mouse vel:{event.rel}")
