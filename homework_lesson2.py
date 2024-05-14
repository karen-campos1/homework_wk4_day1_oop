# Task 1: Vehicle Registration System

# Problem Statement: Create a Python class Vehicle with attributes
# registration_number, type, and owner. Implement a method update_owner to change the vehicle's owner. 
# Then, create a few instances of Vehicle and demonstrate changing the owner.
# Code Example: Provide a basic structure for the Vehicle class without methods.


class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner
        
    def change_owner(self, owner):
        self.owner = owner
        print(f"You have successfully changed ownership to {owner}.")
        
        
vehicle1 = Vehicle('0328565', 'Kia', 'Natalie')
vehicle2 = Vehicle('8562561', 'Tesla', 'Felix')
print(vehicle1.registration_number)
print(vehicle1.type)
print(vehicle1.owner)
vehicle1.change_owner("Bob")
print(vehicle1.owner)
print(vehicle2.registration_number)
print(vehicle2.type)
print(vehicle2.owner)




# Task 2: Event Management System Enhancement

# Problem Statement: Extend an existing Event class by adding a feature to keep track
# of the number of participants. Implement a method add_participant that increases the count 
# and a method get_participant_count to retrieve the current count.
# Code Example: Basic Event class without participant tracking.


class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participants = []
        
        
    def add_participant(self, name):
        self.participants.append(name)
        print(self.participants)
        
    def get_participant_count(self):
        return len(self.participants)

participant1 = Event("Ashley", "Aug 13th")  #i dont know what these attributes are for (they were part of the hw problem) * but my code runs.
participant1.add_participant("Henry")
participant1.add_participant("Bob")
print(participant1.get_participant_count())