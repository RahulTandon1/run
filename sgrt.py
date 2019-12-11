# importing stuff
from graphics import *
import time

# declaring constants
runGroundY = 300
obX = 1000
obY = 250
obWidth = 20
obHeight= 10

playerRadius = 15
playerX =  75
playerY = runGroundY - playerRadius -1
playerVelocity = -10
playerGravity = 0.2

touchZone = 15

# function definitions

def touches(player, obstacle):
    global playerX, playerY, touchZone
    currentPlayerY = player.getP2().getY()
    currentPlayerX = player.getP2().getX()
    if currentPlayerY + touchZone >= playerY:
        player.undraw()
        player = Circle(Point(currentPlayerX, playerY), playerRadius)
        player.draw(win)

# makes the user jump
def jump(player, obstacle):
    global playerVelocity, playerGravity
    print('here')
    player.move(0, playerVelocity)

    # adding +ve to -ve to make it move downward
    playerVelocity += playerGravity
    touches(player, obstacle)


def main():
    # intializes the main window
    win = GraphWin("Bhaag!", 1000, 500)

    # sets up the running foreground
    runGround = Line(Point(0, runGroundY), Point(1000, runGroundY))
    runGround.draw(win)

    # sets up the player i.e. a circle
    player = Circle(Point(playerX, playerY), playerRadius)
    player.draw(win)
    print(player.getP2().getY())

    # sets up the bullet/obstacle i.e. a rectangle. 
    obstacle = Rectangle(Point(obX, obY), Point(obX+obWidth, obY+obHeight))
    obstacle.setFill(color_rgb(200, 20, 20))
    obstacle.setWidth(0)
    obstacle.draw(win)

    
    while True:
        if win.checkKey() == 'space':
            jump(player, obstacle)
    # waits for to execute until mouse is clicked in windows    
    win.getMouse()
    # closes windows / games
    win.close()
main()

