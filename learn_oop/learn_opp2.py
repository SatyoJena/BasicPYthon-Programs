'''
dunder method - Double UNDERscore method
these methods wont be called by user in __main__ rather,
python interpreter uses these methods to interact with the classes. For example,
>__init__(self,*args) method is called when the object is created
Basically you can custom design what will happen when these funcs are used
>__len__(self) is called when object is passed into len() (length fn.)
>__abs__(self) is called when object is passed into abs() (absolute fn.)
>__dict__ is an attribute that returns a dict containing values of other attrs.
a.__dict__ has same result as var(a); where a is a class object
>__call__(self) method defines what to do when your class object is called like a function.
def __call__(self):
    print('a monster has been called'); something like this
>__add__(self,value) we can use this value to use our class object like some
other object which supports '+'(str+str, int+int, int+float etc). for example,
def __add__(self, value):
    return self.health + value #this operation should be viable, though
in main,
>>>a = Monster(20,20,20)
>>>print(a + 4)#Typeerror should be raised as int and Monster cant be added
>>>24#prints 24 instead
>__str__(self) defines how to behave when an instance of a class is passed to
str() and print()
def __str__(self):
    return f"{id(self)} have health {self.health}."
>>>a = Monster(20,20,20)
>>>print(a)
>>>Monster obect at 0x12AD3469420 have health 20)
'''
class Monster:
    def __init__(self,*args):
        self.health  = args[0]#no need to predefine attributes when u can do it
        self.stamina = args[1]#upon the instantiation of an object
        self.energy  = args[2]
        #we can pedefine the attributes in method header, but *args looks cool.
        print("The monster was created!!")
        #this will be printed even if i dont call it in __main__, because python
    def __call__(self):
        print('a monster has been called')

    
    def  attack(self,damage):
        print("the monster has attacked")
        print(f"the monster dealt {damage} damage")
        self.energy -= 5
        print(f"the monster now has {self.energy} energy")
        
    def move(self,speed):
        print(f"the monster has moved at {speed} speed")
        self.stamina -= 10
        print(f"Its stamina decreased to {self.stamina}")
        
