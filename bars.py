import pygame as pg 
from vars import *

class ActionBar:
    def __init__(self, x, y, max_counter):
        self.x = x
        self.y = y 
        self.counter = 0
        self.max_counter = max_counter
        self.on = True
        self.timer = 10

    def draw(self, screen, counter, width=150, height=10, color=DARK_BLUE, flash=False, flash_color=FLUORESCENT_BLUE):
        self.counter = counter
        ratio = self.counter / self.max_counter
        pg.draw.rect(screen, GREY, (self.x, self.y, width, height))

        if self.counter < self.max_counter:
            pg.draw.rect(screen, color, (self.x, self.y, (width * ratio), height))
        if round(self.counter) >= self.max_counter:
            if flash == False:
                pg.draw.rect(screen, flash_color, (self.x, self.y, (width * ratio), height))
            else:
                if self.timer <= 0:
                    if self.on == False:
                        self.on = True
                    else:
                        self.on = False
                    self.timer = 10

                if self.timer > 0:
                    self.timer -= 1

                if self.on == True:
                    pg.draw.rect(screen, color, (self.x, self.y, (width * ratio), height))
                else:
                    pg.draw.rect(screen, flash_color, (self.x, self.y, (width * ratio), height))