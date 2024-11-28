# from datetime import datetime
# import random

# class monster:
#     def __init__(self):
#         self.name = f"Monster_{random.randit(1, 1000)}"
#         self.type = random.choice(["Fire", "Water", "Earth", "Air"])
#         self.level = random.randint(1, 100)
#         self.rarity = random.choice(["Common", "Uncommon", "Rare", "Legendary"])
#         self.damage = random.randint(10, 500)
#         self.health = random.randint(100, 1000)
#         self.energy = random.randint(50, 200)
#         self.sanity = random.randint(0, 100)
#         self.timestamp = datetime.now(timezone.utc)


#     def to_dict(self):
#         return {
#             "Name": self.name,
#             "Type": self.type,
#             "Level": self.level,
#             "Rarity": self.rarity,
#             "Damage": self.damage,
#             "Health": self.health,
#             "Energy": self.energy,
#             "Sanity": self.sanity,
#             "Timestamp": self.timestamp
#         }


#     def __repr__(self):
#         return f"Monster(name={self.name}, type={self.type}, level={self.level})"

