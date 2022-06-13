global player
global items
global assets

player = {
    "name" : "Player",
    "level" : 0,
    "coins" : 0,
    "currentHealth" : {
        "currentHealth" : 1000,
        "maxHealth" : 1000
    },
    "inventory" : {
        "inMainHand" : ("Fist", 20, 0, 0),
        "inOffhand" : ("Nothing", 0, 0, 0),
        "inAccessory" : ("Nothing", 0, 0 ,0),
        "onBody" : {
            "onHead" : ("Nothing", 50, 0, 0),
            "onChest" : ("Nothing", 0, 0, 0),
            "onLegs" : ("Nothing", 0, 0, 0),
            "onFeet" : ("Nothing", 0, 0, 0)
        }
    }
}

items = {
    "itemsMainHand" : { # Main Hand Format - str(name), int(damage), int(price), int(level) - Tuple
        0 : ("Rusty Dagger", 100, 50, 1),
        1 : ("Katana", 200, 100, 2),
        2 : ("Longsword", 300, 200, 2),
        3 : ("Sythe", 400, 500, 4),
        4 : ("Axe", 400, 500, 4),
        5 : ("Astral Sword", 600, 750, 7)
    },
    "itemsOffhand" : { # Offhand Item Format - str(name), int(currentDefense), int(price), int(level) - Tuple
        0 : ("Wooden Sheild", 150, 75, 1),
        1 : ("Bronze Sheild", 200, 100, 2),
        2 : ("Iron Sheild", 400, 300, 2),
        3 : ("Obsidian Sheild", 300, 400, 4),
        4 : ("Diamond Sheild", 300, 400, 4),
        5 : ("Astral Sheild", 650, 500, 8)
    },
    "itemsAccessory" : { # Accesory Item Format - str(name), float(attack power), int(price), int(level) - Tuple
        0 : ("Old Rock", 1.5, 50, 1),
        1 : ("Odd Relic", 2, 130, 1),
        2 : ("Goat's Horn", 2.5, 200, 2),
        3 : ("Engraved Emerald", 3, 315, 3),
        4 : ("Enchanted Diamond", 3.5, 400, 4),
        5 : ("Astral Totem", 5, 500, 6)
    },
    "itemsBody" : { # Body Item Format - str(name), int(currentDefense), int(price), int(level) - Tuple
        "itemsHead" : {
            0 : ("Rookie Helmet", 50, 50, 1),
            1 : ("Cadet Helmet", 100, 100, 2),
            2 : ("Gladiator Helmet", 150, 300, 3),
            3 : ("Obsidian Helmet", 200, 400, 4),
            4 : ("Inquizitor Helmet", 200, 400, 4),
            5 : ("Astral Helmet", 450, 500, 6)
        },
        "itemsChest" : {
            0 : ("Rookie Chestplate", 125, 125, 1),
            1 : ("Cadet Chestplate", 250, 250, 2),
            2 : ("Gladiator Chestplate", 375, 750, 3),
            3 : ("Obsidian Chestplate", 500, 1000, 4),
            4 : ("Inquizitor Chestplate", 500, 1000, 4),
            5 : ("Astral Chestplate", 1125, 1250, 8)
        },
        "itemsLegs" : {
            0 : ("Rookie Leggings", 75, 75, 1),
            1 : ("Cadet Leggings", 150, 150, 2),
            2 : ("Gladiator Leggings", 225, 450, 3),
            3 : ("Obsidian Leggings", 300, 600, 4),
            4 : ("Inquizitor Leggings", 300, 600, 4),
            5 : ("Astral Leggings", 675, 750, 7)
        },
        "itemsFeet" : {
            0 : ("Rookie Boots", 25, 25, 1),
            1 : ("Cadet Boots", 50, 50, 2),
            2 : ("Gladiator Boots", 75, 150, 3),
            3 : ("Obsidian Boots", 100, 200, 4),
            4 : ("Inquizitor Boots", 100, 200, 4),
            5 : ("Astral Boots", 225, 250, 6)
        }
    }
}

assets = {
    "assetsDialouge" : {
        0: ("Put Dialouge Here")
    },
    "assetsBoss" : { # Boss Asset Format - str(name), tuple(int(maxdamage), int(mindamage)), tuple(int(maxdrop), int(mindrop)), int(currentHealth), int(level) - Tuple
        0 : ("Gobin Giant", (100, 0), (600, 400), 1000, 1),
        1 : ("Bronze Mech", (200, 50), (1200, 400), 1750, 3),
        2 : ("The Trickster", (325, 150), (2400, 400), 2500, 4),
        3 : ("Sludge Monster", (750, 250), (3525, 400), 3000, 5),
        4 : ("Coiled Dragon", (2000, 700), (4555, 400), 4500, 7),
        5 : ("Mystical Heptagram", (4000, 1400), (5000, 1500), 7500, 9)
    }
}

def valcoins(action, evalcoins):
    # Do you have enough coins?
    
    # Operation Evaluation
    
    pass
    
def valhealth(action, evalHealth):
    # Defense evaluation
    
    # Health evaluation for health loss

    # Health Restoration

    pass
