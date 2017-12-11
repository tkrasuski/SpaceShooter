import pygame
import os
import random
BLACK = (0,0,0)

class Player(pygame.sprite.Sprite):
    def __init__(self, color=BLACK, width=99, height=75):
       super(Player,self).__init__()
       self.center_img=pygame.image.load(os.path.join('png','player.png')).convert_alpha()
       self.image = self.center_img
       self.left_img = pygame.image.load(os.path.join('png','playerLeft.png')).convert_alpha()
       self.right_img = pygame.image.load(os.path.join('png','playerRight.png')).convert_alpha()
       self.rect = self.image.get_rect()
       self.state='idle'
    def update(self):
        if self.state == 'idle':
            self.image=self.center_img
        if self.state=='left':
            self.image=self.left_img
            self.rect.x-=10
        if self.state=='right':
            self.image=self.right_img
            self.rect.x+=10
        if self.state=='up':
            if self.rect.y>100:
                self.rect.y-=10
        if self.state=='down':
            if self.rect.y<=690:
                self.rect.y+=10
    def idle(self):
        self.state='idle'
    def go_left(self):
        self.state='left'
    def go_right(self):        
        self.state='right'
    def go_up(self):
        self.state='up'
    def go_down(self):
        self.state='down'
    def attack(self):
        self.state = 'attack'
    def dead(self):
        self.state='dead'

class Missile(pygame.sprite.Sprite):
    def __init__(self, color=BLACK, width=99, height=75):
        super(Missile,self).__init__()
        self.image=self.center_img=pygame.image.load(os.path.join('png','laserGreen.png')).convert_alpha()
        self.rect = self.image.get_rect()
    def update(self):
        if self.rect.y>0:
            self.rect.y-=20
class Emissile(pygame.sprite.Sprite):
    def __init__(self, color=BLACK, width=99, height=75):
        super(Emissile,self).__init__()
        self.image=self.center_img=pygame.image.load(os.path.join('png','laserRed.png')).convert_alpha()
        self.rect = self.image.get_rect()
    def update(self):
        if self.rect.y<768:
            self.rect.y+=10
class Enemy(pygame.sprite.Sprite):
    def __init__(self, color=BLACK, width=99, height=75):
        super(Enemy,self).__init__()
        self.image=self.center_img=pygame.image.load(os.path.join('png','enemyShip.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.cntr = 0
        self.shoot = False
    def update(self):
        self.rect.y+=1
        if self.cntr%7==0 and self.cntr%10==0:
            self.shoot=True
        self.cntr+=1
        #print self.cntr

class Rock(pygame.sprite.Sprite):
    def __init__(self, color=BLACK, width=44, height=42):
        super(Rock,self).__init__()
        self.image=pygame.image.load(os.path.join('png','meteorSmall.png')).convert_alpha()
        self.rect=self.image.get_rect()
        self.cntr = 0
        self.rect.y=0
        self.rect.x=random.randint(0,1024)
        self.direction = random.randint(1,3)
        self.shoot=False
    def update(self):
        if self.rect.y>768:
            self.kill()
        if self.rect.x<0:
            self.kill()
        if self.rect.x>1024:
            self.kill()
        self.rect.y+=3
        if self.direction==1:
            self.rect.x+=1
        elif self.direction==3:
            self.rect.x-=1
class Ufo(pygame.sprite.Sprite):
    def __init__(self, color=BLACK, width=91, height=91):
        super(Ufo,self).__init__()
        self.image=pygame.image.load(os.path.join('png','enemyUFO.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,900)
        self.shoot=False
        self.cntr=0
        self.direction=2
    def update(self):
        if self.cntr>500:
            self.kill()
        if self.cntr%7==0 and self.cntr%10==0:
            self.shoot=True
        self.cntr+=1
        if self.rect.y<400:
            self.rect.y+=5
        else:
            if self.direction==2:
                self.direction=3
            if self.rect.x<0:
                self.direction=1
            if self.rect.x>900:
                self.direction=3
            if self.direction==1:
                self.rect.x+=10
            if self.direction==3:
                self.rect.x-=10
        
class Star(pygame.sprite.Sprite):
    def __init__(self, color=BLACK, width=11, height=11):
        super(Star,self).__init__()
        self.image=pygame.image.load(os.path.join('png','starSmall.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,1024)
        self.rect.y = random.randint(0,765)
        
    def update(self):
        self.rect.y+=5
        if self.rect.y>768:
            self.kill()
