
```markdown
# Snake Game

A modern take on the classic Snake game, built using Python and Pygame. Navigate the snake to eat apples, grow longer, and avoid collisions with the walls or itself. The game features smooth animations, custom graphics, and sound effects for an engaging experience.

---

## Features

- **Smooth Gameplay**: The snake moves seamlessly on a grid-based system.
- **Dynamic Growth**: The snake grows longer as it eats apples.
- **Custom Graphics**: Includes custom-designed graphics for the snake's head, body, tail, and apples.
- **Sound Effects**: Plays a crunch sound when the snake eats an apple.
- **Score Display**: Tracks and displays the player's score in real-time.
- **Game Over Logic**: The game resets when the snake collides with itself or the walls.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/snake-game.git
   cd snake-game
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
  - Use the **Arrow Keys** (`↑`, `↓`, `←`, `→`) to move the snake.
- **Objective**:
  - Eat as many apples as possible to grow the snake and increase your score.
- **Game Over**:
  - The game ends if the snake collides with the walls or itself.

---

## File Structure

```
Snake Game/
├── Graphics/
│   ├── head_up.png
│   ├── head_down.png
│   ├── head_left.png
│   ├── head_right.png
│   ├── tail_up.png
│   ├── tail_down.png
│   ├── tail_left.png
│   ├── tail_right.png
│   ├── body_vertical.png
│   ├── body_horizontal.png
│   ├── body_tr.png
│   ├── body_tl.png
│   ├── body_br.png
│   ├── body_bl.png
│   └── apple.png
├── Sound/
│   └── crunch.wav
├── Font/
│   └── PoetsenOne-Regular.ttf
├── main.py
└── README.md
```

---

## Customization

### 1. **Change the Grid Size**:
Modify the `cell_size` and `cell_number` variables in `main.py` to adjust the grid size:
```python
cell_size = 40  # Size of each grid cell
cell_number = 20  # Number of cells in each row/column
```

### 2. **Adjust Game Speed**:
Modify the `pygame.time.set_timer` value to change the snake's speed:
```python
pygame.time.set_timer(SCRENN_UPDATE, 150)  # Lower value = faster snake
```

### 3. **Add More Apples**:
To add multiple apples on the screen, modify the `FRUIT` class to handle multiple fruit positions.

---

## Requirements

- Python 3.7 or higher
- Pygame library

---

## Credits

- **Graphics**: Custom-designed snake and apple graphics.
- **Sound**: Crunch sound effect for eating apples.
- **Font**: [PoetsenOne](https://fonts.google.com/specimen/PoetsenOne).

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as you like.

---


Enjoy playing the Snake Game!
