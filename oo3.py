# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 13:45:13 2026

@author: User
"""

class student:
    
    class_year=2024
    num_student=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        student.num_student+=1
student1=student("Tesfae",25)
student2=student("mola",30)
student3=student("mola",30)

print(student1.name)
print(student1.age)
print(student1.class_year)
print(student.num_student)

print(f"my graduating class of:{student.class_year} has {student.num_student} of students")
    