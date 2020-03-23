'''
Animal Shelter:

An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out"
basis.

People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type).

They cannot select which specific animal they would like.

Create the data structures to maintain this system and implement operations such as:
enqueue, dequeueAny, dequeueDog and dequeueCat.

You may use the built-in Linked list data structure. 
'''
import time

class Animal:
  DOG = 'dog'
  CAT = 'cat'

  animal_type = None
  arrival_order = None

  def __init__(self, animal_type):
    self.animal_type = animal_type

  def get_type(self):
    return self.animal_type

  def is_dog(self):
    if self.animal_type == self.DOG:
      return True
    else:
      return False

  def set_arrival_order(self, value):
    self.arrival_order = value 

  def get_order(self):
    return self.arrival_order

  def older_than(self, other):
    if self.get_order() < other.get_order():
      return True
    else:
      return False

  def __str__(self):
    return self.animal_type + ': ' + str(self.arrival_order)


class Dog(Animal):
  def __init__(self):
    super().__init__(Animal.DOG)


class Cat(Animal):
  def __init__(self):
    super().__init__(Animal.CAT)
  


class Shelter:
  dogs = None
  cats = None
  order = None

  def __init__(self):
    self.order = 0
    self.dogs = []
    self.cats = []

  def __str__(self):
    to_return = 'dogs: ' + str(self.dogs) + '\n'
    to_return += 'cats: ' + str(self.cats)
    return to_return

  def enqueue(self, animal):
    animal.set_arrival_order(self.order)
    self.order += 1
    if animal.is_dog():
      self.dogs.append(animal)
    else:
      self.cats.append(animal)

  def dequeueAny(self):
    if len(self.dogs) and len(self.cats) == 0:
      return 'NO MORE ANIMALS'
    
    if len(self.dogs) == 0:
      return self.cats.pop(0)
    
    if len(self.cats) == 0:
      return self.dogs.pop(0)
    

    oldest_dog = self.dogs[0]
    oldest_cat = self.cats[0]

    if oldest_dog.older_than(oldest_cat):
      return self.dogs.pop(0)
    else:
      return self.cats.pop(0)

  def dequeueDog(self):
    if len(self.dogs) == 0:
      return 'NO MORE DOGS'
    else:
      return self.dogs.pop(0)

  def dequeueCat(self):
    if len(self.cats) == 0:
      return 'NO MORE CATS'
    else:
      return self.cats.pop(0)  


shelter = Shelter()
dog1 = Dog()
dog2 = Dog()
cat1 = Cat()
cat2 = Cat()

shelter.enqueue(dog1)
shelter.enqueue(cat1)
shelter.enqueue(cat2)
shelter.enqueue(dog2)

print(shelter)

print(shelter.dequeueAny())
print(shelter)

print(shelter.dequeueAny())
print(shelter)

print(shelter.dequeueAny())
print(shelter)