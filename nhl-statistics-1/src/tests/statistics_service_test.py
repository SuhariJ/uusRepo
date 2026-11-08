import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):

        self.stats = StatisticsService(
            PlayerReaderStub()
        )

        self.players = PlayerReaderStub().get_players()

    def test_search(self):
        player = self.stats.search("Semenko")
        self.assertEqual(player.name, "Semenko")
        self.assertEqual(self.stats.search("jaakko"), None)

    def test_team(self):

        self.assertEqual(len(self.stats.team("EDM")), 3)
        self.assertEqual(len(self.stats.team("MDO")), 0)

    def test_top(self):

        top = self.stats.top(2)
        self.assertEqual(top[0].name, "Gretzky")

        top_neg = self.stats.top(-1)
        self.assertEqual(len(top_neg), 0)