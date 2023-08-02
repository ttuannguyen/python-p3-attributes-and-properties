#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    
    def __init__(self, name="Trenton"):
        self.name = name
    
    def get_name(self):
        print('Retrieving name.')
        return self._name

    def set_name(self, name):
        print(f"Setting name to { name }")
        self._name = name
    
    name = property(get_name, set_name)


person = Person(job="programmer")

