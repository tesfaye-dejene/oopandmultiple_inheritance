# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 14:06:37 2026

@author: User
"""

class animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True
    def eating(self):
        print(f"{self.name}:  is eating")
    def sleap(self):
        print(f"{self.name}: is sleaping")
        
class dog(animal):
    def speak(self):
        print("woof!")

class cat(animal):
   def speak(self):
       print("meaw!")

class mouse(animal):
    def speak(self):
        print(f"{self.name}:katkat!")

dog=dog("rocki")
cat=cat("bala")
mouse=mouse("leba")


print(dog.name)
print(dog.is_alive)

dog.eating()
cat.sleap()
mouse.speak()



