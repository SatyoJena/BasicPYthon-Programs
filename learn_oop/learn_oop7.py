class Monster:
    def __init__(self,health):
        self.hp = health
    def reduce_hp(self,damage):
        self.hp -=(damage)

class Hero:
    def __init__(self,damage,MonsterObject):
        "does damage dmg to monster"
        self.damage = damage
        self.MonsterObject = MonsterObject
    def attack(self):
        before = self.MonsterObject.hp
        self.MonsterObject.reduce_hp(self.damage)
        after = self.MonsterObject.hp
        print(f"monster's hp reduced from {before} to {after}")
