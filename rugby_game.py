from enum import Enum


class Marque(Enum):
    DROP = 3
    PENALITE = 3
    ESSAI = 5
    ESSAI_TRANSFORME = 7


class RugbyGame:

    def __init__(self, equipe_1, equipe_2):
        self.equipe_1 = equipe_1
        self.equipe_2 = equipe_2
        self.score_1 = 0
        self.score_2 = 0

    def get_score(self):
        return "{}-{}".format(self.score_1, self.score_2)

    def marque(self, type_score, equipe):
        if equipe == self.equipe_1:
            self.score_1 += type_score.value
        else:
            self.score_2 += type_score.value

    def drop(self, equipe):
        self.marque(Marque.DROP, equipe)

    def penalite(self, equipe):
        self.marque(Marque.PENALITE, equipe)

    def essai(self, equipe):
        self.marque(Marque.ESSAI, equipe)

    def essai_transforme(self, equipe):
        self.marque(Marque.ESSAI_TRANSFORME, equipe)
