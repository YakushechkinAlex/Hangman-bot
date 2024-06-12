import telebot
from random import choice

TOKEN = 'Token_id'
bot = telebot.TeleBot(TOKEN)

# Reading words from file
try:
    with open('new.txt', 'r', encoding='utf-8') as f:
        words = [line.strip() for line in f.readlines() if line.strip()]
except FileNotFoundError:
    print("Файл 'words.txt' не найден. Используется стандартный список слов.")
    words = ('питон', 'игра', 'енот')  # Backup words

# ASCII image of a hangman
hangman_pics = (
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
| 
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\ 
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\ 
|   | 
|   | 
|  /
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\ 
|   | 
|   | 
|  / \\
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\ 
|   | 
|   | 
|  / \\
|  | 
|
--------
"""
)


# Словарь для хранения состояний игр всех пользователей
games = {}



def new_game(user_id):
    # creating new game
    word = choice(words)
    games[user_id] = {
        'word': word,
        'so_far': '_' * len(word),
        'wrong': 0,
        'used': []
    }
    return games[user_id]


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Напиши /play чтобы начать игру в Виселицу.")


@bot.message_handler(commands=['play'])
def play(message):
    game = new_game(message.chat.id)
    display_game(message.chat.id, game)


# Links to images
hangman_images = [
    'body1.jpg',
    'body2.jpg',
    'body3.jpg',
    'body4.jpg',
    'body5.jpg',
    'body6.jpg',
    'body7.jpg',
    'body8.jpg',
    'body9.jpg',
    'body10.jpg'
]


def display_game(user_id, game):
    # Game display for a user
    hangman = hangman_pics[game['wrong']]  # ASCII image
    image_path = hangman_images[game['wrong']]  # Image
    # Sending image to a user
    with open(image_path, 'rb') as photo:
        bot.send_photo(user_id, photo)
    so_far = ' '.join(game['so_far'])
    used = ', '.join(game['used'])

    # Sending ASCII image
    bot.send_message(user_id, f"\nСлово: {so_far}\nИспользованные буквы: {used}\nВведите букву:")




@bot.message_handler(func=lambda message: message.chat.id in games)
def handle_guess(message):
    game = games[message.chat.id]
    guess = message.text.strip().lower()

    if len(guess) != 1 or not guess.isalpha():
        bot.reply_to(message, "Пожалуйста, введите одну русскую букву.")
        return

    if guess in game['used']:
        bot.reply_to(message, "Эту букву вы уже использовали!")
        return

    game['used'].append(guess)

    if guess in game['word']:
        new_so_far = ''.join(
            [guess if game['word'][i] == guess else game['so_far'][i] for i in range(len(game['word']))])
        game['so_far'] = new_so_far

        if '_' not in new_so_far:
            bot.send_message(message.chat.id, f"Поздравляем! Вы угадали слово: {game['word']}")
            del games[message.chat.id]
        else:
            display_game(message.chat.id, game)
    else:
        game['wrong'] += 1
        if game['wrong'] >= len(hangman_pics):
            bot.send_message(message.chat.id, f"Вы проиграли. Загаданное слово было: {game['word']}")
            del games[message.chat.id]
        else:
            display_game(message.chat.id, game)


if __name__ == '__main__':
    bot.polling()
