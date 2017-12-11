# -*- coding: utf-8 -*-
import pygame
from GameObjects import Player, Missile, Enemy, Emissile, Star
import Logic


pygame.init()
BLACK = (0,0,0)

# Display resolution 
x=1024
y=768
# Game points
points = 0

gameDisplay = pygame.display.set_mode((x,y))
pygame.display.set_caption(u'Space Shooter')
pygame.display.update()
gameExit = False
# text and fonts
myfont = pygame.font.SysFont("monospace", 15)
mybiggerfont = pygame.font.SysFont("monospace", 30)
def banner(txt):
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    done=True
        gameDisplay.fill(BLACK)
        label = mybiggerfont.render(txt, 1, (255,255,0))
        ptnlab = mybiggerfont.render('points: '+str(points), 1, (255,255,0))
        gameDisplay.blit(label,(400,400))
        gameDisplay.blit(ptnlab,(400,450))
        
        pygame.display.update() # Display update
        clock.tick(30)    

        

# Game clock
clock = pygame.time.Clock()
# Player
player = Player()
player.rect.y = 690
player.rect.x=512
plgrp=pygame.sprite.Group()
plgrp.add(player)
# Missiles
misgrp=pygame.sprite.Group()
emisgrp=pygame.sprite.Group() 
# Enemies
enemygrp=pygame.sprite.Group()
enemy = Enemy()
enemy.rect.x=player.rect.x
enemygrp.add(enemy)
# stars in background
stargrp = pygame.sprite.Group()
# joystick
pygame.joystick.init() # to do - using pad in the game 



# życia
lives = 6 # 6 beaceuse one of then them is wasted in first iteration


lp = 0 #program counter

# main game loop
while  not gameExit:
    lp+=1
    star = Star()
    stargrp.add(star)

    plcollenemy = pygame.sprite.spritecollideany(player,enemygrp)
    plcollemissile =pygame.sprite.spritecollideany(player,emisgrp)
    if plcollenemy or plcollemissile:
        player.kill()
        emisgrp.empty()
        enemygrp.empty()
        banner('You are dead')
        lives -=1
        if lives >0:
            player = Player()
            player.rect.y = 690
            plgrp.add(player)
        else:
            banner('GAME OVER')
            gameExit=True
    for mis in misgrp.sprites():
        if mis.rect.y<=0:
            mis.kill()
        collider =pygame.sprite.spritecollideany(mis,enemygrp)
        if collider:
            coltype =str(type(collider))
            collider.kill()
            mis.kill()
            points+=10
            if 'Ufo' in coltype:
                lives+=1
        
    for en in enemygrp:
        if en.rect.y>y:
            en.kill()
        if en.shoot:
            emis = Emissile()
            emis.rect.x=en.rect.x+45
            emis.rect.y=en.rect.y+5
            en.shoot=False
            emisgrp.add(emis)
    enes = Logic.getStuff(lp)
    for e in enes:
        enemygrp.add(e)
    # reading events
    for event in pygame.event.get():
        # Chcecking if the window is closed
        if event.type == pygame.QUIT:
            gameExit=True
        # Moving player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if player.rect.x>0:
                    player.go_left()
            if event.key == pygame.K_RIGHT:
                if player.rect.x<x:
                    player.go_right()
            if event.key==pygame.K_UP:
                player.go_up()
            if event.key==pygame.K_DOWN:
                player.go_down()
            if event.key == pygame.K_SPACE:
                missile = Missile()
                missile.rect.y=player.rect.y
                missile.rect.x=player.rect.x+45
                misgrp.add(missile)
            if event.key == pygame.K_1:
                banner('pause')
        if event.type == pygame.KEYUP: # Checking if button is pressed
            if not player.state=='dead':
                player.idle()
    
    gameDisplay.fill(BLACK)
    label = myfont.render("PC:"+str(lp)+" points: "+str(points)+" lives: "+str(lives), 1, (255,255,0))
    gameDisplay.blit(label,(10,10))
    stargrp.update()
    stargrp.draw(gameDisplay)
    plgrp.update()
    plgrp.draw(gameDisplay)
    misgrp.update()
    misgrp.draw(gameDisplay)
    enemygrp.update()
    emisgrp.update()
    enemygrp.draw(gameDisplay)
    emisgrp.draw(gameDisplay)
    pygame.display.update() #aktualizujemy ekran
    clock.tick(30)    
# leaving app
pygame.quit()
quit()
