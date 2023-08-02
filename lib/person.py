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
    
    def __init__(self, job, name="Lee"):
        self.name = name
        self.job = job
    
    def get_name(self):
        print('Retrieving name.')
        return self._name

    def set_name(self, name):
        print(f"Setting name to { name }")
        self._name = name
    
    name = property(get_name, set_name)

    def get_job(self):
        print("Retrieving job.")
        return self.__init__job

    def set_job(self, job):
        if job in APPROVED_JOBS: 
            print(f"Setting job to { job }")
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    job = property(get_job, set_job)


person = Person(job="Marketing")
person.job = "Data Science"
