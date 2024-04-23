from Base import *


class flyer(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 12
        self.hitbox = (self.x, self.y)

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
        self.hitbox = (self.x, self.y)

class targ(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        self.hitbox = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, black, self.hitbox, 2)

class dinousar(object):
    def __init__(self, x, y, width, height, vel):
        self.x = x
        self.y = y
        self.width = width
        self.vel = vel
        self.height = height
        self.isJump = False
        self.jumpCount = 10
        self.start = 5
        self.hitbox = (self.x+5, self.y, 72, 89)

    def draw(self, win):
        if self.start > -5:
            win.blit(Dino[0], (self.x, self.y))
            self.start -=1
        else:
            win.blit(Dino[1], (self.x, self.y))
            self.start +=5
        self.hitbox = (self.x+5, self.y, 70, 80)

    def hit(self):
        for i in obstacles:
            obstacles.pop(obstacles.index(i))
        ending_font = pygame.font.SysFont('comicsans', 100)
        end_text = ending_font.render('YOU LOSE', 1, red)
        win.blit(end_text, (250-(end_text.get_width()/2), 200))
        pygame.display.update()
        global score
        score=0

        i = 0
        while i < 200:
            pygame.time.delay(10)
            i+=1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()

class obstacle(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.position = (x, y)
        self.vel = 10
        self.hitbox = (self.x, self.y, width, height)

    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.width, self.height))
        self.hitbox = (self.x, self.y, self.width, self.height)
