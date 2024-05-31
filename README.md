
# Pygame Collisions Tutorial

This repository contains the code for a video tutorial on creating a simple collision detection system using Pygame in Python.

## Overview

In this tutorial, we build a basic Pygame application that demonstrates collision detection between a player-controlled character (Dino) and an obstacle. The tutorial covers setting up the Pygame window, updating the character's position, detecting collisions, and visually representing the collision state.

## Features

- **Pygame Window Setup:** Initialize a Pygame window with a specified width and height.
- **Dino Character:** A player-controlled character that can move and interact with obstacles.
- **Obstacle:** A static rectangular obstacle positioned within the game window.
- **Collision Detection:** Real-time detection of collisions between the Dino and the obstacle.
- **Visual Feedback:** Visual representation of the obstacle and collision state.

## Code Structure

- **main.py:** The main script that initializes the Pygame window, handles events, updates the Dino's position, checks for collisions, and renders the game objects.
- **dino.py:** A separate module containing the `Dino` class, which manages the character's position, rendering, and collision detection.

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/pygame-collisions-tutorial.git
   cd pygame-collisions-tutorial
   ```

2. Ensure you have Python and Pygame installed. You can install Pygame using pip:
   ```bash
   pip install pygame
   ```

3. Run the `main.py` script:
   ```bash
   python main.py
   ```

## Usage

- Run the script and a window titled "Pygame collisions" will appear.
- The `Dino` character will automatically move and interact with the obstacle.
- The obstacle is drawn as a black rectangle.
- If a collision occurs, visual feedback will be provided.

## Dependencies

- Python 3.x
- Pygame

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.
