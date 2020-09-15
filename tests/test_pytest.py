import pytest
from hangman import Hangman, WORDS, ATTEMPTS
import mock 

def test_init():
    hangman = Hangman()
    assert hangman.secret_word in WORDS
    assert len(hangman.gamer_word) == len(hangman.secret_word)

@pytest.mark.parametrize('letter', ['a', 'A', 'z', 'Z'])
def test_valid_letter(letter):
    hangman = Hangman()
    valid_letter = hangman.valid_letter(letter)
    assert valid_letter

@pytest.mark.parametrize('letter', ['1', '', '.', 'ы', 'Ы', ' ', 'ss'])
def test_invalid_letter(letter):
    hangman = Hangman()
    valid_letter = hangman.valid_letter(letter)
    assert not valid_letter

@pytest.mark.parametrize('letter', ['a', 'A', 'z', 'Z'])
def test_input(letter):
    hangman = Hangman()
    with mock.patch('builtins.input') as input_mock:
        input_mock.return_value = letter
        leter_returned = hangman.input_letter()
    assert leter_returned == letter

def test_check_letter_success():
    hangman = Hangman()
    hangman.check_letter(hangman.secret_word[0].capitalize())
    letter_lower = hangman.secret_word[0].lower()
    assert letter_lower in hangman.used_letters
    assert hangman.gamer_word[0] == letter_lower
    assert hangman.user_mistakes == 0

def test_check_letter_success_testword():
    hangman = Hangman()
    hangman.secret_word = 'Abracadabra'
    hangman.gamer_word = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',]
    hangman.check_letter('a')
    assert hangman.gamer_word == ['a', '_', '_', 'a', '_', 'a', '_', 'a', '_', '_', 'a',]
    assert 'a' in hangman.used_letters
    assert hangman.user_mistakes == 0


def test_check_letter_not_success():
    hangman = Hangman()
    letter_not_in = ""
    for i in range(97, 123):
        if chr(i) not in hangman.secret_word.lower():
            letter_not_in = chr(i)
            break
    hangman.check_letter(letter_not_in)
    assert letter_not_in in hangman.used_letters
    assert letter_not_in not in hangman.gamer_word
    assert hangman.user_mistakes == 1

def test_valid_letter_is_repeated():
    hangman = Hangman()
    hangman.check_letter(hangman.secret_word[0])
    valid_letter = hangman.valid_letter(hangman.secret_word[0])
    assert not valid_letter

def test_end_game_loose():
    hangman = Hangman()
    hangman.user_mistakes = ATTEMPTS
    assert hangman.end_game()
    assert not hangman.is_won
    assert hangman.is_lost

def test_end_game_win():
    hangman = Hangman()
    hangman.user_mistakes = ATTEMPTS - 1
    hangman.gamer_word = list(hangman.secret_word)
    assert hangman.end_game()
    assert hangman.is_won
    assert not hangman.is_lost

def test_end_game_loose_not_win():
    hangman = Hangman()
    hangman.user_mistakes = ATTEMPTS
    hangman.gamer_word = list(hangman.secret_word)
    assert hangman.end_game()
    assert not hangman.is_won
    assert hangman.is_lost

def test_end_game_in_process():
    hangman = Hangman()
    hangman.user_mistakes = ATTEMPTS - 1
    hangman.check_letter(hangman.secret_word[0])
    assert not hangman.end_game()

