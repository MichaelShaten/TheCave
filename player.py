from entity import Entity

class Player(Entity):
    def __init__(self,hp,ac,speed,player_name):
        super().__init__(hp, ac, speed, species="player", name=player_name)


# import random

# result = random.randrange(1,21)


# print(result)