from ggame import App, RectangleAsset, LineStyle, Color, Sprite
from random import randint

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

blue=Color(0x87cefa, 1)
purple=Color(0x7b68ee, 1)
line=LineStyle(0,blue)
black = Color(0, 1)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, line, black)
bg = Sprite(bg_asset, (0,0))
pi=3.14159
go=True
lineasset=RectangleAsset(1,100,line,blue)
circle=[Sprite(lineasset, (400,100)), Sprite(lineasset, (400,100)), Sprite(lineasset, (400,100)), Sprite(lineasset, (400,100)), Sprite(lineasset, (400,100)), Sprite(lineasset, (400,100)), Sprite(lineasset, (400,100)), Sprite(lineasset, (400,100)),Sprite(lineasset, (400,100)), Sprite(lineasset, (400,100)), Sprite(lineasset, (400,100)), Sprite(lineasset, (400,100)), Sprite(lineasset, (400,100)), Sprite(lineasset, (400,100)), Sprite(lineasset, (400,100)), Sprite(lineasset, (400,100))]
circle[1].rotation=pi/8
circle[2].rotation=pi/4
circle[3].rotation=pi*3/8
circle[4].rotation=pi/2
circle[5].rotation=pi*5/8
circle[6].rotation=pi*3/4
circle[7].rotation=pi*7/8
circle[8].rotation=pi
circle[9].rotation=pi*9/8
circle[10].rotation=pi*5/4
circle[11].rotation=pi*11/8
circle[12].rotation=pi*3/2
circle[13].rotation=pi*13/8
circle[14].rotation=pi*7/4
circle[15].rotation=pi*15/8

lineasset=RectangleAsset(1,50,line,purple)
circles=[Sprite(lineasset, (200,100)), Sprite(lineasset, (200,100)), Sprite(lineasset, (200,100)), Sprite(lineasset, (200,100)), Sprite(lineasset, (200,100)), Sprite(lineasset, (200,100)), Sprite(lineasset, (200,100)), Sprite(lineasset, (200,100)),Sprite(lineasset, (200,100)), Sprite(lineasset, (200,100)), Sprite(lineasset, (200,100)), Sprite(lineasset, (200,100)), Sprite(lineasset, (200,100)), Sprite(lineasset, (200,100)), Sprite(lineasset, (200,100)), Sprite(lineasset, (200,100))]
circles[1].rotation=pi/8
circles[2].rotation=pi/4
circles[3].rotation=pi*3/8
circles[4].rotation=pi/2
circles[5].rotation=pi*5/8
circles[6].rotation=pi*3/4
circles[7].rotation=pi*7/8
circles[8].rotation=pi
circles[9].rotation=pi*9/8
circles[10].rotation=pi*5/4
circles[11].rotation=pi*11/8
circles[12].rotation=pi*3/2
circles[13].rotation=pi*13/8
circles[14].rotation=pi*7/4
circles[15].rotation=pi*15/8
def step():
    for x in circle:
        x.rotation+=pi/64
        x.y+=1
    for x in circles:
        x.rotation+=pi/64
        x.x+=1

        
myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run(step)
