'''
import Vache

class VacheALait (Vache):
    RENDEMENT_LAIT:float = 1.1
    PRODUCTION_LAIT_MAX:float=40.0
    laitDisponible:float
    laitTotalProduit:float
    laitTotalTraite:float

    def __init__(self, poids, age):
        super().__init__(self, poids, age)

'''