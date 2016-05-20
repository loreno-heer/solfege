# Solfege - free ear training software
# Copyright (C) 2007, 2008, 2011, 2016 Tom Cato Amundsen
# License is GPL, see file COPYING

import unittest
from solfege.mpd.mpdutils import find_possible_first_note


class TestMpdUtils(unittest.TestCase):

    def test_1(self):
        self.assertEqual((0, 1), find_possible_first_note("d e"))
        self.assertEqual((1, 3), find_possible_first_note("<d'4 e>"))
        self.assertEqual((11, 12), find_possible_first_note(r"\clef bass <3X d'4 e>"))
        self.assertEqual((12, 14), find_possible_first_note(r"\clef bass <d'4 e>"))
        self.assertEqual((10, 12), find_possible_first_note(r"\time 3/4 d'4 e "))
        self.assertEqual((13, 15), find_possible_first_note(r"\times 3/4 { d'4 e }"))
        self.assertEqual((1, 2), find_possible_first_note(r"[c8 d]"))

suite = unittest.makeSuite(TestMpdUtils)
