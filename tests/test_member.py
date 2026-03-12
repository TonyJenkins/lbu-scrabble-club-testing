#!/usr/bin/env python3

import unittest

from scrabble_club.member import Member

class TestMember(unittest.TestCase):

    def test_average_score_is_zero_when_no_games(self):
        member = Member(1, "A", "A")
        self.assertEqual(member.average_score, 0)
