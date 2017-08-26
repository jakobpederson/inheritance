import unittest
from inheritance import Karjo, Khajit, Miraak, Nord


class TestInheritance(unittest.TestCase):

    def test_override(self):
        char = Karjo()
        khajit = Khajit()
        self.assertEqual('thief', khajit.get_occupation())
        self.assertEqual('guard', char.get_occupation())

    def test_extend(self):
        char = Karjo()
        self.assertEqual("khajit extension", char.get_race())

    def test_miraak(self):
        char = Miraak()
        nord = Nord()
        self.assertEqual("nord extension of skyrim", nord.get_race)
        self.assertEqual("immortal nord extension of skyrim", char.get_race())
