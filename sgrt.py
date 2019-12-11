# importing stuff
from graphics import *
import time

# declaring constants
gameOver = False

runGroundY = 300
obX = 1000
obY = 270
obWidth = 40
obHeight= 10
obSpeed = 5

playerRadius = 20
playerX =  100
playerY = runGroundY - playerRadius -1
playerVelocity = -5
playerGravity = 0.2

touchZone = 15
playerGrounded = False


# function definitions

# makes the user jump
def jump(player, obstacle):
    global playerVelocity, playerGravity, playerGrounded, obSpeed 
    player.move(0, playerVelocity)

    # adding +ve to -ve to make it move downward
    playerVelocity += playerGravity
    obstacle.move(-obSpeed, 0)

    playerCurrentYDiff = playerY + playerRadius- player.getP2().getY()
    if  playerCurrentYDiff <= 10 and playerVelocity > 0:
        player.move(0, playerCurrentYDiff)
        # reset velocity
        playerVelocity = -5
        playerGrounded = True
        
    if obstacle.getP1().getX() <= 0:
        obstacle.move(1050, 0)
        

def touches(player, obstacle):
    global playerX, playerRadius
    playerPt1 = player.getP1()
    playerPt2 = player.getP2()
    obstaclePt = obstacle.getP1()
    xMatches= bool (obstaclePt.getX() - playerPt2.getX() <= 0 and obstaclePt.getX() - playerPt2.getX() >= 0)
    yMatches= bool(obstaclePt.getY() > playerPt1.getY() and obstaclePt.getY() < playerPt2.getY() )
    return bool (xMatches and yMatches)

def main():
    global playerGrounded, obstacleY, gameOver, obSpeed, playerRadius
    # intializes the main window
    win = GraphWin("The Slow Down Running Game!", 1000, 500)
    win.setBackground(color_rgb(117, 117, 117))

    # sets up the running foreground
    runGround = Line(Point(0, runGroundY), Point(1000, runGroundY))
    runGround.setOutline(color_rgb(255, 255, 255))
    runGround.setWidth(10)
    runGround.draw(win)

    # sets up the player i.e. a circle
    player = Circle(Point(playerX, playerY), playerRadius)
    player.setFill(color_rgb(255, 234, 148))
    player.setWidth(0)
    player.draw(win)

    # sets up the bullet/obstacle i.e. a rectangle. 
    obstacle = Rectangle(Point(obX, obY), Point(obX+obWidth, obY+obHeight))
    obstacle.setFill(color_rgb(255, 147, 125))
    obstacle.setWidth(0)
    obstacle.draw(win)

    # sets up the gameOverText but does not draw it yet
    gameOverText = Text(Point(470, 250), 'Game Over')
    gameOverText.setFace('helvetica')
    gameOverText.setStyle('bold')
    gameOverText.setSize(36) # maximum possible value is 36

    jumpCounter = 0
    while not gameOver:
        if win.checkKey() == 'space':
            while not playerGrounded:
                jump(player, obstacle)

                if (touches(player, obstacle)):
                    gameOver = True
                    break

            playerGrounded = False
            jumpCounter += 1
        else:
            obstacle.move(-5, 0)
            if obstacle.getP1().getX() <= 0:
                obstacle.move(1050, 0)
            if (touches(player, obstacle)):
                gameOver = True
    if gameOver == True:
        gameOverText.draw(win)
        
               
    # waits for to execute until mouse is clicked in windows    
    win.getMouse()
    # closes windows / games
    win.close()
main()

