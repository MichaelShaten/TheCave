import random
from entity import Entity

# class Monster:
#     def __init__(self,hp=20,ac=12,speed=30,species="monster",flight=False):
#         self.hp = hp
#         self.ac = ac
#         self.speed = speed
#         self.species = species

#     def take_damage(self, damage_taken):
#         self.hp -= damage_taken
#         print(f"{self.species} takes {damage_taken} points of damage! ")

#     def attack(self, enemy, damage_given):
#         enemy.take_damage(damage_given)

        

class Griffin(Entity):
    def __init__(self,hp=30,ac=18,speed=30):
        super().__init__(hp=hp,ac=ac,speed=speed,species="griffin",flight=True)

# class Scorpion(Entity):
#     def __init__(self,hp=0)
        

def main():
    
    print("it's printing this")
    spider = Entity(20,12,30,"ogre")
    

    print(spider.hp)

    spider.take_damage(10)
    print(spider.hp)

    scorpion = Entity(10,10,10)
    sword_choice = input("Pick a sword (gold or silver): ")
    sword_damage = 0
    sword_equipped = sword_choice
    if sword_equipped == "gold":
        sword_damage = random.randrange(1,6)
    elif sword_equipped == "silver":
        sword_damage = random.randrange(1,10)
        

    scorpion.take_damage(sword_damage)
    print(scorpion.hp)
   

if __name__ == "__main__":
    main()