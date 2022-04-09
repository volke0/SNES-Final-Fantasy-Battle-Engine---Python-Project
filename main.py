import pygame as pg 
import inputstream, battle_scene
from vars import *
from setup import *

running = True
playing = True

inputStream = inputstream.InputStream()
battle = battle_scene.BattleScene()

while running == True:

    inputStream.processInput()
    battle.update()
    battle.input(inputStream)
    battle.draw(screen)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    clock.tick(FPS)
    pg.display.flip()
