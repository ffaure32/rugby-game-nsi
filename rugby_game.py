class RugbyGame:

    def __init__(self, equipe_1, equipe_2):
        self.equipe_1 = equipe_1
        self.equipe_2 = equipe_2
        self.score_1 = 0
        self.score_2 = 0

    def get_score(self):
        return "{}-{}".format(self.score_1, self.score_2)

    def drop(self, equipe):
        if equipe == self.equipe_1:
            self.score_1 += 3
        else:
            self.score_2 += 3

    def penalite(self, equipe):
        if equipe == self.equipe_1:
            self.score_1 += 3
        else:
            self.score_2 += 3
