# 🌌 Gravity Game (Neon Space Platformer)

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.x-orange?style=for-the-badge&logo=sdl&logoColor=white)](https://www.pygame.org/)
[![Status](https://img.shields.io/badge/Status-In%20Development-success?style=for-the-badge)]()

*A clean, physics-driven platformer built from scratch in Python with custom gravity mechanics and smooth collisions.*

</div>

---

## ⚡ About The Project

**Gravity Game** is a lightweight, high-performance 2D platformer built entirely without third-party AI physics frameworks. It features custom gravity simulation, velocity vectors, directional sprite handling, and dynamic platform collision detection in a deep-space aesthetic.

---

## 🛠️ Tech Stack & Architecture

* **Language:** Python 3.x
* **Graphics & Loop:** Pygame (`pygame.display`, `pygame.clock`)
* **Core Mechanics:** 
  * Custom gravitational acceleration (`GRAVITY`) and jump impulses (`JUMP_HEIGHT`).
  * Bounding-box collision detection with circular meteor platforms (`pygame.Rect` vs `colliderect`).
  * Procedural starfield generation using Python's `random` module.

---

## 🚀 Key Features

* **Physics Engine:** Real-time velocity tracking (`Y_VELOCITY`) with ground checks and instant vertical clamping upon landing.
* **Dynamic Sprite Flipping:** Smooth horizontal facing adjustment (`pygame.transform.flip`) depending on movement direction (`A`/`D` keys).
* **Atmospheric Environment:** Procedurally generated background starfield and celestial meteor platforms.
* **Auto-Respawn System:** Automatic position and velocity reset if the player falls off the bottom boundary of the screen.

---

## 📦 Quick Start & Installation

### Prerequisites
Make sure you have Python installed, then install Pygame:
```bash
pip install pygame
