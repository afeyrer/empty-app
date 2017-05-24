from ggame import App, RectangleAsset, LineStyle, Color, Sprite
from random import randint

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
dir=7
dirs=1
dirss=1
blue=Color(0x87cefa, 1)
purple=Color(0x7b68ee, 1)
pink=Color(0xff69b4, 1)
line=LineStyle(0,blue)
black = Color(0, 1)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, line, black)
bg = Sprite(bg_asset, (0,0))
pi=3.14159
go=True
lineasset=RectangleAsset(1,100,line,blue)
circle=[Sprite(lineasset, (400,100)), Sprite(lineasset, (400,100)), Sprite(lineasset, (400,100)), Sprite(lineasset, (400,100)), Sprite(lineasset, (400,100)), Sprite(lineasset, (400,100)), Sprite(lineasset, (400,100)), Sprite(lineasset, (400,100)),Sprite(lineasset, (400,100)), Sprite(lineasset, (400,100)), Sprite(lineasset, (400,100)), Sprite(lineasset, (400,100)), Sprite(lineasset, (400,100)), Sprite(lineasset, (400,100)), Sprite(lineasset, (400,100)), Sprite(lineasset, (400,100))]
for x in range(16):
    circle[x].rotation=pi*x/8

lineasset=RectangleAsset(1,50,line,purple)
circles=[Sprite(lineasset, (200,100)), Sprite(lineasset, (200,100)), Sprite(lineasset, (200,100)), Sprite(lineasset, (200,100)), Sprite(lineasset, (200,100)), Sprite(lineasset, (200,100)), Sprite(lineasset, (200,100)), Sprite(lineasset, (200,100)),Sprite(lineasset, (200,100)), Sprite(lineasset, (200,100)), Sprite(lineasset, (200,100)), Sprite(lineasset, (200,100)), Sprite(lineasset, (200,100)), Sprite(lineasset, (200,100)), Sprite(lineasset, (200,100)), Sprite(lineasset, (200,100))]
for x in range(16):
    circles[x].rotation=pi*x/8

lineasset=RectangleAsset(1,30,line,pink)
circless=[Sprite(lineasset, (200,500)), Sprite(lineasset, (200,500)), Sprite(lineasset, (200,500)), Sprite(lineasset, (200,500)), Sprite(lineasset, (200,500)), Sprite(lineasset, (200,500)), Sprite(lineasset, (200,500)), Sprite(lineasset, (200,500)),Sprite(lineasset, (200,500)), Sprite(lineasset, (200,500)), Sprite(lineasset, (200,500)), Sprite(lineasset, (200,500)), Sprite(lineasset, (200,500)), Sprite(lineasset, (200,500)), Sprite(lineasset, (200, 500)), Sprite(lineasset, (200,500))]
for x in range(16):
    circless[x].rotation=pi*x/8


def step():
    for x in circle:
        x.rotation+=pi/64
        x.y+=dir
        """if x.y+100>=SCREEN_HEIGHT or x.y-100<0:
            dir=(0-dir)"""
    for x in circles:
        x.rotation+=pi/64
        x.x+=dirs
    for x in circless:
        x.rotation+=pi/64
        x.x+=dirss
        x.y-=dirss

        
myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run(step)
