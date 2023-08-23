import random

def print_hangman(lives):
    """ Выводит изображение виселицы """
    if lives == 10:
        print("  _______")
        print(" |/      |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("_|___")
    elif lives == 9:
        print("  _______")
        print(" |/      |")
        print(" |      (_)")
        print(" |")
        print(" |")
        print(" |")
        print("_|___")
    elif lives == 8:
        print("  _______")
        print(" |/      |")
        print(" |      (_)")
        print(" |       |")
        print(" |")
        print(" |")
        print("_|___")
    elif lives == 7:
        print("  _______")
        print(" |/      |")
        print(" |      (_)")
        print(" |       |")
        print(" |      /")
        print(" |")
        print("_|___")
    elif lives == 6:
        print("  _______")
        print(" |/      |")
        print(" |      (_)")
        print(" |       |")
        print(" |      / \\")
        print(" |")
        print("_|___")
    elif lives == 5:
        print("  _______")
        print(" |/      |")
        print(" |      (_)")
        print(" |      /|\\")
        print(" |       |")
        print(" |")
        print("_|___")
    elif lives == 4:
        print("  _______")
        print(" |/      |")
        print(" |      (_)")
        print(" |      /|\\")
        print(" |       |")
        print(" |      /")
        print("_|___")
    elif lives == 3:
        print("  _______")
        print(" |/      |")
        print(" |      (_)")
        print(" |      /|\\")
        print(" |       |")
        print(" |      / \\")
        print("_|___")
    elif lives == 2:
        print("  _______")
        print(" |/      |")
        print(" |     (o_o)")
        print(" |      /|\\")
        print(" |       |")
        print(" |      / \\")
        print("_|___")
    elif lives == 1:
        print("  _______")
        print(" |/      |")
        print(" |     (x_o)")
        print(" |      /|\\")
        print(" |       |")
        print(" |      / \\")
        print("_|___")
    else:
        print("  _______")
        print(" |/      |")
        print(" |     (x_x)")
        print(" |      /|\\")
        print(" |       |")
        print(" |      / \\")
        print("_|___")

def get_word():
    """ Возвращает случайное слово из списка """
    words = ["автомобиль", "библиотека", "вокзал", "горизонт", "дерево", "ежевика", "железная", "зимовка", "ирис", "корабль", "лавина", "музыка", "небоскреб", "облако", "программа", "самолет", "телевизор", "успех", "фонарь", "холодильник", "цветок", "чайник", "шахматы", "щенок", "электроника", "ювелирный", "яхта"]
    return random.choice(words)

def display_word(word, guessed_letters):
    """ Выводит текущее состояние угаданного слова """
    for letter in word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

def game():
    """ Запускает игру """
    print("Игра 'Виселица' началась!")
    print("Введите '+', чтобы получить новое слово")
    print("Введите '!', чтобы завершить игру")
    # Получение случайного слова
    word = get_word()
    # Множество для вводимых букв
    guessed_letters: set = set()
    # Количество жизней
    lives = 10

    while lives > 0:
        # Показ виселицы
        print_hangman(lives)
        # Текущее состояние угадываемого слова
        display_word(word, guessed_letters)

        # Ввод буквы пользователем
        guess = input("Введите букву или +/!: ").lower()
          
        # Если пользователь нажал на кнопку "+", то получаем новое слово
        if guess == '+':
            word = get_word()
            guessed_letters.clear()
            print("Новое слово загадано. Продолжайте игру!")
            continue

        # Если пользователь нажал на кнопку "!", заканчиваем игру и закрываем окно
        if guess == '!':
            print("Вы завершили игру.")
            break
        
        # Если пользователь уже выиграл игру, то не запрашиваем у него новую букву
        if set(word) <= guessed_letters:
            continue
        
        # Проверка, что введена только одна буква
        if len(guess) != 1:
            print("Вы должны ввести только одну букву.")
            continue

        # Проверка, что пользователь ввел букву
        if not guess.isalpha():
            print("Вы должны ввести букву.")
            continue

        # Проверка, что буква еще не была введена
        if guess in guessed_letters:
            print("Вы уже угадывали эту букву.")
            continue

        # Добавление введенной буквы в множество
        guessed_letters.add(guess)

        # Есть ли введенная буква в слове
        if guess not in word:
            # Если буквы нет
            lives -= 1
            print("Такой буквы в слове нет.")
            continue

        # Угаданы все буквы
        if set(word) <= guessed_letters:
            print_hangman(lives)
            display_word(word, guessed_letters)
            print("Поздравляем, вы выиграли!")
    # Закончились жизни
    else:
        print_hangman(lives)
        print(f"К сожалению, вы проиграли. Загаданное слово было '{word}'.")
        
game()