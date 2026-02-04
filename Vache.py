from InvalidVacheException import InvalidVacheException
import itertools


class vache:
    id_iter = itertools.count()
    AGE_MAX = 25
    POIDS_MAX = 1000.0
    PANSE_MAX = 50.0
    POIDS_MIN_PANSE = 2.0
    petitNom:str
    poids:float
    panse:float
    age:int
    RENDEMENT_RUMINATION:float=0.25

    def __init__(self, petitNom, age, poids):
        self.petitNom = petitNom
        self.age = age
        self.poids = poids
        self.id = next(self.id_iter)
        self.valider_etat()

    def __str__(self):
        return print(f"{self.id} La vache {self.petitNom} a {self.age} et pèse {self.poids}" )
    
    def valider_etat (self):
        if self.petitNom.isspace() or self.petitNom == "" or self.age <= 0 or self.poids <= 0 or self.poids > self.POIDS_MAX:
            raise InvalidVacheException(f"La vache {self.id} n'est pas valide")
        
v= vache(" ", 20, 43.0)
v.__str__()

a= vache("ay", 20, 43.0)
a.__str__()