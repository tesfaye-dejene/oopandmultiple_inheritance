# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 13:12:58 2026

@author: User
"""
from oo2 import car

car1=car("tesla",2026,"black",False)
car2=car("tesla",2026,"black",False)
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

        
car1.drive()
car2.stop()