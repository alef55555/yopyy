import pygame
import random

WIDTH = 640  # ширина игрового окна
HEIGHT = 520 # высота игрового окна
FPS = 60 # частота кадров в секунду

# создаем игру и окно
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tanks")
background = pygame.Surface((300, 300))
background.fill(pygame.Color('#000000'))
clock = pygame.time.Clock()


white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)


class Bullet:
    x = 0
    y = 0
    width = 10
    height = 10
    speed = 3
    direct = 0 #0-up, 1-right, 2-down, 3-left
    
    def __init__(self, x, y, width, height,direct):
        self.x = x
        self.y = y     
        self.width = width     
        self.height = height
        self.direct = direct
        
    
    
class Block:
    global pygame
    
    def __init__(self, x, y, width, height,imagePath):
        self.x = x
        self.y = y     
        self.width = width     
        self.height = height   
        self.imagePath = imagePath
        self.frames = []
        
        if(len(imagePath) > 0):  
            self.frames.append(pygame.image.load(imagePath))        
        
    def getCurrentFrame(self):
        if (len(self.frames) > 0):
            return self.frames[0]
        else:
            return pygame.Surface((0,0))

class Tank:
    speed = 1
    current_frame_index = 0
    animation_ticker = 0
    x = 0
    y = 0
    width = 16
    height = 16
    
    reload = 0
    
    direct = 0 #0-up, 1-right, 2-down, 3-left
    frameDirectOffset = 0
    
    frames = []
    
    global pygame
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.reload = 0
        
        for i in range(1, 9):
            self.frames.append(pygame.image.load(f"tank/tank{i}.png"))        
            
    def setDirect(self, direct):
        self.direct = direct
        
        if self.direct == 0: #UP
            self.frameDirectOffset = 0
        elif self.direct == 1: #RIGHT
            self.frameDirectOffset = 6
        elif self.direct == 2: #DOWN
            self.frameDirectOffset = 4
        elif self.direct == 3: #LEFT
            self.frameDirectOffset = 2       
            
    def move(self, direct):
        if direct == 0: #UP
            self.y -= self.speed
        elif direct == 1: #RIGHT
            self.x += self.speed
        elif direct == 2: #DOWN
            self.y += self.speed
        elif direct == 3: #LEFT
            self.x -= self.speed
            
        self.setDirect(direct)
            
    def update(self):
        if (self.reload > 0):
            self.reload-=1
        self.tickAnimation()
        
    def tickAnimation(self):
        self.animation_ticker += 1
        if self.animation_ticker > 5:
            self.current_frame_index += 1
            self.animation_ticker = 0
            if (self.current_frame_index > 1):
                self.current_frame_index = 0
                
    def getCurrentFrame(self):
        return self.frames[self.frameDirectOffset + self.current_frame_index]
    

    def fireBullet(self):
        if self.reload == 0:
            self.reload +=60
            if self.direct == 0:
                return Bullet(self.x+6,self.y-3,3,3,self.direct)
            elif self.direct == 1:
                return Bullet(self.x+17,self.y+5,3,3,self.direct)
            elif self.direct == 2:
                return Bullet(self.x+7,self.y+17,3,3,self.direct)
            elif self.direct == 3:
                return Bullet(self.x-5,self.y+6,3,3,self.direct)  
            
class Tankk():
    speed = 1
    current_frame_index = 0
    animation_ticker = 0
    x = 0
    y = 0
    width = 16
    height = 16
    
    reload = 0
    
    direct = 0 #0-up, 1-right, 2-down, 3-left
    frameDirectOffset = 0
    
    frames = []
    
    global pygame
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.reload = 0
        
        for i in range(1, 9):
            self.frames.append(pygame.image.load(f"tank/tank1{i}.png"))        
            
    def setDirect(self, direct):
        self.direct = direct
        
        if self.direct == 0: #UP
            self.frameDirectOffset = 0
        elif self.direct == 1: #RIGHT
            self.frameDirectOffset = 6
        elif self.direct == 2: #DOWN
            self.frameDirectOffset = 4
        elif self.direct == 3: #LEFT
            self.frameDirectOffset = 2       
            
    def move(self, direct):
        if direct == 0: #UP
            self.y -= self.speed
        elif direct == 1: #RIGHT
            self.x += self.speed
        elif direct == 2: #DOWN
            self.y += self.speed
        elif direct == 3: #LEFT
            self.x -= self.speed
            
        self.setDirect(direct)
            
    def update(self):
        if (self.reload > 0):
            self.reload-=1
        self.tickAnimation()
        
    def tickAnimation(self):
        self.animation_ticker += 1
        if self.animation_ticker > 5:
            self.current_frame_index += 1
            self.animation_ticker = 0
            if (self.current_frame_index > 1):
                self.current_frame_index = 0
                
    def getCurrentFrame(self):
        return self.frames[self.frameDirectOffset + self.current_frame_index]
    

    def fireBullet(self):
        if self.reload == 0:
            self.reload +=60
            if self.direct == 0:
                return Bullet(self.x+6,self.y-3,3,3,self.direct)
            elif self.direct == 1:
                return Bullet(self.x+17,self.y+5,3,3,self.direct)
            elif self.direct == 2:
                return Bullet(self.x+7,self.y+17,3,3,self.direct)
            elif self.direct == 3:
                return Bullet(self.x-5,self.y+6,3,3,self.direct)    

tank2 = Tankk(200,256)
tank1 = Tank(320,256)
bullets = []    
blocks = []

blocks.append(Block(200,150, 120,40, "tank/wall1.png"))
blocks.append(Block(10,36, 120,40,"tank/wall1.png"))
blocks.append(Block(125,67, 120,40, "tank/wall1.png"))
blocks.append(Block(0,0, WIDTH,2, ""))
blocks.append(Block(0,0, 2,HEIGHT, ""))
blocks.append(Block(0,HEIGHT-2, WIDTH,10, ""))
blocks.append(Block(WIDTH-2,0, 10,HEIGHT, ""))

def hitTest(x,y,x1,y1,x2,y2,x3,y3):

    if x3 < x or y3 < y or x2 > x1 or y2 > y1:

        return False

    else:

        return True

    
            

# Цикл игры
running = True
while running:
    # держим цикл на правильной скорости
    clock.tick(FPS)
    
    # Ввод процесса (события)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and tank1.x > 0:
        tank1.move(3)
    elif keys[pygame.K_RIGHT] and tank1.x + tank1.width < WIDTH:
        tank1.move(1)
    elif keys[pygame.K_UP] and tank1.y > 0:
        tank1.move(0)
    elif keys[pygame.K_DOWN] and tank1.y + tank1.height < HEIGHT:
        tank1.move(2)
    elif keys[pygame.K_SPACE]:
        b = tank1.fireBullet()
        if (b):
            bullets.append(b)
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and tank2.x > 0:
        tank2.move(3)
    elif keys[pygame.K_d] and tank2.x + tank2.width < WIDTH:
        tank2.move(1)
    elif keys[pygame.K_w] and tank2.y > 0:
        tank2.move(0)
    elif keys[pygame.K_s] and tank2.y + tank2.height < HEIGHT:
        tank2.move(2)
    elif keys[pygame.K_f]:                   
        b = tank2.fireBullet()
        if (b):
            bullets.append(b)        
    
    #выводим кадры, обновляем экран
    screen.fill(black)
    
    tank1.update()
    screen.blit(tank1.getCurrentFrame(), [tank1.x, tank1.y])
    tank2.update()
    screen.blit(tank2.getCurrentFrame(), [tank2.x, tank2.y])    
    
    
    for block in blocks:
        tmp = pygame.transform.scale(
            block.getCurrentFrame(), (block.width,
                       block.height))        
        screen.blit(tmp, [block.x, block.y])
        pygame.draw.rect(screen, green, (block.x, block.y, block.width, block.height),1)        
        print(hitTest(tank1.x, tank1.y, tank1.x+tank1.width, tank1.y+tank1.height, block.x, block.y, block.x+block.width, block.y+block.height))
        if hitTest(tank1.x, tank1.y, tank1.x+tank1.width, tank1.y+tank1.height, block.x, block.y, block.x+block.width, block.y+block.height) == True:
            if tank1.direct == 0:
                tank1.y = block.y+block.height+2
            elif tank1.direct == 1:
                tank1.x = block.x-tank1.width-2   
            elif tank1.direct == 2:
                tank1.y = block.y-tank1.height-2 
            elif tank1.direct == 3:
                tank1.x = block.x+block.width+2
        if hitTest(tank2.x, tank2.y, tank2.x+tank2.width, tank2.y+tank2.height, block.x, block.y, block.x+block.width, block.y+block.height) == True:
            if tank2.direct == 0:
                tank2.y = block.y+block.height+2
            elif tank2.direct == 1:
                tank2.x = block.x-tank2.width-2   
            elif tank2.direct == 2:
                tank2.y = block.y-tank2.height-2 
            elif tank2.direct == 3:
                tank2.x = block.x+block.width+2
        if hitTest(tank1.x, tank1.y, tank1.x+tank1.width, tank1.y+tank1.height, tank2.x, tank2.y, tank2.x+tank2.width, tank2.y+tank2.height) == True:
            if tank1.direct == 0:
                tank1.y = tank1.y
            elif tank1.direct == 1:
                tank1.x = tank1.x  
            elif tank1.direct == 2:
                tank1.y = tank1.y
            elif tank1.direct == 3:
                tank1.x = tank1.x
        if hitTest(tank1.x, tank1.y, tank1.x+tank1.width, tank1.y+tank1.height, tank2.x, tank2.y, tank2.x+tank2.width, tank2.y+tank2.height) == True:
            if tank2.direct == 0:
                tank2.y = tank2.y
            elif tank2.direct == 1:
                tank2.x = tank2.x  
            elif tank2.direct == 2:
                tank2.y = tank2.y
            elif tank2.direct == 3:
                tank2.x = tank2.x  
                
        
        
        
    bulletsToDelete = []
        
    for bullet in bullets:
        pygame.draw.rect(screen, green, (bullet.x, bullet.y, bullet.width, bullet.height),1)
        if bullet.direct == 0:
            bullet.y -= bullet.speed
        elif bullet.direct == 2:
            bullet.y += bullet.speed
        elif bullet.direct == 3:
            bullet.x -= bullet.speed
        elif bullet.direct == 1:
            bullet.x += bullet.speed
        for block in blocks:    
            if (hitTest(bullet.x, bullet.y, bullet.x+bullet.width, bullet.y+bullet.height,block.x, block.y , block.x+block.width, block.y+block.height)):
                bulletsToDelete.append(bullet)
        
        
    for bullet in bulletsToDelete:
        bullets.remove(bullet)
    

           
    pygame.display.flip()
