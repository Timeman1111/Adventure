"""
World setup - Creates all scenes, shops, and NPCs for the game
"""
import pickle
from scene import Scene, Shop
from npc import NPC
from items import items_database


def create_game_world():
    """Create and return all game scenes"""

    scenes = {}

    # ===== TOWN SQUARE =====
    town_square = Scene("Town Square")
    town_square.set_location_text(
        "You are in the town square of Koya Kingdom. "
        "The bustling center of town with shops and friendly faces. "
        "To the east lies the dark forest, to the north is the castle."
    )

    # Create Bob NPC
    bob = NPC("Bob")
    bob.import_dialog("dialog/bob.json")

    # Create Elder Marcus NPC
    elder_marcus = NPC("Elder Marcus")
    elder_marcus.import_dialog("dialog/elder_marcus.json")

    # Create Sarah's General Store
    sarah_shop = Shop("Sarah's General Store", "Sarah", "A cozy shop with various supplies")
    sarah_shop.add_products([
        items_database['health_potion'],
        items_database['mana_potion'],
        items_database['stamina_potion'],
        items_database['super_health_potion']
    ])

    # Create Sarah NPC
    sarah = NPC("Sarah")
    sarah.import_dialog("dialog/sarah_merchant.json")

    town_square.add_shop(sarah_shop)
    town_square.properties['npcs'] = {
        'bob': bob,
        'elder_marcus': elder_marcus,
        'sarah': sarah
    }
    scenes['town_square'] = town_square


    # ===== BLACKSMITH =====
    blacksmith_scene = Scene("Joe's Blacksmith")
    blacksmith_scene.set_location_text(
        "The heat from the forge warms your face. "
        "The sound of hammer on anvil rings through the air. "
        "Weapons and armor line the walls."
    )

    # Create Joe's Shop
    joe_shop = Shop("Joe's Smithy", "Joe", "The finest weapons and armor")
    joe_shop.add_products([
        items_database['iron_sword'],
        items_database['steel_sword'],
        items_database['wooden_bow'],
        items_database['leather_armor'],
        items_database['chainmail'],
        items_database['plate_armor']
    ])

    # Create Joe NPC
    joe = NPC("Joe")
    joe.import_dialog("dialog/joe_blacksmith.json")

    blacksmith_scene.add_shop(joe_shop)
    blacksmith_scene.properties['npcs'] = {'joe': joe}
    scenes['blacksmith'] = blacksmith_scene


    # ===== DARK FOREST =====
    dark_forest = Scene("Dark Forest")
    dark_forest.set_location_text(
        "You enter a dark and ominous forest. "
        "Strange sounds echo through the trees. "
        "This is dangerous territory - monsters lurk here."
    )
    dark_forest.properties['encounters'] = ['goblin', 'wolf', 'orc']
    dark_forest.properties['npcs'] = {}
    scenes['dark_forest'] = dark_forest


    # ===== CASTLE =====
    castle = Scene("Koya Castle")
    castle.set_location_text(
        "You stand before the magnificent Koya Castle. "
        "Its towering spires reach into the sky. "
        "Guards stand at attention by the entrance."
    )
    castle.properties['npcs'] = {}
    scenes['castle'] = castle

    return scenes


def save_scenes():
    """Create and save all scenes to pickle files"""
    scenes = create_game_world()

    for scene_name, scene in scenes.items():
        filename = f"scenes/{scene_name}.pkl"
        with open(filename, 'wb') as f:
            pickle.dump(scene, f)
        print(f"Saved {scene_name} to {filename}")


if __name__ == "__main__":
    # Create scenes directory if it doesn't exist
    import os
    if not os.path.exists('scenes'):
        os.makedirs('scenes')

    save_scenes()
    print("\nAll scenes created successfully!")
