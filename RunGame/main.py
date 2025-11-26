import pygame

# ----------------------------
# Setup
# ----------------------------
pygame.init()

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Runner")
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont(None, 36)

# ----------------------------
# Constants
# ----------------------------
BG_COLOR = (20, 20, 20)
GROUND_COLOR = (200, 200, 200)
GROUND_Y = 300  # y-position of ground line

# Dino settings
DINO_WIDTH = 40
DINO_HEIGHT = 60
DINO_COLOR = (100, 255, 100)
DINO_X = 100  # fixed x position

GRAVITY = 0.8
JUMP_STRENGTH = -15

# Cactus settings
CACTUS_WIDTH = 30
CACTUS_HEIGHT = 50
CACTUS_COLOR = (0, 200, 0)
CACTUS_SPEED = 6

# ----------------------------
# Game state variables
# ----------------------------
dino_y = GROUND_Y - DINO_HEIGHT
dino_vel_y = 0

cactus_x = WIDTH
cactus_y = GROUND_Y - CACTUS_HEIGHT

score = 0
game_over = False


# ----------------------------
# Helper draw functions
# ----------------------------
def draw_dino():
    pygame.draw.rect(
        screen,
        DINO_COLOR,
        (DINO_X, dino_y, DINO_WIDTH, DINO_HEIGHT)
    )


def draw_cactus():
    pygame.draw.rect(
        screen,
        CACTUS_COLOR,
        (cactus_x, cactus_y, CACTUS_WIDTH, CACTUS_HEIGHT)
    )


def draw_ground():
    pygame.draw.line(
        screen,
        GROUND_COLOR,
        (0, GROUND_Y),
        (WIDTH, GROUND_Y),
        3
    )


# ----------------------------
# Main loop
# ----------------------------
running = True
while running:

    # --- Event handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # Jump (only if not game over and on ground)
            if event.key == pygame.K_SPACE and not game_over:
                if dino_y >= GROUND_Y - DINO_HEIGHT:
                    dino_vel_y = JUMP_STRENGTH

            # Restart when game over
            if event.key == pygame.K_r and game_over:
                dino_y = GROUND_Y - DINO_HEIGHT
                dino_vel_y = 0
                cactus_x = WIDTH
                score = 0
                game_over = False

    # --- Update logic ---
    if not game_over:
        # Dino physics
        dino_vel_y += GRAVITY
        dino_y += dino_vel_y

        # Stop at ground
        if dino_y > GROUND_Y - DINO_HEIGHT:
            dino_y = GROUND_Y - DINO_HEIGHT
            dino_vel_y = 0

        # Cactus movement
        cactus_x -= CACTUS_SPEED
        if cactus_x < -CACTUS_WIDTH:
            cactus_x = WIDTH

        # Collision detection
        dino_rect = pygame.Rect(DINO_X, dino_y, DINO_WIDTH, DINO_HEIGHT)
        cactus_rect = pygame.Rect(cactus_x, cactus_y, CACTUS_WIDTH, CACTUS_HEIGHT)

        if dino_rect.colliderect(cactus_rect):
            game_over = True

        # Score (1 per frame)
        score += 1

    # --- Drawing ---
    screen.fill(BG_COLOR)

    draw_ground()
    draw_dino()
    draw_cactus()

    # Score
    score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_surface, (10, 10))

    # Game over text
    if game_over:
        text = font.render("GAME OVER - Press R to restart", True, (255, 80, 80))
        screen.blit(
            text,
            (WIDTH // 2 - text.get_width() // 2,
             HEIGHT // 2 - text.get_height() // 2),
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
