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

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search(self):
        player = self.stats.search("Lemieux")
        self.assertEqual(player.name, "Lemieux")
        self.assertAlmostEqual(player.goals, 45)

    def test_failed_search(self):
        player = self.stats.search("Nobody")
        self.assertIsNone(player)

    def test_team(self):
        team = self.stats.team("PIT")
        self.assertEqual(team[0].name, "Lemieux")
        self.assertAlmostEqual(len(team), 1)

    def test_top(self):
        best = self.stats.top(2)
        self.assertEqual(best[0].name, "Gretzky")
        self.assertEqual(best[1].assists, 54)
