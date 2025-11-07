import pygame
import random
import math
from pygame import mixer

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

#background
background = pygame.image.load("SharpShooter/background.jpg")

#background Sound
mixer.music.load("SharpShooter/background.wav")
mixer.music.play(-1)

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("SharpShooter/rocket.png")
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load("SharpShooter/player.png")
playerX = 370
playerY = 530
playerX_change = 0

#enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    
    enemyImg.append(pygame.image.load("SharpShooter/enemy.png"))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(15,150))
    enemyX_change.append(4)
    enemyY_change.append(40)

#bullet
# Ready state means you cant see bullet on screen
#Fire - The bullet is currently moving
bulletImg = pygame.image.load("SharpShooter/bullet.png")
bulletX = 0
bulletY = 530
bulletyX_change = 0
bulletY_change = 10
bullet_state = "ready"

#score

score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)

textX = 10
textY = 10

def player(x,y):
    screen.blit(playerImg,(x,y))
    
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
    
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x + 16,y + 10))
    
def is_collision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2)) + (math.pow(enemyY - bulletY,2))
    if distance < 27:
        return True
    else:
        return False
    
def show_score(x,y):
    score = font.render("Score : " + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
    
    
#game loop
while running:
   
    screen.fill((0,0,0))
    #background image
    screen.blit(background,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= 5
                
            if event.key == pygame.K_RIGHT:
                playerX_change += 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound("SharpShooter/laser.wav")
                    bullet_sound.play()
                    # get the current x-coordinate of the spaceship.
                    bulletX = playerX
                    
                    fire_bullet(playerX,bulletY)
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                 playerX_change = 0
             
            
    #checking for boundaries of spaceship so it doesnt go out of bounds
    playerX += playerX_change
    
    if playerX <= 0:
        playerX = 0
    elif playerX >=736:
        playerX = 736
        
    # enemy movements
    for i in range(num_of_enemies):
        
        enemyX[i] += enemyX_change[i]
        
        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >=736:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]
            
        #collision
        collision = is_collision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            explosion_sound = mixer.Sound("SharpShooter/explosion.wav")
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(15,150)
            
        enemy(enemyX[i],enemyY[i],i)
            
    #Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
        
   
        
    player(playerX,playerY)
    show_score(textX,textY)
    
    pygame.display.update()
    clock.tick(60)  # limits FPS to 60

pygame.quit()