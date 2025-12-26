# 🚀 MAGIC BUBBLE SORTER
### *An Interactive Puzzle Game for Sorting Colored Liquids*

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-000000?style=for-the-badge&logo=pygame&logoColor=white)](https://www.pygame.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

**MAGIC BUBBLE SORTER** is a **fun and colorful puzzle game** built with **Python** and **Pygame**.  
Players sort colored liquids in tubes by moving blocks from one tube to another until each tube contains only a single color.

---

## 📖 Overview
The game challenges players with **increasing levels of difficulty**. Each level adds more tubes, making the puzzle progressively harder. The game features:
- Animated and colorful tube blocks
- Click-to-select and move colors
- Restart or generate new boards anytime
- Victory detection for perfect sorting

---

## 🎯 Objective
Sort all colored blocks so that every tube contains **only one color**. Use **strategy and planning** to move blocks efficiently across tubes.

---

## 🏗️ Game Mechanics
1. **Select a tube** by clicking on it.  
2. **Select a destination tube** to move the top block or stack of same-colored blocks.  
3. Legal moves:
   - Move a block onto an empty tube
   - Move a block onto another block of the **same color**  
4. **Victory** is achieved when all tubes are sorted.

---

## ✨ Features
- **Multiple Levels:** Difficulty increases with more tubes.  
- **Colorful Gradient Backgrounds:** Makes gameplay visually appealing.  
- **Intuitive Controls:** Mouse-based selection, easy-to-understand interactions.  
- **Restart and New Board Options:** Spacebar to restart, Enter to generate new board or next level.  

---

## 🛠️ Technical Stack

| Layer        | Technology / Library | Key Implementation Details |
|-------------|--------------------|----------------------------|
| **Language** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) Python 3.7+ | Core logic, event handling, game loop |
| **Graphics** | ![Pygame](https://img.shields.io/badge/Pygame-000000?style=flat&logo=pygame&logoColor=white) Pygame 2.x | Handles rendering, mouse events, colors, and display updates |

---

## 📂 Project Structure
```text
MAGIC_BUBBLE_SORTER/
├── magic_sort.py       
├── README.md           
└── assets/
```
---
## Prerequisites

- **Python** version **3.7 or higher**
- **Pygame** version **2.x**

### Install Pygame

Use `pip` to install Pygame:

```bash
pip install pygame
