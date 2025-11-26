import random
import pygame
from pathlib import Path
from dataclasses import dataclass, field
from bot_ai import SimpleCatchBot

# ----------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------
USE_BOT_DEFAULT = True  # start with bot playing; you can change to False


WIDTH, HEIGHT = 800, 600
FPS = 60
PLAYER = {'w': 80, 'h': 20, 'color': (50, 200, 255), 'speed': 7}
OBJECT = {
    'size': 30,
    'good': (255, 200, 50),
    'bad': (255, 50, 50),
    'bonus': (50, 255, 100),
    'slow': (100, 100, 255),
    'double': (255, 100, 200),
}
SOUND_PATH = Path('assets/sounds')
HIGH_SCORE_FILE = Path('highscore.txt')


# ----------------------------------------------------------------------
# Helper functions
# ----------------------------------------------------------------------
def load_sound(name, volume=0.5):
    path = SOUND_PATH / f'{name}.wav'
    if path.exists():
        s = pygame.mixer.Sound(str(path))
        s.set_volume(volume)
        return s
    return None


def load_high_score():
    if HIGH_SCORE_FILE.exists():
        try:
            return int(HIGH_SCORE_FILE.read_text())
        except ValueError:
            return 0
    return 0


def save_high_score(score):
    HIGH_SCORE_FILE.write_text(str(score))


# ----------------------------------------------------------------------
# Data classes
# ----------------------------------------------------------------------
@dataclass
class Particle:
    x: float
    y: float
    vx: float = field(default_factory=lambda: random.uniform(-3, 3))
    vy: float = field(default_factory=lambda: random.uniform(-5, -2))
    color: tuple = (255, 255, 255)
    lifetime: int = 30
    size: int = field(default_factory=lambda: random.randint(3, 6))

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.2
        self.lifetime -= 1

    def draw(self, surface):
        alpha = max(0, int(self.lifetime / 30 * 255))
        s = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
        pygame.draw.circle(s, (*self.color, alpha), (self.size, self.size), self.size)
        surface.blit(s, (self.x - self.size, self.y - self.size))


@dataclass
class FallingObject:
    x: float
    y: float
    obj_type: str = 'good'   # good, bad, bonus, slow, double
    speed: float = 4.0

    def __post_init__(self):
        self.size = OBJECT['size']
        if self.obj_type in ('slow', 'double'):
            self.size -= 10  # just a visual variation

    def update(self):
        self.y += self.speed

    def draw(self, surface):
        center = (self.x + self.size // 2, self.y + self.size // 2)
        if self.obj_type == 'good':
            color = OBJECT['good']
            pygame.draw.rect(surface, color, (self.x, self.y, self.size, self.size))
            pygame.draw.circle(surface, (255, 255, 200), center, self.size // 4)
        elif self.obj_type == 'bad':
            color = OBJECT['bad']
            pygame.draw.rect(surface, color, (self.x, self.y, self.size, self.size))
            pygame.draw.line(
                surface, (255, 255, 255),
                (self.x + 5, self.y + 5),
                (self.x + self.size - 5, self.y + self.size - 5), 3
            )
            pygame.draw.line(
                surface, (255, 255, 255),
                (self.x + self.size - 5, self.y + 5),
                (self.x + 5, self.y + self.size - 5), 3
            )
        elif self.obj_type == 'bonus':
            color = OBJECT['bonus']
            pygame.draw.circle(surface, color, center, self.size // 2)
            pygame.draw.circle(surface, (255, 255, 255), center, self.size // 4)
        elif self.obj_type == 'slow':
            color = OBJECT['slow']
            pygame.draw.rect(surface, color, (self.x, self.y, self.size, self.size))
        elif self.obj_type == 'double':
            color = OBJECT['double']
            pygame.draw.rect(surface, color, (self.x, self.y, self.size, self.size))

    def rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)


# ----------------------------------------------------------------------
# Game states
# ----------------------------------------------------------------------
class State:
    SPLASH = 'splash'
    PLAYING = 'playing'
    PAUSED = 'paused'
    GAME_OVER = 'game_over'


# ----------------------------------------------------------------------
# Main Game class
# ----------------------------------------------------------------------
class CatchGame:
    def __init__(self):
        pygame.init()

        # Try to init mixer safely
        self.mixer_ok = True
        try:
            pygame.mixer.init()
        except pygame.error:
            self.mixer_ok = False

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Catch the Falling Objects")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 48)
        self.small_font = pygame.font.SysFont(None, 32)

        # Load sounds (only if mixer available)
        if self.mixer_ok:
            self.sounds = {
                'catch': load_sound('catch'),
                'miss': load_sound('miss'),
                'bonus': load_sound('bonus'),
                'life_lost': load_sound('life_lost'),
            }
        else:
            self.sounds = {}
        
        # Bot setup
        self.bot = SimpleCatchBot(deadzone=5)
        self.use_bot = USE_BOT_DEFAULT


        # Game variables
        self.state = State.SPLASH
        self.reset_game_variables()
        self.high_score = load_high_score()

    def reset_game_variables(self):
        self.player_x = WIDTH // 2 - PLAYER['w'] // 2
        self.player_y = HEIGHT - PLAYER['h'] - 20
        self.objects = []
        self.particles = []
        self.score = 0
        self.lives = 3
        self.level = 1
        self.base_speed = 4.0
        self.spawn_timer = 0
        self.spawn_rate = 60  # frames between spawns
        self.power_up_active = False
        self.power_up_timer = 0

    # ------------------------------------------------------------------
    # Main loop
    # ------------------------------------------------------------------
    def run(self):
        running = True
        while running:
            self.handle_events()
            if self.state == State.PLAYING:
                self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(FPS)
        pygame.quit()

    # ------------------------------------------------------------------
    # Event handling
    # ------------------------------------------------------------------
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.toggle_pause()
                    
                if event.key == pygame.K_b:
                    # toggle bot on/off
                    self.use_bot = not self.use_bot
                    
                        
                if self.state == State.SPLASH and event.key == pygame.K_SPACE:
                    self.state = State.PLAYING
                if self.state == State.GAME_OVER:
                    if event.key == pygame.K_r:
                        self.reset_game_variables()
                        self.state = State.PLAYING
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        raise SystemExit

    def toggle_pause(self):
        if self.state == State.PLAYING:
            self.state = State.PAUSED
        elif self.state == State.PAUSED:
            self.state = State.PLAYING

    # ------------------------------------------------------------------
    # Update logic
    # ------------------------------------------------------------------
    def update(self):
        # Player movement: bot or human
        if self.use_bot:
            direction = self.bot.decide(
                player_x=self.player_x,
                player_width=PLAYER['w'],
                objects=self.objects,
                screen_width=WIDTH,
            )
            # direction is -1, 0, or +1
            self.player_x += direction * PLAYER['speed']
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.player_x -= PLAYER['speed']
            if keys[pygame.K_RIGHT]:
                self.player_x += PLAYER['speed']

        # Clamp to screen bounds
        self.player_x = max(0, min(self.player_x, WIDTH - PLAYER['w']))

        # Spawn objects
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_rate:
            self.objects.append(self.spawn_object())
            self.spawn_timer = 0

        # Update objects
        player_rect = pygame.Rect(self.player_x, self.player_y, PLAYER['w'], PLAYER['h'])
        for obj in self.objects[:]:
            obj.update()
            if player_rect.colliderect(obj.rect()):
                self.handle_collision(obj)
                self.objects.remove(obj)
            elif obj.y > HEIGHT:
                if obj.obj_type == 'good':
                    self.lives -= 1
                    self.play_sound('miss')
                    if self.lives <= 0:
                        self.state = State.GAME_OVER
                self.objects.remove(obj)

        # Update particles
        for p in self.particles[:]:
            p.update()
            if p.lifetime <= 0:
                self.particles.remove(p)

        # Level progression
        new_level = self.score // 100 + 1
        if new_level > self.level:
            self.level = new_level
            self.spawn_rate = max(20, 60 - (self.level - 1) * 5)
            self.base_speed += 0.5

        # Power-up timer
        if self.power_up_active:
            self.power_up_timer -= 1
            if self.power_up_timer <= 0:
                self.power_up_active = False

    def handle_collision(self, obj: FallingObject):
        cx = obj.x + obj.size // 2
        cy = obj.y + obj.size // 2

        if obj.obj_type == 'good':
            self.score += 10
            self.play_sound('catch')
            for _ in range(10):
                self.particles.append(
                    Particle(cx, cy, color=OBJECT['good'])
                )

        elif obj.obj_type == 'bad':
            self.lives -= 1
            self.play_sound('miss')
            for _ in range(10):
                self.particles.append(
                    Particle(cx, cy, color=OBJECT['bad'])
                )
            if self.lives <= 0:
                self.state = State.GAME_OVER

        elif obj.obj_type == 'bonus':
            self.score += 50
            self.play_sound('bonus')
            for _ in range(15):
                self.particles.append(
                    Particle(cx, cy, color=OBJECT['bonus'])
                )

        elif obj.obj_type == 'slow':
            # temporarily slow things down
            self.base_speed = max(1.0, self.base_speed - 1.5)
            self.power_up_timer = FPS * 10  # 10 seconds
            self.power_up_active = True

        elif obj.obj_type == 'double':
            # simple double-score pickup
            self.score += 20
            self.power_up_timer = FPS * 10
            self.power_up_active = True

    def play_sound(self, name):
        s = self.sounds.get(name)
        if s:
            s.play()

    # ------------------------------------------------------------------
    # Drawing
    # ------------------------------------------------------------------
    def draw(self):
        self.screen.fill((10, 10, 30))
        self.draw_grid()
        self.draw_player()
        for obj in self.objects:
            obj.draw(self.screen)
        for p in self.particles:
            p.draw(self.screen)
        self.draw_ui()

        if self.state == State.SPLASH:
            self.draw_splash()
        elif self.state == State.PAUSED:
            self.draw_paused()
        elif self.state == State.GAME_OVER:
            self.draw_game_over()

    def draw_grid(self):
        for i in range(0, WIDTH, 40):
            pygame.draw.line(self.screen, (20, 20, 50), (i, 0), (i, HEIGHT))
        for i in range(0, HEIGHT, 40):
            pygame.draw.line(self.screen, (20, 20, 50), (0, i), (WIDTH, i))

    def draw_player(self):
        pygame.draw.rect(
            self.screen,
            PLAYER['color'],
            (self.player_x, self.player_y, PLAYER['w'], PLAYER['h']),
        )
        # little highlight
        pygame.draw.rect(
            self.screen,
            (100, 230, 255),
            (self.player_x, self.player_y, PLAYER['w'], PLAYER['h'] // 2),
        )
        pygame.draw.rect(
            self.screen,
            (255, 255, 255),
            (self.player_x, self.player_y, PLAYER['w'], 3),
        )

    def draw_ui(self):
        score_s = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        level_s = self.small_font.render(f"Level: {self.level}", True, (255, 255, 255))
        lives_s = self.font.render(f"Lives: {self.lives}", True, (255, 100, 100))
        high_s = self.small_font.render(f"High: {self.high_score}", True, (200, 200, 200))

        self.screen.blit(score_s, (10, 10))
        self.screen.blit(level_s, (10, 60))
        self.screen.blit(lives_s, (WIDTH - 150, 10))
        self.screen.blit(high_s, (WIDTH - 150, 50))

        if self.power_up_active:
            power_s = self.small_font.render("POWER-UP!", True, (255, 255, 0))
            self.screen.blit(
                power_s,
                (WIDTH // 2 - power_s.get_width() // 2, 10),
            )

    def draw_splash(self):
        splash_s = self.font.render(
            "Catch the Falling Objects", True, (255, 255, 255)
        )
        instr_s = self.small_font.render(
            "Press SPACE to start", True, (200, 200, 200)
        )
        self.screen.blit(
            splash_s,
            (WIDTH // 2 - splash_s.get_width() // 2, HEIGHT // 2 - 30),
        )
        self.screen.blit(
            instr_s,
            (WIDTH // 2 - instr_s.get_width() // 2, HEIGHT // 2 + 10),
        )

    def draw_paused(self):
        pause_s = self.font.render("PAUSED", True, (255, 255, 255))
        self.screen.blit(
            pause_s,
            (WIDTH // 2 - pause_s.get_width() // 2, HEIGHT // 2),
        )

    def draw_game_over(self):
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.screen.blit(overlay, (0, 0))

        over_s = self.font.render("GAME OVER", True, (255, 50, 50))
        final_s = self.font.render(
            f"Final Score: {self.score}", True, (255, 255, 255)
        )
        restart_s = self.small_font.render(
            "Press R to Restart or Q to Quit", True, (200, 200, 200)
        )

        self.screen.blit(
            over_s,
            (WIDTH // 2 - over_s.get_width() // 2, HEIGHT // 2 - 60),
        )
        self.screen.blit(
            final_s,
            (WIDTH // 2 - final_s.get_width() // 2, HEIGHT // 2),
        )
        self.screen.blit(
            restart_s,
            (WIDTH // 2 - restart_s.get_width() // 2, HEIGHT // 2 + 60),
        )

        if self.score > self.high_score:
            self.high_score = self.score
            save_high_score(self.high_score)

    # ------------------------------------------------------------------
    # Object spawning
    # ------------------------------------------------------------------
    def spawn_object(self):
        x = random.randint(0, WIDTH - OBJECT['size'])
        rand = random.random()
        if rand < 0.70:
            obj_type = 'good'
        elif rand < 0.90:
            obj_type = 'bad'
        elif rand < 0.95:
            obj_type = 'bonus'
        elif rand < 0.975:
            obj_type = 'slow'
        else:
            obj_type = 'double'
        return FallingObject(x, -OBJECT['size'], obj_type, self.base_speed)


# ----------------------------------------------------------------------
# Entry point
# ----------------------------------------------------------------------
if __name__ == "__main__":
    game = CatchGame()
    game.run()
