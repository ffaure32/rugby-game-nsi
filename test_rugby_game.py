from unittest import TestCase

from rugby_game import RugbyGame


class RugbyGameTest(TestCase):

    def setUp(self):
        self.game = RugbyGame("UBB", "Toulouse")

    def test_init_game(self):

        assert self.game.get_score() == "0-0"

    def test_drop_de_jalibert(self):
        self.game.drop("UBB")

        assert self.game.get_score() == "3-0"

    def test_drop_de_ntamack(self):
        self.game.drop("Toulouse")

        assert self.game.get_score() == "0-3"

    def test_drop_des_grandisse(self):
        self.game.drop("Toulouse")
        self.game.drop("UBB")

        assert self.game.get_score() == "3-3"

    def test_penalite(self):
        self.game.penalite("UBB")

        assert self.game.get_score() == "3-0"
