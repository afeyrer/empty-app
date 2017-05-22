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
x=20
y=0
z=3
snk=[(20,20)]
dir=0
go=True
lineasset=RectangleAsset(1,100,line,blue)
line=Sprite(lineasset, (400,50))

def step():
    global z
    z=z+1
    if go:
        if z==4:
            line.rotation=x
            x=x+(3.14159/4)
            print(x)
            z=0
        
myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run(step)
