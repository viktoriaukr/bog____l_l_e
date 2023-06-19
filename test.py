from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

app.config['TESTING'] = True


class FlaskTests(TestCase):

    def test_board(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<div>TImer: <span class="timer"></span></div>', html)



    def test_check_valid_word(self):
        boggle_game = Boggle()
        board = [
            ['A', 'B', 'C', 'D'],
            ['E', 'F', 'G', 'H'],
            ['I', 'J', 'K', 'L'],
            ['M', 'N', 'O', 'P']
        ]
        word = 'DOG'
        result = boggle_game.check_valid_word(board, word)
        self.assertEqual(result, 'not-on-board')



    def test_check_valid_word_2(self):
        boggle_game = Boggle()
        board = [
            ['A', 'B', 'C', 'D'],
            ['E', 'F', 'G', 'H'],
            ['I', 'J', 'K', 'L'],
            ['M', 'N', 'O', 'P']
        ]
        word = 'XYZ'
        result = boggle_game.check_valid_word(board, word)
        self.assertEqual(result, 'not-on-board')
