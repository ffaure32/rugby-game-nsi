from unittest import TestCase

from rugby_game import RugbyGame


class RugbyGameTest(TestCase):
    def test_init_game(self):
        game = RugbyGame("La Voulte", "Beziers")

        assert game.score() == "0-0"