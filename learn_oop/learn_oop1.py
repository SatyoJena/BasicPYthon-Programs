'''
in a class, varibles are called "attributes" and functions are called "methods"
'''
class Monster:#the convention for class names in CamelCaseNAmes
    health  = 90
    stamina = 50
    energy  = 60
    '''
    def  attack():
        print("the monster has attacked")
        
    though the above function looks fine, but upon calling in __main__ like
    >>> a = Monster()
    >>> a.attack(),
    it will raise a TypeError saying,
    Monster.attack() takes 0 positional arguments, but 1 was given.
    
    Every method of a class is defined with at least 1 argument i.e.
    the reference to class it is being defined in, because in __main__, python
    itself passes a reference to the method that was called.
    correct way to do it is as follows
    '''
    def  attack(self,damage):
        print("id of self is",id(self))
        print("the monster has attacked")
        print(f"the monster dealt {damage} damage")
        self.energy -= 5
        print(f"the monster now has {self.energy} energy")
        
    '''
    self is a reference to the class it can be used throughout(and only in)
    the class methods to access class attribues and methods.
    we can give it any name but generally "self" "this" are a convention to use.
    '''
    def move(self,speed):
        #self here has nothing to do with self up there.
        #that self got destroyed(garbaged) and we created another self
        print(f"the monster has moved at {speed} speed")
        self.stamina -= 10
        print(f"Its stamina decreased to {self.stamina}")
# __main__ scope
a= Monster()
print("id of a is",id(a)) #this will have same result as self
a.attack(40)
a.move(33)
