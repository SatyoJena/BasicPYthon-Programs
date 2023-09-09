'''
def update_energy(amount):
    energy += amount

energy = 23
update_energy(7)

running the program gives...
Traceback (most recent call last):
  File "G:/pyPrograms/learn_oop5.py", line 5, in <module>
    update_energy(7)
  File "G:/pyPrograms/learn_oop5.py", line 2, in update_energy
    energy += amount
UnboundLocalError: local variable 'energy' referenced before assignment
'''
# but the following is allowed for some reason
def update_energy(amount):
    a.energy += amount

class magic:
    def __init__(self,energy):
        self.energy = energy

a = magic(23)
print(a.energy)
update_energy(7)
print(a.energy)
