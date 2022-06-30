import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):
    pass
    # Test we get the right result string for a final score dictionary representing -
        # Home win
    def test_home_win(self):
        result = {"home_score": 1, "away_score": 0}
        self.assertEqual("Home win", get_result(result))
        # Away win
    def test_away_win(self):
        result = {"home_score": 0, "away_score": 1}
        self.assertEqual("Away win", get_result(result))
        # Draw
    def test_draw(self):
        result = {"home_score": 0, "away_score": 0}
        self.assertEqual("Draw", get_result(result))

    # Test we get right list of result strings for a list of final score dictionaries. 
    def test_results_list(self):
        results = [
        {"home_score": 1, "away_score": 0},
        {"home_score": 0, "away_score": 1},
        {"home_score": 0, "away_score": 0}
        ] 
        self.assertEqual(["Home win", "Away win", "Draw"], get_results(results))

if __name__ == "__main__":
    unittest.main()
