import pygame
import random
import math
from pygame import mixer

# Initialize pygame
pygame.init()

# Set up the game screen
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# Load the background image
background = pygame.image.load("SharpShooter/background.jpg")

# Load and play background music
mixer.music.load("SharpShooter/background.wav")
mixer.music.play(-1)

# Set up the game window title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("SharpShooter/rocket.png")
pygame.display.set_icon(icon)

# Load player image and initialize its position
playerImg = pygame.image.load("SharpShooter/player.png")
playerX = 370
playerY = 530
playerX_change = 0

# Load enemy images and initialize their positions and movements
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("SharpShooter/enemy.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(15, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Load bullet image and initialize its state
# "ready" means the bullet is not visible on the screen
# "fire" means the bullet is currently moving
bulletImg = pygame.image.load("SharpShooter/bullet.png")
bulletX = 0
bulletY = 530
bulletyX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Initialize score and fonts
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10
over_font = pygame.font.Font("freesansbold.ttf", 64)

# Function to draw the player on the screen
def player(x, y):
    screen.blit(playerImg, (x, y))

# Function to draw an enemy on the screen
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

# Function to fire a bullet
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

# Function to check for collision between a bullet and an enemy
def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False

# Function to display the score on the screen
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

# Function to display the "Game Over" text
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 200))

# Game loop
while running:
    # Fill the screen with black color
    screen.fill((0, 0, 0))
    # Draw the background image
    screen.blit(background, (0, 0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= 5
            if event.key == pygame.K_RIGHT:
                playerX_change += 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    # Play bullet firing sound
                    bullet_sound = mixer.Sound("SharpShooter/laser.wav")
                    bullet_sound.play()
                    # Get the current x-coordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)

        # Check for key releases
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Update player position and prevent it from going out of bounds
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Update enemy positions
    for i in range(num_of_enemies):
        # Check for game over condition
        if enemyY[i] > 500:
            for j in range(num_of_enemies):
                enemyY[j] = 2000  # Move enemies off-screen
            game_over_text()
            break

        # Move the enemy
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]

        # Check for collision between bullet and enemy
        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            # Play explosion sound
            explosion_sound = mixer.Sound("SharpShooter/explosion.wav")
            explosion_sound.play()
            # Reset bullet and enemy positions
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(15, 150)

        # Draw the enemy
        enemy(enemyX[i], enemyY[i], i)

    # Update bullet position
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Draw the player and display the score
    player(playerX, playerY)
    show_score(textX, textY)

    # Update the display and limit the frame rate
    pygame.display.update()
    clock.tick(60)

# Quit pygame
pygame.quit()