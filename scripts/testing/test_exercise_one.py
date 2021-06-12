import unittest

import sys
sys.path.append("..")
from scripts import exercise_one

class Testing(unittest.TestCase):

    def test_results(self):
        self.assertNotEqual(exercise_one.pattern_count(),2)
        self.assertNotEqual(exercise_one.pattern_count(),'Huffington Post')
        self.assertNotEqual(exercise_one.pattern_count(),'https://myentorno.pdf')
