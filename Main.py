from Base import *
from Characters import *
from Functions import *
pygame.init() 
win = pygame.display.set_mode((WIN_HEIGHT, WIN_WIDTH))
pygame.display.set_caption('Dinousar Game')

def redraw_game_window():
    pygame.draw.rect(win, (255, 255, 255), (x, y, WIN_HEIGHT, WIN_WIDTH))
    pygame.draw.rect(win, (144, 0, 0), (0, 450, 1000, 129))
    for i in rockets:
        i.draw(win)
    LeBlob.draw(win)
    Target.draw(win)
    score_tab = font.render(f'Score: {score}', 1, (0, 0, 0))
    win.blit(score_tab, (800, 25))
    for i in obstacles:
        i.draw(win)
    pygame.display.update()

#MainLoop
font = pygame.font.SysFont('comicsans', 20, True)
run = True
Rocket = flyer(1000, 271, 3000, 20)
LeBlob = dinousar(20, 371, 40, 40, 5)
Target = targ(980, 250, 20, 50, white)
obstacles = []
shootLoop = 0
counter = 0
rockets = []

while run:
    pygame.time.delay(50)
    redraw_game_window()
    keys = pygame.key.get_pressed()

    if shootLoop > 0:
        shootLoop+=1
    if shootLoop > 3:
        shootLoop = 0

    #Obstacle Adder
    counter+=1
    counter, obstacles = obstacle_adder(counter, obstacles)
    
    #Collision Checker
    for i in obstacles:
        if LeBlob.hitbox[0] + LeBlob.hitbox[2] > i.hitbox[0] and LeBlob.hitbox[0] < i.hitbox[0] + i.hitbox[2]:
            if LeBlob.hitbox[1] + LeBlob.hitbox[3] > i.hitbox[1]:
                LeBlob.hit()       

        if i.x > 0:
            i.x -= i.vel
        else:
            obstacles.pop(obstacles.index(i))
            score+=10

    for i in rockets:
        if i.x < 1000 and i.x > 0:
            i.x+=i.vel
        else:
            rockets.pop(rockets.index(i))
        
        if (i.radius+i.x) > Target.x: 
            if i.y in range(Target.y, (Target.y + Target.height)): 
                score+=100
                rockets.pop(rockets.index(i))

    #Key-stroke checker
    if keys[pygame.K_s] and shootLoop == 0 and len(rockets)< 5:
        rockets.append(flyer(round(LeBlob.x + LeBlob.width // 2), round(LeBlob.y + LeBlob.height // 2), 6, (0,0,0)))

    if not (LeBlob.isJump):
        if keys[pygame.K_SPACE]:
            LeBlob.isJump = True
    else:
        jump_equation(LeBlob)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    

