'''Here's a less trivial lab, testing your knowledge of basic Python
object-oriented programming.

(Remember: if a method response has quotes around it, that means the
method returns a string.  If there are no quotes, that means it
printed (i.e., using print()).

>>> fido = Dog("Fido")
>>> fido.description()
'Fido the Dog'
>>> fido.speak()
'Woof!'

>>> fifi = Cat("Fifi")
>>> fifi.description()
'Fifi the Cat'
>>> fifi.speak()
'Meow!'

>>> nemo = Fish("Nemo")
>>> nemo.description()
'Nemo the Fish'
>>> nemo.speak()
''

>>> fifi.emote()
Fifi the Cat says: Meow!
>>> fido.emote()
Fido the Dog says: Woof!
>>> nemo.emote()
Nemo the Fish says: 

'''

# Write your code here:

class Animal:
    def __init__(self, name):
        self.name = name
        self.sound = ''
        self.specy = ''
        
    def description(self):
        return self.name + ' the ' + self.specy
    def speak(self):
        return self.sound+'!'
    def emote(self):
        print (self.description() + ' says: ' + self.sound + '!')
        
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.specy='Dog'
        self.sound = 'Woof'
        
class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.specy='Fish'
        self.sound = ''
    def speak(self):
        return ''
    def emote(self):
        print (self.description() + ' says: ' + self.sound)
        
        
    
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.specy='Cat'
        self.sound = 'Meow'
    
    
# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
