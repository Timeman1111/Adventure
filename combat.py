import random
from game_functions import scrollTxt, clear
import time


class Enemy:
    """Enemy class for combat encounters"""

    def __init__(self, name, health, damage, defense, exp_reward, gold_reward):
        self.name = name
        self.max_health = health
        self.health = health
        self.damage = damage
        self.defense = defense
        self.exp_reward = exp_reward
        self.gold_reward = gold_reward

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        actual_damage = max(1, damage - self.defense)
        self.health -= actual_damage
        return actual_damage

    def attack(self):
        return random.randint(int(self.damage * 0.8), int(self.damage * 1.2))


# Enemy database
enemies_database = {
    'goblin': Enemy(
        name="Goblin",
        health=30,
        damage=8,
        defense=2,
        exp_reward=15,
        gold_reward=10
    ),
    'orc': Enemy(
        name="Orc",
        health=60,
        damage=15,
        defense=5,
        exp_reward=30,
        gold_reward=25
    ),
    'wolf': Enemy(
        name="Wolf",
        health=40,
        damage=12,
        defense=3,
        exp_reward=20,
        gold_reward=15
    ),
    'bandit': Enemy(
        name="Bandit",
        health=50,
        damage=10,
        defense=4,
        exp_reward=25,
        gold_reward=30
    ),
    'dragon': Enemy(
        name="Dragon",
        health=200,
        damage=40,
        defense=15,
        exp_reward=200,
        gold_reward=500
    ),
    'skeleton': Enemy(
        name="Skeleton",
        health=35,
        damage=10,
        defense=2,
        exp_reward=18,
        gold_reward=12
    )
}


class Combat:
    """Combat system handler"""

    def __init__(self, player, enemy_key):
        self.player = player
        self.enemy = self.create_enemy(enemy_key)

    def create_enemy(self, enemy_key):
        """Create a copy of an enemy from the database"""
        template = enemies_database.get(enemy_key)
        if template:
            return Enemy(
                template.name,
                template.max_health,
                template.damage,
                template.defense,
                template.exp_reward,
                template.gold_reward
            )
        return None

    def player_attack(self):
        """Calculate player attack damage"""
        base_damage = 10
        weapon_damage = 0

        # Check if player has equipped weapon
        if 'weapon' in self.player.inventory:
            weapon = self.player.inventory['weapon']
            if weapon and hasattr(weapon, 'properties'):
                weapon_damage = weapon.properties.get('damage', 0)

        total_damage = base_damage + weapon_damage
        return random.randint(int(total_damage * 0.8), int(total_damage * 1.2))

    def player_defense(self):
        """Calculate player defense"""
        base_defense = 0
        armor_defense = 0

        # Check if player has equipped armor
        if 'armor' in self.player.inventory:
            armor = self.player.inventory['armor']
            if armor and hasattr(armor, 'properties'):
                armor_defense = armor.properties.get('defense', 0)

        return base_defense + armor_defense

    def player_take_damage(self, damage):
        """Player takes damage"""
        defense = self.player_defense()
        actual_damage = max(1, damage - defense)
        self.player.stats['health'] -= actual_damage
        return actual_damage

    def start_combat(self):
        """Main combat loop"""
        clear()
        scrollTxt(f"\n=== COMBAT ===\n", 0.03)
        scrollTxt(f"A wild {self.enemy.name} appears!\n", 0.03)
        scrollTxt(f"{self.enemy.name} HP: {self.enemy.health}/{self.enemy.max_health}\n\n", 0.03)

        while self.enemy.is_alive() and self.player.stats['health'] > 0:
            scrollTxt(f"Your HP: {self.player.stats['health']}\n", 0.03)
            scrollTxt(f"{self.enemy.name} HP: {self.enemy.health}/{self.enemy.max_health}\n\n", 0.03)

            scrollTxt("Choose your action:\n", 0.03)
            scrollTxt("1. Attack\n", 0.03)
            scrollTxt("2. Use Item\n", 0.03)
            scrollTxt("3. Run Away\n", 0.03)

            choice = input("\nYour choice: ").strip()

            if choice == "1":
                # Player attacks
                damage = self.player_attack()
                actual_damage = self.enemy.take_damage(damage)
                scrollTxt(f"\nYou attack the {self.enemy.name} for {actual_damage} damage!\n", 0.03)
                time.sleep(0.5)

                # Enemy attacks back if still alive
                if self.enemy.is_alive():
                    enemy_damage = self.enemy.attack()
                    actual_enemy_damage = self.player_take_damage(enemy_damage)
                    scrollTxt(f"The {self.enemy.name} attacks you for {actual_enemy_damage} damage!\n", 0.03)
                    time.sleep(0.5)

            elif choice == "2":
                # Use item
                self.use_item_in_combat()

            elif choice == "3":
                # Try to run away
                if random.random() < 0.5:
                    scrollTxt("\nYou successfully ran away!\n", 0.03)
                    time.sleep(1)
                    return False
                else:
                    scrollTxt("\nYou failed to escape!\n", 0.03)
                    # Enemy gets a free attack
                    enemy_damage = self.enemy.attack()
                    actual_enemy_damage = self.player_take_damage(enemy_damage)
                    scrollTxt(f"The {self.enemy.name} attacks you for {actual_enemy_damage} damage!\n", 0.03)
                    time.sleep(0.5)

            scrollTxt("\n" + "="*30 + "\n\n", 0.01)

        # Combat ended
        if self.player.stats['health'] <= 0:
            scrollTxt("\n*** YOU HAVE BEEN DEFEATED ***\n", 0.03)
            scrollTxt("Game Over!\n", 0.03)
            return False
        else:
            scrollTxt(f"\n*** VICTORY ***\n", 0.03)
            scrollTxt(f"You defeated the {self.enemy.name}!\n", 0.03)
            scrollTxt(f"You gained {self.enemy.exp_reward} EXP and {self.enemy.gold_reward} gold!\n", 0.03)
            self.player.stats['money'] += self.enemy.gold_reward
            time.sleep(2)
            return True

    def use_item_in_combat(self):
        """Use a consumable item during combat"""
        scrollTxt("\nYour Inventory:\n", 0.03)

        consumables = {k: v for k, v in self.player.inventory.items()
                       if hasattr(v, 'type') and v.type == 'consumable'}

        if not consumables:
            scrollTxt("You have no consumable items!\n", 0.03)
            time.sleep(1)
            return

        idx = 1
        item_list = []
        for key, item in consumables.items():
            scrollTxt(f"{idx}. {item.name}\n", 0.03)
            item_list.append((key, item))
            idx += 1

        scrollTxt(f"{idx}. Cancel\n", 0.03)

        choice = input("\nChoose item: ").strip()

        try:
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(item_list):
                key, item = item_list[choice_idx]
                effect_type = item.properties['effect_type']
                effect_value = item.properties['effect_value']

                if effect_type in self.player.stats:
                    self.player.stats[effect_type] = min(
                        100,
                        self.player.stats[effect_type] + effect_value
                    )
                    scrollTxt(f"\nYou used {item.name}! Restored {effect_value} {effect_type}.\n", 0.03)
                    del self.player.inventory[key]
                    time.sleep(1)
        except (ValueError, IndexError):
            scrollTxt("\nInvalid choice!\n", 0.03)
            time.sleep(1)
