# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 11:59:53 2026

@author: User
"""
#multiple inheritance
class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleaping")
class prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeang")

class predetur(Animal):
    def hunt(self):
        print(f" {self.name} is hunting")

class rabit(prey):
    pass
class hawk(predetur):
    pass
class fish(prey ,predetur):
    pass

rabit=rabit("bugs")
hawk=hawk("likens")
fish=fish("cacat")

rabit.sleep()
hawk.hunt()
fish.flee()
fish.hunt()
