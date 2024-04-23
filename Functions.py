from Characters import *

def obstacle_adder(counter: int, obstacles: list):
    if counter > 5 and len(obstacles) == 0:
        obstacles.append(obstacle(1050,400, 20, 60))
        obstacles.append(obstacle(1350,400, 20, 60))
        counter = 0
    return counter, obstacles

def jump_equation(i):
    if i.jumpCount > -10:
        neg = 1
        if i.jumpCount < 0:
            neg = -1
        i.y-= (i.jumpCount**2)*0.3*neg
        i.jumpCount-=1
    else:
        i.isJump= False
        i.jumpCount = 10
        i.y = 371
