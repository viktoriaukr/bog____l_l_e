from boggle import Boggle
from flask import Flask, render_template, session, request, jsonify
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_key596'
debug = DebugToolbarExtension(app)


boggle_game = Boggle()

@app.route('/')
def board():
    board = boggle_game.make_board()
    session['board'] = board
    score = session.get('score', 0)
    return render_template('base.html', board=board, score=score)

@app.route('/submit-guess')
def submit_guess():
    
    word = request.args['word']
    board = session['board']

    word = boggle_game.check_valid_word(board, word) 
    
    return jsonify({'result': word})

    
