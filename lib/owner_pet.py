class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of Pet")
        pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"pet_type must be one of {Pet.PET_TYPES}")
        self.name = name
        self.pet_type = pet_type
        self.owner = None
        if owner is not None:
            if not isinstance(owner, Owner):
                raise Exception("owner must be an instance of Owner")
            owner.add_pet(self)
        Pet.all.append(self)

owner1 = Owner("Alice")
pet1 = Pet("Fluffy", "cat", owner1)
pet2 = Pet("Buddy", "dog", owner1)
pet3 = Pet("Whiskers", "rodent")

owner2 = Owner("Bob")
owner2.add_pet(pet3)

print(owner1.pets())  
print(owner2.pets()) 
print(owner1.get_sorted_pets())  
