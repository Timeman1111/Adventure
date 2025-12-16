# Koya Kingdom - Text Adventure Game

Welcome to **Koya Kingdom**, an immersive text-based RPG adventure game built in Python!

## Features

### Core Gameplay
- **Character Creation** - Create your unique character with a custom name
- **Turn-based Combat** - Fight monsters including goblins, wolves, orcs, and even dragons
- **Quest System** - Accept quests from NPCs and complete objectives
- **Shop System** - Buy weapons, armor, and consumables from merchants
- **Save/Load System** - Save your progress and continue your adventure later

### Game World
The game features multiple locations to explore:
- **Town Square** - The bustling center of Koya Kingdom
- **Joe's Blacksmith** - Buy weapons and armor
- **Dark Forest** - A dangerous area filled with monsters
- **Koya Castle** - The magnificent royal castle

### NPCs
Interact with various characters:
- **Bob** - A friendly townsperson with local knowledge
- **Elder Marcus** - The village leader who needs your help
- **Sarah** - A merchant selling potions and supplies
- **Joe** - The blacksmith who forges the finest weapons

### Items & Equipment
- **Weapons**: Iron Sword, Steel Sword, Legendary Blade, Wooden Bow
- **Armor**: Leather Armor, Chainmail, Plate Armor
- **Consumables**: Health Potions, Mana Potions, Stamina Potions

### Combat System
- Attack enemies with your equipped weapon
- Use consumable items during battle
- Attempt to flee from dangerous encounters
- Earn gold and experience from victories

## How to Play

### Starting the Game
```bash
python3 main.py
```

### Main Menu Options
1. **Explore** - Visit different locations and interact with the world
2. **Status** - View your character's stats, health, and equipped items
3. **Inventory** - Check your items and equipment
4. **Save Game** - Save your current progress
5. **Quit** - Exit the game

### Exploration
When exploring a location, you can:
- Talk to NPCs and engage in branching dialogues
- Visit shops to buy items
- Hunt monsters (in the Dark Forest)
- Travel to different locations

### Combat
During combat encounters:
- **Attack** - Deal damage to the enemy
- **Use Item** - Consume potions to restore health, mana, or stamina
- **Run Away** - Attempt to flee the battle (50% success rate)

### Tips for Success
1. Start by visiting Joe's Blacksmith to buy better equipment
2. Stock up on health potions from Sarah's General Store
3. Talk to Elder Marcus to accept the monster hunting quest
4. Only venture into the Dark Forest when well-equipped
5. Save your game regularly!

## Game Stats
Your character has four main stats:
- **Health**: Your life points (100 max)
- **Mana**: Magic points (100 max)
- **Stamina**: Energy for actions (100 max)
- **Gold**: Currency for purchasing items (starts at 100)

## Requirements
- Python 3.6 or higher
- colorama library (for colored text)

## Installation
The game uses the colorama library which is already included in the `.pythonlibs` directory.

## File Structure
```
Adventure/
├── main.py              # Main game file
├── game_functions.py    # Utility functions
├── scene.py             # Scene and Shop classes
├── npc.py              # NPC and dialog system
├── items.py            # Item database and classes
├── combat.py           # Combat system
├── world.py            # World generation
├── scenes/             # Pre-generated scene files
│   ├── town_square.pkl
│   ├── blacksmith.pkl
│   ├── dark_forest.pkl
│   └── castle.pkl
└── dialog/             # NPC dialog files
    ├── bob.json
    ├── elder_marcus.json
    ├── joe_blacksmith.json
    └── sarah_merchant.json
```

## Development
To regenerate the game world scenes:
```bash
python3 world.py
```

## Credits
Created as a text-based RPG adventure game featuring:
- Dynamic dialog system
- Object-oriented design
- Persistent save system
- Modular architecture for easy expansion

Enjoy your adventure in Koya Kingdom! 🏰⚔️
