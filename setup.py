import pygame 

class cube(object):
    rows = 20
    w = 640
    h = 480
    def __init__(self, start, dirX = 1, dirY = 0, color = (255,0,0)):
        self.pos = start
        self.dirX = 1
        self.dirY = 0
        self.color = color

    def move(self, dirX, dirY):
        self.dirX = dirX
        self.dirY = dirY
        self.pos = (self.pos[0] + self.dirX, self.pos[1] + self.dirY)
        
    def draw(self, surface, eyes = False):
        disX = self.w // self.rows
        disY = self.h // self.rows 
        i, j = self.pos[0], self.pos[1]

        pygame.draw.rect(surface, self.color, (i*disX + 1, j*disY + 1, disX - 2, disY - 2))
        if eyes:
            centre = disX // 2
            radius = 3
            circleMiddle = (i*disX+centre-radius,j*disY+8)
            circleMiddle2 = (i*disX + disX -radius*2, j*disY+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)

class snake(object):
    body = []
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirX = 0
        self.dirY = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirX = -1
                    self.dirY = 0
                    self.turns[self.head.pos[:]] = [self.dirX, self.dirY]

                elif keys[pygame.K_RIGHT]:
                    self.dirX = 1
                    self.dirY = 0
                    self.turns[self.head.pos[:]] = [self.dirX, self.dirY]

                elif keys[pygame.K_UP]:
                    self.dirX = 0
                    self.dirY = -1
                    self.turns[self.head.pos[:]] = [self.dirX, self.dirY]

                elif keys[pygame.K_DOWN]:
                    self.dirX = 0
                    self.dirY = 1
                    self.turns[self.head.pos[:]] = [self.dirX, self.dirY]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0],turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                if c.dirX == -1 and c.pos[0] <= 0: 
                    c.pos = (c.rows-1, c.pos[1])
                elif c.dirX == 1 and c.pos[0] >= c.rows-1: 
                    c.pos = (0,c.pos[1])
                elif c.dirY == 1 and c.pos[1] >= c.rows-1: 
                    c.pos = (c.pos[0], 0)
                elif c.dirY == -1 and c.pos[1] <= 0: 
                    c.pos = (c.pos[0],c.rows-1)
                else: 
                    c.move(c.dirX,c.dirY)


    def reset(self,pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)

def drawGrid(w, h, rows, surface):
    horSize = w // rows
    verSize = h // rows

    x = 0
    y = 0
    for i in range(rows):
        x = x + horSize
        y = y + verSize
        pygame.draw.line(surface, (255,255,255), (x,0), (x,w))
        pygame.draw.line(surface, (255,255,255), (0,y), (w,y))

def redrawWindow(surface):
    global rows, width, height, s
    surface.fill((0,0,0))
    snek.draw(surface)
    drawGrid(width, height, rows, surface)
    pygame.display.update()

def randomSnack(rows,items):
    pass

def message(subject, context):
    pass

def run():
    global width, rows, height, snek
    width = 640
    height = 480
    rows = 20
    win = pygame.display.set_mode((width, height))
    snek = snake((255,0,0), (10,10))

    clock = pygame.time.Clock()
    flag = True
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        snek.move()
        redrawWindow(win)

if __name__ == "__main__":
    run()