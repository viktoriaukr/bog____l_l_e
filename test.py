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
            self.assertIn('board', session)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<div>TImer: <span class="timer"></span></div>', html)


    def test_submit_guess_invalid_word(self):
        with app.test_client() as client:
            client.get('/')
            response = client.get('/submit-guess?word=invalid&board=example_board')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['result'], 'not-on-board')




