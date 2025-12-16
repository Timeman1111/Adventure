import time
import os
import colorama
import pickle
import random
from game_functions import *
from combat import Combat
from items import get_item

clear()


# Player Class
class Player:
    def __init__(self):
        # Initialize the player starting stats
        self.name = None
        self.tutorial = True
        self.companions = {}
        self.inventory = {}
        self.achievements = {}
        self.interacted_with = {}
        self.current_location = "town_square"
        self.quests = {}

        self.stats = {
            "health": 100,
            "mana": 100,
            "stamina": 100,
            "money": 100
        }


class Game:

    def __init__(self, player):
        self.player = player
        self.scenes = {}
        self.running = True

    def load_scene(self, scene_file):
        """Load scene from pre-pickled file of Scene type"""
        f = open(scene_file, 'rb')
        scene = pickle.load(f)
        f.close()
        self.scenes[scene.name] = scene
        return scene

    def load_all_scenes(self):
        """Load all game scenes"""
        scene_files = {
            'town_square': 'scenes/town_square.pkl',
            'blacksmith': 'scenes/blacksmith.pkl',
            'dark_forest': 'scenes/dark_forest.pkl',
            'castle': 'scenes/castle.pkl'
        }

        for scene_name, scene_file in scene_files.items():
            try:
                self.load_scene(scene_file)
            except FileNotFoundError:
                scrollTxt(f"Warning: Could not load {scene_file}\n", 0.03)

    def request_name(self):
        """Get player name"""
        while True:
            user = input("\nNAME: ")
            try:
                int(user)
                scrollTxt('\nPlease enter a valid name (not a number)!\n')
                continue
            except:
                if user.strip():
                    self.player.name = user
                    return
                else:
                    scrollTxt('\nName cannot be empty!\n')

    def tutorial(self):
        """Tutorial introduction"""
        scrollTxt('\n=== WELCOME TO KOYA KINGDOM ===\n\n', 0.045)
        scrollTxt('You are about to embark on an epic adventure!\n\n', delay=0.045)
        scrollTxt('What is your name, brave adventurer?\n', delay=0.045)
        self.request_name()
        scrollTxt(f'\nWelcome, {self.player.name}!\n\n', 0.045)
        scrollTxt('Your journey begins in the town square...\n\n', 0.045)
        time.sleep(1)
        self.player.tutorial = False

    def show_status(self):
        """Display player status"""
        clear()
        scrollTxt(f"\n=== {self.player.name}'s Status ===\n", 0.02)
        scrollTxt(f"Health: {self.player.stats['health']}/100\n", 0.02)
        scrollTxt(f"Mana: {self.player.stats['mana']}/100\n", 0.02)
        scrollTxt(f"Stamina: {self.player.stats['stamina']}/100\n", 0.02)
        scrollTxt(f"Gold: {self.player.stats['money']}\n", 0.02)
        scrollTxt(f"Location: {self.player.current_location.replace('_', ' ').title()}\n\n", 0.02)

        scrollTxt("Equipped Items:\n", 0.02)
        weapon = self.player.inventory.get('weapon', None)
        armor = self.player.inventory.get('armor', None)
        scrollTxt(f"  Weapon: {weapon.name if weapon else 'None'}\n", 0.02)
        scrollTxt(f"  Armor: {armor.name if armor else 'None'}\n\n", 0.02)

        input("Press Enter to continue...")

    def show_inventory(self):
        """Display and manage inventory"""
        clear()
        scrollTxt("\n=== INVENTORY ===\n\n", 0.02)

        if not self.player.inventory:
            scrollTxt("Your inventory is empty.\n\n", 0.03)
            input("Press Enter to continue...")
            return

        items_list = []
        idx = 1
        for key, item in self.player.inventory.items():
            if hasattr(item, 'name'):
                scrollTxt(f"{idx}. {item.name} ({item.type})\n", 0.02)
                items_list.append((key, item))
                idx += 1

        scrollTxt(f"\n{idx}. Back\n", 0.02)

        choice = input("\nSelect item to view details (or back): ").strip()
        try:
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(items_list):
                key, item = items_list[choice_idx]
                scrollTxt(f"\n{item.name}\n", 0.02)
                scrollTxt(f"Type: {item.type}\n", 0.02)
                scrollTxt(f"Rarity: {item.rarity}\n", 0.02)
                scrollTxt(f"Description: {item.description}\n", 0.02)
                input("\nPress Enter to continue...")
        except (ValueError, IndexError):
            pass

    def talk_to_npc(self, npc):
        """Handle NPC dialog interactions"""
        clear()
        scrollTxt(f"\n=== Talking to {npc.name} ===\n\n", 0.03)

        current_line = "1"

        while True:
            try:
                line_data = npc.request_line(current_line)
            except KeyError:
                scrollTxt(f"\n{npc.name} has nothing more to say.\n", 0.03)
                time.sleep(1)
                return

            scrollTxt(f"{npc.name}: {line_data['text']}\n\n", 0.03)

            responses = line_data['responses']

            for idx, response in enumerate(responses, 1):
                scrollTxt(f"{idx}. {response[0]}\n", 0.03)

            choice = input("\nYour choice: ").strip()

            try:
                choice_idx = int(choice) - 1
                if 0 <= choice_idx < len(responses):
                    next_action = responses[choice_idx][1]

                    if next_action == "end":
                        scrollTxt("\n", 0.01)
                        return
                    elif next_action == "shop":
                        return "shop"
                    elif next_action == "quest_accept":
                        scrollTxt("\nQuest accepted!\n", 0.03)
                        self.player.quests['monster_hunt'] = "active"
                        time.sleep(1)
                        return
                    else:
                        current_line = str(next_action)
                else:
                    scrollTxt("\nInvalid choice!\n", 0.03)
                    time.sleep(1)
            except (ValueError, IndexError):
                scrollTxt("\nInvalid choice!\n", 0.03)
                time.sleep(1)

    def visit_shop(self, shop):
        """Handle shop interactions"""
        clear()
        scrollTxt(f"\n=== {shop.name} ===\n", 0.03)
        scrollTxt(f"{shop.description}\n\n", 0.03)

        while True:
            scrollTxt("Available Items:\n", 0.03)

            items_list = []
            idx = 1
            for item in shop.products:
                scrollTxt(f"{idx}. {item.name} - {item.cost} gold ({item.type})\n", 0.02)
                items_list.append(item)
                idx += 1

            scrollTxt(f"\n{idx}. Leave Shop\n", 0.03)
            scrollTxt(f"\nYour Gold: {self.player.stats['money']}\n", 0.03)

            choice = input("\nWhat would you like to buy? ").strip()

            try:
                choice_idx = int(choice) - 1
                if choice_idx == len(items_list):
                    return

                if 0 <= choice_idx < len(items_list):
                    item = items_list[choice_idx]

                    if self.player.stats['money'] >= item.cost:
                        self.player.stats['money'] -= item.cost

                        # Handle equipment (weapon/armor) separately
                        if item.type in ['weapon', 'armor']:
                            if item.type in self.player.inventory:
                                scrollTxt(f"\nReplaced your old {item.type} with {item.name}!\n", 0.03)
                            else:
                                scrollTxt(f"\nEquipped {item.name}!\n", 0.03)
                            self.player.inventory[item.type] = item
                        else:
                            # For consumables, add to inventory with unique key
                            key = f"{item.name.lower().replace(' ', '_')}_{len(self.player.inventory)}"
                            self.player.inventory[key] = item
                            scrollTxt(f"\nPurchased {item.name}!\n", 0.03)

                        time.sleep(1)
                    else:
                        scrollTxt(f"\nYou don't have enough gold! Need {item.cost} gold.\n", 0.03)
                        time.sleep(1)
            except (ValueError, IndexError):
                scrollTxt("\nInvalid choice!\n", 0.03)
                time.sleep(1)

    def explore_location(self):
        """Explore current location"""
        current_scene = self.scenes.get(self.player.current_location)

        if not current_scene:
            scrollTxt("Error: Location not found!\n", 0.03)
            return

        clear()
        scrollTxt(f"\n=== {current_scene.name} ===\n\n", 0.03)
        scrollTxt(f"{current_scene.properties.get('location_setting_text', 'No description')}\n\n", 0.03)

        scrollTxt("What would you like to do?\n\n", 0.03)
        scrollTxt("1. Talk to NPCs\n", 0.03)
        scrollTxt("2. Visit Shops\n", 0.03)

        # Show combat option for dark forest
        if self.player.current_location == "dark_forest":
            scrollTxt("3. Hunt Monsters\n", 0.03)
            scrollTxt("4. Travel\n", 0.03)
            scrollTxt("5. Back to Menu\n", 0.03)
        else:
            scrollTxt("3. Travel\n", 0.03)
            scrollTxt("4. Back to Menu\n", 0.03)

        choice = input("\nYour choice: ").strip()

        if choice == "1":
            self.interact_with_npcs(current_scene)
        elif choice == "2":
            self.interact_with_shops(current_scene)
        elif choice == "3" and self.player.current_location == "dark_forest":
            self.hunt_monsters(current_scene)
        elif (choice == "3" and self.player.current_location != "dark_forest") or \
             (choice == "4" and self.player.current_location == "dark_forest"):
            self.travel()

    def interact_with_npcs(self, scene):
        """Interact with NPCs in current scene"""
        npcs = scene.properties.get('npcs', {})

        if not npcs:
            scrollTxt("\nThere's no one to talk to here.\n", 0.03)
            time.sleep(1)
            return

        clear()
        scrollTxt("\n=== NPCs ===\n\n", 0.03)

        npc_list = list(npcs.items())
        for idx, (key, npc) in enumerate(npc_list, 1):
            scrollTxt(f"{idx}. {npc.name}\n", 0.03)

        scrollTxt(f"\n{len(npc_list) + 1}. Back\n", 0.03)

        choice = input("\nWho would you like to talk to? ").strip()

        try:
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(npc_list):
                key, npc = npc_list[choice_idx]
                result = self.talk_to_npc(npc)

                # If NPC wants to open shop
                if result == "shop":
                    shops = scene.properties.get('shops', [])
                    if shops:
                        self.visit_shop(shops[0])
        except (ValueError, IndexError):
            pass

    def interact_with_shops(self, scene):
        """Interact with shops in current scene"""
        shops = scene.properties.get('shops', [])

        if not shops:
            scrollTxt("\nThere are no shops here.\n", 0.03)
            time.sleep(1)
            return

        clear()
        scrollTxt("\n=== Shops ===\n\n", 0.03)

        for idx, shop in enumerate(shops, 1):
            scrollTxt(f"{idx}. {shop.name}\n", 0.03)

        scrollTxt(f"\n{len(shops) + 1}. Back\n", 0.03)

        choice = input("\nWhich shop? ").strip()

        try:
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(shops):
                self.visit_shop(shops[choice_idx])
        except (ValueError, IndexError):
            pass

    def hunt_monsters(self, scene):
        """Engage in random combat"""
        encounters = scene.properties.get('encounters', [])

        if not encounters:
            scrollTxt("\nNo monsters here.\n", 0.03)
            time.sleep(1)
            return

        enemy_key = random.choice(encounters)
        combat = Combat(self.player, enemy_key)
        result = combat.start_combat()

        if not result and self.player.stats['health'] <= 0:
            self.game_over()

    def travel(self):
        """Travel to different locations"""
        clear()
        scrollTxt("\n=== TRAVEL ===\n\n", 0.03)

        locations = {
            '1': ('town_square', 'Town Square'),
            '2': ('blacksmith', "Joe's Blacksmith"),
            '3': ('dark_forest', 'Dark Forest'),
            '4': ('castle', 'Koya Castle')
        }

        for key, (loc_key, loc_name) in locations.items():
            marker = " (current)" if loc_key == self.player.current_location else ""
            scrollTxt(f"{key}. {loc_name}{marker}\n", 0.03)

        scrollTxt("\n5. Cancel\n", 0.03)

        choice = input("\nWhere would you like to go? ").strip()

        if choice in locations:
            loc_key, loc_name = locations[choice]
            if loc_key != self.player.current_location:
                self.player.current_location = loc_key
                scrollTxt(f"\nTraveling to {loc_name}...\n", 0.03)
                time.sleep(1)

    def save_game(self):
        """Save game state"""
        try:
            save_data = {
                'player': self.player,
                'version': '1.0'
            }
            with open('savegame.pkl', 'wb') as f:
                pickle.dump(save_data, f)
            scrollTxt("\nGame saved successfully!\n", 0.03)
            time.sleep(1)
        except Exception as e:
            scrollTxt(f"\nError saving game: {e}\n", 0.03)
            time.sleep(1)

    def load_game(self):
        """Load game state"""
        try:
            with open('savegame.pkl', 'rb') as f:
                save_data = pickle.load(f)
            self.player = save_data['player']
            scrollTxt("\nGame loaded successfully!\n", 0.03)
            time.sleep(1)
            return True
        except FileNotFoundError:
            scrollTxt("\nNo save file found.\n", 0.03)
            time.sleep(1)
            return False
        except Exception as e:
            scrollTxt(f"\nError loading game: {e}\n", 0.03)
            time.sleep(1)
            return False

    def game_over(self):
        """Handle game over"""
        clear()
        scrollTxt("\n" + "="*40 + "\n", 0.02)
        scrollTxt("         GAME OVER\n", 0.05)
        scrollTxt("="*40 + "\n\n", 0.02)
        scrollTxt("Your adventure has come to an end...\n", 0.03)
        scrollTxt("\nThank you for playing!\n\n", 0.03)
        self.running = False
        time.sleep(3)

    def main_menu(self):
        """Display main menu"""
        while self.running:
            clear()
            scrollTxt(f"\n=== {self.player.name}'s Adventure ===\n\n", 0.03)

            scrollTxt("1. Explore\n", 0.03)
            scrollTxt("2. Status\n", 0.03)
            scrollTxt("3. Inventory\n", 0.03)
            scrollTxt("4. Save Game\n", 0.03)
            scrollTxt("5. Quit\n", 0.03)

            choice = input("\nWhat would you like to do? ").strip()

            if choice == "1":
                self.explore_location()
            elif choice == "2":
                self.show_status()
            elif choice == "3":
                self.show_inventory()
            elif choice == "4":
                self.save_game()
            elif choice == "5":
                scrollTxt("\nThanks for playing!\n", 0.03)
                self.running = False
                break

    def start_game(self):
        """Initialize and start the game"""
        # Check for saved game
        clear()
        scrollTxt("\n=== KOYA KINGDOM ===\n\n", 0.03)
        scrollTxt("1. New Game\n", 0.03)
        scrollTxt("2. Load Game\n", 0.03)

        choice = input("\nYour choice: ").strip()

        if choice == "2":
            if self.load_game():
                self.player.tutorial = False
            else:
                scrollTxt("Starting new game...\n", 0.03)
                time.sleep(1)

        # Run tutorial for new games
        if self.player.tutorial:
            self.tutorial()

        # Load all scenes
        self.load_all_scenes()

        # Start main game loop
        self.main_menu()


if __name__ == "__main__":
    game = Game(Player())
    game.start_game()
