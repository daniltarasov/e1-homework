import random
import mock

WORDS = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
ATTEMPTS = 4


class Hangman():
    def __init__(self):
        self.user_mistakes = 0
        self.used_letters = []
        self.secret_word = random.choice(WORDS)
        self.gamer_word = ['_'] * len(self.secret_word)
        self.is_lost = False
        self.is_won = False

    def input_letter(self):
        while True:
            letter = input("Введите букву латинского алфавита: ")
            if self.valid_letter(letter):
                break
        return letter

    def valid_letter(self, letter):
        if len(letter) == 1 and ((65 <= ord(letter) <= 90) or (97 <= ord(letter) <= 122)) \
        and letter.lower() not in self.used_letters:
            return True
        elif len(letter) != 1:
            print(f'Требуется один символ!')
        elif letter.lower() in self.used_letters:
            print(f'буква "{letter}" уже была!')
        elif not letter.isalpha():
            print(f'"{letter}" не буква!')
        elif not (65 <= ord(letter) <= 90) or (97 <= ord(letter) <= 122):
            print(f'буква "{letter}" не из латинского алфавита!')
        return False
    
    def check_letter(self, letter):
        letter_lower = letter.lower()
        self.used_letters.append(letter_lower)
        if letter_lower in self.secret_word.lower():
            for pos, char in enumerate(self.secret_word.lower()):
                if char == letter_lower:
                    self.gamer_word[pos] = letter_lower
        else:
            self.user_mistakes +=1

    def end_game(self):
        if self.user_mistakes >= ATTEMPTS:
            self.is_lost = True
            return True

        if '_' in self.gamer_word:
            return False
        else:
            self.is_won = True
            return True

    def play(self):
        # print(self.secret_word)
        print(f'Угадайте слово. У вас {ATTEMPTS} попытки.')
        while not self.end_game():
            print(' '.join(self.gamer_word))
            # print(f"Попыток осталось: {ATTEMPTS - user_mistakes}, пробовали буквы: {','.join(used_letters)}")
            print(f"Штрафных очков: {self.user_mistakes}, пробовали буквы: {','.join(self.used_letters)}")
            letter = self.input_letter()
            self.check_letter(letter)
        if self.is_won:
            print(' '.join(self.gamer_word))
            print('Ура, Вы выиграли!')
        elif self.is_lost:
            print(f"Штрафных очков: {self.user_mistakes}. Увы, Вы проиграли :(.")


def main():
    hangman = Hangman()
    hangman.play()


if __name__ == "__main__":
    main()