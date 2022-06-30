import unittest

from src.compound_interest import CompoundInterest

class CompoundInterestTest(unittest.TestCase):

    # Tests
    def test_compound_interest(self):

    # Should return 732.81 given 100 principal, 10 percent, 20 years
        self.assertEqual(732.81, CompoundInterest.do_compound_interest(100, 0.1, 20))

    # Should return 181.94 given 100 principal, 6 percent, 10 years
        self.assertEqual(181.94, CompoundInterest.do_compound_interest(100, 0.06, 10))

    # Should return 149,058.55 given 100000 principal, 5 percent, 8 years
        self.assertEqual(149058.55, CompoundInterest.do_compound_interest(100000, 0.05, 8))

    # Should return 0.00 given 0 principal, 10 percent, 1 year
        self.assertEqual(0.00, CompoundInterest.do_compound_interest(0, 0.1, 1))

    # Should return 100.00 given 100 principal, 0 percent, 10 years
        self.assertEqual(100.00, CompoundInterest.do_compound_interest(100, 0, 10))


    # Extention tests
    def test_compound_interest_with_monthly_contribution(self):


    # Should return 118,380.16 given 100 principal, 5 percent, 8 years, 1000 per month
        self.assertEqual(118380.16, CompoundInterest.compound_interest_with_monthly_contribution(100, 0.05, 8, 1000))
    # Should return 156,093.99 given 100 principal, 5 percent, 10 years, 1000 per month
        self.assertEqual(156093.99, CompoundInterest.compound_interest_with_monthly_contribution(100, 0.05, 10, 1000))
    # Should return 475,442.59 given 116028.86, 7.5 percent, 8 years, 2006 per month
        self.assertEqual(475442.59, CompoundInterest.compound_interest_with_monthly_contribution(116028.86, 0.075, 8, 2006))
    
    # Should return 718,335.96 given 116028.86 principal, 9 percent, 12 years, 1456 per month
        self.assertEqual(718335.96, CompoundInterest.compound_interest_with_monthly_contribution(116028.86, 0.09, 12, 1456))

