class Entity:
    def __init__(self,hp=20,ac=12,speed=30,species="<unknown>", name="entity",flight=False):
        self.hp = hp
        self.ac = ac
        self.speed = speed
        self.species = species
        self.name = name
        self.flight = flight

    def take_damage(self, damage_taken):
        self.hp -= damage_taken
        print(f"{self.species} takes {damage_taken} points of damage! ")

    def attack(self, enemy, damage_given):
        enemy.take_damage(damage_given)