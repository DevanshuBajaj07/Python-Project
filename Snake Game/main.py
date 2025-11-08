import pygame
import math
import random
import sys
from pygame.math import Vector2

# Snake class to handle snake behavior and graphics
class SNAKE:
    def __init__(self):
        # Initialize the snake's body, direction, and other attributes
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.new_block = False
        
        # Load graphics for the snake's head, tail, and body
        self.head_up = pygame.image.load('Snake Game/Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Snake Game/Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Snake Game/Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Snake Game/Graphics/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('Snake Game/Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Snake Game/Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Snake Game/Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Snake Game/Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Snake Game/Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Snake Game/Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Snake Game/Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Snake Game/Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Snake Game/Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Snake Game/Graphics/body_bl.png').convert_alpha()

        # Load sound for eating fruit
        self.crunch_sound = pygame.mixer.Sound('Snake Game/Sound/crunch.wav')
        
    # Draw the snake on the screen
    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            # Draw the head, tail, or body based on the block's position
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    # Determine the corner graphics for the body
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)

    # Update the graphics for the snake's head based on its direction
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down

    # Update the graphics for the snake's tail based on its direction
    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down
            
    # Move the snake in the current direction
    def move_snake(self):
        if self.new_block == True:  
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            
    # Add a new block to the snake's body
    def add_block(self):
        self.new_block = True
        
    # Play the crunch sound when the snake eats a fruit
    def play_crunch_sound(self):
        self.crunch_sound.play()
        
    # Reset the snake to its initial state
    def reset(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)    

# Fruit class to handle fruit behavior and graphics
class FRUIT:
    def __init__(self):
        self.randomize()
        
    # Draw the fruit on the screen
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        screen.blit(apple, fruit_rect)
        
    # Randomize the fruit's position
    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

# Main game class to handle game logic and rendering
class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
    
    # Update the game state
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        
    # Draw all game elements
    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake() 
        self.draw_score()
        
    # Check for collisions between the snake and the fruit
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()
            
        # Ensure the fruit does not spawn on the snake's body
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()
            
    # Check if the snake has collided with the wall or itself
    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
            
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
                
    # Draw the grass pattern on the screen
    def draw_grass(self):
        grass_color = (167,209,61)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
                
    # Draw the score on the screen
    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56,74,12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 7, apple_rect.height)
        
        pygame.draw.rect(screen, (167,209,61), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)
        pygame.draw.rect(screen, (56,74,12), bg_rect, 2)
         
    # Handle game over logic
    def game_over(self):
        self.snake.reset()
        
# Initialize the mixer for sound
pygame.mixer.pre_init(44100, -16, 2, 512)
        
# Initialize pygame
pygame.init()

# Set up the grid size and cell size
cell_size = 40
cell_number = 20

# Set up the display
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
pygame.display.set_caption("Snake Game")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Load assets
apple = pygame.image.load("Snake Game/apple.png").convert_alpha()
game_font = pygame.font.Font("Snake Game/Font/PoetsenOne-Regular.ttf", 25)

# Set up a custom event for screen updates
SCRENN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCRENN_UPDATE, 150)

# Create the main game object
main_game = MAIN()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == SCRENN_UPDATE:
            main_game.update()
            
        if event.type == pygame.KEYDOWN:
            # Handle snake movement based on arrow key input
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
                
    # Fill the screen with a background color
    screen.fill((175,215,70))
    
    # Draw all game elements
    main_game.draw_elements()
    
    # Update the display
    pygame.display.flip()
    
    # Limit the frame rate
    clock.tick(60)

# Quit pygame and exit the program
pygame.quit()
sys.exit()