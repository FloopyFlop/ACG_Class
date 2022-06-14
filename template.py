# _  _  ____  ____   ___    ____  ____    __     ___  _   _    ____  ____   ___  _   _      __     ___   ___     ___  __      __    ___  ___ 
#( )/ )(_  _)(  _ \ / __)  (_  _)( ___)  /__\   / __)( )_( )  (_  _)( ___) / __)( )_( )    /__\   / __) / __)   / __)(  )    /__\  / __)/ __)
# )  (  _)(_  )(_) )\__ \    )(   )__)  /(__)\ ( (__  ) _ (     )(   )__) ( (__  ) _ (    /(__)\ ( (__ ( (_-.  ( (__  )(__  /(__)\ \__ \\__ \
#(_)\_)(____)(____/ (___/   (__) (____)(__)(__) \___)(_) (_)   (__) (____) \___)(_) (_)  (__)(__) \___) \___/   \___)(____)(__)(__)(___/(___/

# This is the template file for the KIDS TEACH TECH adventure game, advanced python, class. Read README.md for linsensing properties.

#   __ .___       .__  __    __   
#  / / |   | ____ |__|/  |_  \ \  
# / /  |   |/    \|  \   __\  \ \ 
# \ \  |   |   |  \  ||  |    / / 
#  \_\ |___|___|  /__||__|   /_/  
#               \/                

import random # Random number generator for bossfight.

global player
global items
global assets

player = { # All global player variables.
    "name" : "Player",
    "level" : 0,
    "coins" : 0,
    "health" : {
        "currentHealth" : 1000,
        "maxHealth" : 1000
    },
    "inventory" : {
        "Mainhand" : ["Fist", 20, 0, 0],
        "Offhand" : ["Nothing", 0, 0, 0],
        "Accesory" : ["Nothing", 0, 0 ,0],
        "Body" : {
            "Head" : ["Nothing", 50, 0, 0],
            "Chest" : ["Nothing", 0, 0, 0],
            "Legs" : ["Nothing", 0, 0, 0],
            "Feet" : ["Nothing", 0, 0, 0]
        }
    }
}

items = { # All item data.
    "Mainhand" : {
        "format" : ["Name", "Damage", "Price", "Level"],
        0 : ["Rusty Dagger", 100, 50, 1],
        1 : ["Katana", 200, 100, 2],
        2 : ["Longsword", 300, 200, 2],
        3 : ["Sythe", 400, 500, 4],
        4 : ["Axe", 400, 500, 4],
        5 : ["Astral Sword", 600, 750, 7]
    },
    "Offhand" : {
        "format" : ["Name", "Defense", "Price", "Level"],
        0 : ["Wooden Sheild", 150, 75, 1],
        1 : ["Bronze Sheild", 200, 100, 2],
        2 : ["Iron Sheild", 400, 300, 2],
        3 : ["Obsidian Sheild", 300, 400, 4],
        4 : ["Diamond Sheild", 300, 400, 4],
        5 : ["Astral Sheild", 650, 500, 8]
    },
    "Accesory" : {
        "format" : ["Name", "Power", "Price", "Level"],
        0 : ["Old Rock", 1.5, 50, 1],
        1 : ["Odd Relic", 2, 130, 1],
        2 : ["Goat's Horn", 2.5, 200, 2],
        3 : ["Engraved Emerald", 3, 315, 3],
        4 : ["Enchanted Diamond", 3.5, 400, 4],
        5 : ["Astral Totem", 5, 500, 6]
    },
    "Body" : {
        "Head" : {
            "format" : ["Name", "Defense", "Price", "Level"],
            0 : ["Rookie Helmet", 50, 50, 1],
            1 : ["Cadet Helmet", 100, 100, 2],
            2 : ["Gladiator Helmet", 150, 300, 3],
            3 : ["Obsidian Helmet", 200, 400, 4],
            4 : ["Inquizitor Helmet", 200, 400, 4],
            5 : ["Astral Helmet", 450, 500, 6]
        },
        "Chest" : {
            "format" : ["Name", "Defense", "Price", "Level"],
            0 : ["Rookie Chestplate", 125, 125, 1],
            1 : ["Cadet Chestplate", 250, 250, 2],
            2 : ["Gladiator Chestplate", 375, 750, 3],
            3 : ["Obsidian Chestplate", 500, 1000, 4],
            4 : ["Inquizitor Chestplate", 500, 1000, 4],
            5 : ["Astral Chestplate", 1125, 1250, 8]
        },
        "Legs" : {
            "format" : ["Name", "Defense", "Price", "Level"],
            0 : ["Rookie Leggings", 75, 75, 1],
            1 : ["Cadet Leggings", 150, 150, 2],
            2 : ["Gladiator Leggings", 225, 450, 3],
            3 : ["Obsidian Leggings", 300, 600, 4],
            4 : ["Inquizitor Leggings", 300, 600, 4],
            5 : ["Astral Leggings", 675, 750, 7]
        },
        "Feet" : {
            "format" : ["Name", "Defense", "Price", "Level"],
            0 : ["Rookie Boots", 25, 25, 1],
            1 : ["Cadet Boots", 50, 50, 2],
            2 : ["Gladiator Boots", 75, 150, 3],
            3 : ["Obsidian Boots", 100, 200, 4],
            4 : ["Inquizitor Boots", 100, 200, 4],
            5 : ["Astral Boots", 225, 250, 6]
        }
    }
}

assets = { # All misc asset data, if you add any special types of data, here is the place to do it.
    "headings" : {
        "shopBanner" : ("          ____  _  _   __  ____         \n   ___   / ___)/ )( \ /  \(  _ \   ___  \n  (___)  \___ \) __ ((  O )) __/  (___) \n         (____/\_)(_/ \__/(__)          \n") # A cool little shop banner
    },
    "boss" : {
        "format" : ["Name", ["maxDamage", "minDamage"], ["maxDrop", "minDrop"],"health", "Level"],
        0 : ["Gobin Giant", [100, 0], [600, 400], 1000, 1],
        1 : ["Bronze Mech", [200, 50], [1200, 400], 1750, 3],
        2 : ["The Trickster", [325, 150], [2400, 400], 2500, 4],
        3 : ["Sludge Monster", [750, 250], [3525, 400], 3000, 5],
        4 : ["Coiled Dragon", [2000, 700], [4555, 400], 4500, 7],
        5 : ["Mystical Heptagram", [4000, 1400], [5000, 1500], 7500, 9]
    },
    "characters" : {
        "format" : ["Name"],
        "Shopkeeper" : ["Janet"],
        "Mayor" : ["Mayor Cheese"],
        "Construction Worker" : ["Hardhat Bob"],
        "Robot" : ["Rob"],
        "Prisioner" : ["Prisoneer"],
        "Guard" : ["Guard Jerry"],
        "Wizard" : ["GWhiz"],
        "Empty" : ["Name"],
    }
}

#   __ _________            .___       __   
#  / / \_   ___ \  ____   __| _/____   \ \  
# / /  /    \  \/ /  _ \ / __ |/ __ \   \ \ 
# \ \  \     \___(  <_> ) /_/ \  ___/   / / 
#  \_\  \______  /\____/\____ |\___  > /_/  
#              \/            \/    \/       

def dialogue(Character, Dialogue): # Part 1 -
    pass
# Code a function that makes a character (from assets) recite dialogue

def choice(Choices): # Part 2 --
    pass
# Code a function that allows the user to choose from one of many options, and plan out a way that you can integrate it into shop() and bossfight()

def valcoins(Action, Val): # Part 1 -
    pass
# Add or subtract coins from player["coins"] based on the Action and the value in Val, If the player does not have enough coins then cancel the transaction. (If the player is buying an item it should not be given to them)

def valhealth(Action, Val): # Part 1 -
    pass 
# Add, Subtract health from player["health"]["currentHealth"] or refill to player["health"]["maxHealth"], the subtraction should also take in to account the defense of the player (what armor the player is wearing)

def shop(): # Part 2 --
    pass
# First the player will select what type of item they want, then they will buy it (if they are a high enough level) make sure to display the items niceley

def bossfight(): # Part 3 ---
    pass 
# Create a bossfight which deals a random amount of damage between assets["Boss"][int]["maxDamage"] assets["Boss"][int]["minDamage"] and, when killed drops an amount of coins between the min and max.
#This should also be Level sensitive and there should be a choice for the player to attack with their sword or defend with their sheild.