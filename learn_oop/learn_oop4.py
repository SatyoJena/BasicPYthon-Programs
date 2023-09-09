class Monsters:
    def __init__(self,func):
        self.func = func

class Attack:
    def bite(self):
        print("the moster just bit")
    def strike(self):
        print("the moster just striked")
    def slash(self):
        print("the moster just slashed")
    def kick(self):
        print("the monster just kicked")

#a= Monsters(Attack.slash) -- wrong!!
'''
Attack.slash is a Class object Attack().slash is a method object
the correct is equivalent to
b= Attack()
a= Monsterss(b.slash)
'''
a= Monsters(Attack().slash) # right
a.func()
