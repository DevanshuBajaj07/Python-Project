
```markdown
# SharpShooter Game

SharpShooter is a classic arcade-style space shooter game built using Python and Pygame. Control your spaceship, shoot down enemies, and aim for the highest score while avoiding enemy advances. The game features dynamic enemy movement, collision detection, and sound effects for an immersive experience.

---

## Features

- **Player Movement**: Move the spaceship left and right to dodge enemies.
- **Shooting Mechanic**: Fire bullets to destroy enemies.
- **Dynamic Enemy Movement**: Enemies move horizontally and descend as they reach the screen edges.
- **Collision Detection**: Bullets destroy enemies on impact, and the score increases.
- **Game Over Condition**: The game ends when an enemy reaches the bottom of the screen.
- **Sound Effects**: Includes background music, laser firing, and explosion sounds.
- **Score Display**: Tracks and displays the player's score in real-time.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/sharpshooter-game.git
   cd sharpshooter-game
   ```

2. **Install Dependencies**:
   Ensure you have Python installed. Then, install Pygame:
   ```bash
   pip install pygame
   ```

3. **Run the Game**:
   ```bash
   python main.py
   ```

---

## How to Play

- **Controls**:
  - Use the **Left Arrow Key** (`←`) to move left.
  - Use the **Right Arrow Key** (`→`) to move right.
  - Press the **Spacebar** to shoot bullets.
- **Objective**:
  - Destroy as many enemies as possible to increase your score.
- **Game Over**:
  - The game ends if any enemy reaches the bottom of the screen.

---

## File Structure

```
SharpShooter/
├── SharpShooter/
│   ├── background.jpg         # Background image for the game
│   ├── background.wav         # Background music
│   ├── rocket.png             # Icon for the game window
│   ├── player.png             # Player spaceship image
│   ├── enemy.png              # Enemy spaceship image
│   ├── bullet.png             # Bullet image
│   ├── laser.wav              # Laser firing sound effect
│   ├── explosion.wav          # Explosion sound effect
├── main.py                    # Main Python script for the game
└── README.md                  # Project documentation
```

---

## Customization

### 1. **Change the Number of Enemies**:
Modify the `num_of_enemies` variable in `main.py` to increase or decrease the number of enemies:
```python
num_of_enemies = 6  # Change this value
```

### 2. **Adjust Enemy Speed**:
Modify the `enemyX_change` and `enemyY_change` values to adjust enemy movement speed:
```python
enemyX_change.append(4)  # Horizontal speed
enemyY_change.append(40)  # Vertical speed
```

### 3. **Change Bullet Speed**:
Modify the `bulletY_change` value to adjust the bullet's speed:
```python
bulletY_change = 10  # Bullet speed
```

### 4. **Change Background Music**:
Replace the `background.wav` file in the `SharpShooter` folder with your desired music file. Ensure the file name matches in the code:
```python
mixer.music.load("SharpShooter/background.wav")
```

---

## Requirements

- Python 3.7 or higher
- Pygame library

---

## Credits

- **Graphics**: Custom-designed spaceship, enemy, and bullet graphics.
- **Sound**: Background music, laser firing, and explosion sound effects.
- **Font**: Default Pygame font for score display.

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as you like.

---

Enjoy the game!
```
