# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 13:28:02 2026

@author: User
"""

class car:
    def __init__(self,model,year,color,for_sale):
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale
        
    def drive(self):
        print(f"you drive the car:{self.model}")
    def stop(self):
         print(f"you stop the car:{self.model}")