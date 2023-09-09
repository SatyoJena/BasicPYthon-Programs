# A diffrent style to set attributes
class Monster:
    ER = 1.85
    def __init__(self,health,energy):
        self.health = health
        self.set_energy(energy)#attribute being set by a method. pretty good eh?

    def set_energy(self,energy):
        new_energy = self.ER * energy
        self.energy = new_energy
        
