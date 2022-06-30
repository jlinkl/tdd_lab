import unittest

from src.high_scores import latest, personal_best, personal_top_three
from src.high_scores import highest_to_lowest

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    def setUp(self):
        self.scores = [50, 75 ,46, 54, 31]
        self.scores_equal = [50, 50, 50, 50, 50]
        self.scores_two = [50, 75]
        self.one_score = [75]
    # Tests

    # Test latest score (the last thing in the list)
    def test_latest_score(self):
        self.assertEqual(31, latest(self.scores))
    # Test personal best (the highest score in the list)
    def test_personal_best(self):
        self.assertEqual(75, personal_best(self.scores))
    # Test top three from list of scores
    def test_top_three(self):
        self.assertEqual([75, 54, 50], personal_top_three(self.scores))
    # Test ordered from highest tp lowest
    def test_highest_to_lowest(self):
        self.assertEqual([75, 54, 50, 46, 31], highest_to_lowest(self.scores))
    # Test top three when there is a tie
    def test_top_three_when_tied(self):
        self.assertEqual([50, 50, 50], personal_top_three(self.scores_equal))
    # Test top three when there are less than three
    def test_top_two(self):
        self.assertEqual([75, 50], personal_top_three(self.scores_two))
 # Test top three when there is only one
    def test_top_one(self):
        self.assertEqual([75], personal_top_three(self.one_score))
