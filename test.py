from MonsterLab import Monster
from app.data import Database





# Create an instance of Monster
monster = Monster()

# Inspect its attributes
print(dir(monster))


    # def to_dict(self, monster):
    #     """Convert the Monsters instance to a dictionary"""
    #     monster_dict = monster.__dict__

    #     return {
    #         "Name": monster_dict.get("name", "Unknown"),
    #         "Type": monster_dict.get("type", "Unknown"),
    #         "Level": monster_dict.get("level", 0),
    #         "Rarity": monster_dict.get("rarity", "Common"),
    #         "Damage": monster_dict.get("damage", 0),
    #         "Health": monster_dict.get("health", 0),
    #         "Energy": monster_dict.get("energy", 0),
    #         "Sanity": monster_dict.get("sanity", 100),
    #         "Timestamp": monster_dict.get("timestamp")
    #     }

    # def __repr__(self):
    #     return f"Database connection to {self.db}"