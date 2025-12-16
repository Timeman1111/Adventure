class Item:
    """Base Item class for all items in the game"""

    def __init__(self, name, item_type, cost, rarity, description, properties={}):
        self.name = name
        self.type = item_type
        self.cost = cost
        self.rarity = rarity
        self.description = description
        self.properties = properties


class Weapon(Item):
    """Weapon class for combat items"""

    def __init__(self, name, cost, rarity, description, damage, weapon_type):
        properties = {
            'damage': damage,
            'weapon_type': weapon_type
        }
        super().__init__(name, 'weapon', cost, rarity, description, properties)


class Armor(Item):
    """Armor class for defensive items"""

    def __init__(self, name, cost, rarity, description, defense, armor_type):
        properties = {
            'defense': defense,
            'armor_type': armor_type
        }
        super().__init__(name, 'armor', cost, rarity, description, properties)


class Consumable(Item):
    """Consumable class for usable items"""

    def __init__(self, name, cost, rarity, description, effect_type, effect_value):
        properties = {
            'effect_type': effect_type,
            'effect_value': effect_value
        }
        super().__init__(name, 'consumable', cost, rarity, description, properties)


# Create some default items
items_database = {
    # Weapons
    'iron_sword': Weapon(
        name="Iron Sword",
        cost=50,
        rarity="common",
        description="A basic iron sword. Reliable and sturdy.",
        damage=15,
        weapon_type="sword"
    ),
    'steel_sword': Weapon(
        name="Steel Sword",
        cost=150,
        rarity="uncommon",
        description="A well-crafted steel sword. Sharp and deadly.",
        damage=25,
        weapon_type="sword"
    ),
    'legendary_blade': Weapon(
        name="Legendary Blade",
        cost=1000,
        rarity="legendary",
        description="An ancient blade forged by master smiths. Its edge never dulls.",
        damage=50,
        weapon_type="sword"
    ),
    'wooden_bow': Weapon(
        name="Wooden Bow",
        cost=30,
        rarity="common",
        description="A simple wooden bow. Good for hunting.",
        damage=10,
        weapon_type="bow"
    ),

    # Armor
    'leather_armor': Armor(
        name="Leather Armor",
        cost=40,
        rarity="common",
        description="Light leather armor. Provides basic protection.",
        defense=10,
        armor_type="light"
    ),
    'chainmail': Armor(
        name="Chainmail",
        cost=120,
        rarity="uncommon",
        description="Interlocking metal rings. Solid protection.",
        defense=20,
        armor_type="medium"
    ),
    'plate_armor': Armor(
        name="Plate Armor",
        cost=500,
        rarity="rare",
        description="Heavy plate armor. Maximum protection.",
        defense=40,
        armor_type="heavy"
    ),

    # Consumables
    'health_potion': Consumable(
        name="Health Potion",
        cost=20,
        rarity="common",
        description="Restores 50 health points.",
        effect_type="health",
        effect_value=50
    ),
    'mana_potion': Consumable(
        name="Mana Potion",
        cost=20,
        rarity="common",
        description="Restores 50 mana points.",
        effect_type="mana",
        effect_value=50
    ),
    'stamina_potion': Consumable(
        name="Stamina Potion",
        cost=15,
        rarity="common",
        description="Restores 50 stamina points.",
        effect_type="stamina",
        effect_value=50
    ),
    'super_health_potion': Consumable(
        name="Super Health Potion",
        cost=75,
        rarity="rare",
        description="Restores 150 health points.",
        effect_type="health",
        effect_value=150
    )
}


def get_item(item_key):
    """Get an item from the database by its key"""
    return items_database.get(item_key, None)
