#!/usr/bin/env python3

import unittest

from scrabble_club.member import Member

class TestMember(unittest.TestCase):

    def test_average_score_is_zero_when_no_games(self):
        member = Member(1, "A", "A")
        self.assertEqual(member.average_score, 0)

    def test_adding_score_updates_average(self):
        member = Member(1, "A", "A")
        member.play_game(100)
        self.assertEqual(member.average_score, 100)
        member.play_game(200)
        self.assertEqual(member.average_score, 150)

    def test_best_score_is_zero_if_no_games(self):
        member = Member(1, "A", "A")
        self.assertEqual(member.best_score, 0)

    def test_best_score_with_one_game(self):
        member = Member(1, "A", "A")
        member.play_game(150)
        self.assertEqual(member.best_score, 150)

    def test_best_score_with_many_games(self):
        member = Member(1, "A", "A")
        member.play_game(150)
        self.assertEqual(member.best_score, 150)
        member.play_game(200)
        self.assertEqual(member.best_score, 200)
        member.play_game(100)
        self.assertEqual(member.best_score, 200)

    def test_repr(self):
        member = Member(1, "Alice", "Ace", [100, 150])
        expected = "Member(member_id=1, name='Alice', nick_name='Ace', games=[100, 150])"
        self.assertEqual(repr(member), expected)

    def test_repr_with_default_games(self):
        member = Member(2, "Bob", "B")
        expected = "Member(member_id=2, name='Bob', nick_name='B', games=[])"
        self.assertEqual(repr(member), expected)

    def test_repr_changes_after_adding_game(self):
        member = Member(3, "Cara", "C")
        before = repr(member)

        member.play_game(120)

        after = repr(member)
        expected_after = "Member(member_id=3, name='Cara', nick_name='C', games=[120])"
        self.assertNotEqual(before, after)
        self.assertEqual(after, expected_after)
        
        