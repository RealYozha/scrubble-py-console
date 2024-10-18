import random


LETTER_SCORES = {
    "А": 1,
    "Б": 3,
    "В": 1,
    "Г": 3,
    "Д": 2,
    "Е": 1,
    "Ё": 3,
    "Ж": 5,
    "З": 5,
    "И": 1,
    "Й": 4,
    "К": 2,
    "Л": 2,
    "М": 2,
    "Н": 1,
    "О": 1,
    "П": 2,
    "Р": 1,
    "С": 1,
    "Т": 1,
    "У": 2,
    "Ф": 10,
    "Х": 5,
    "Ц": 5,
    "Ч": 5,
    "Ш": 8,
    "Щ": 10,
    "Ъ": 10,
    "Ы": 4,
    "Ь": 3,
    "Э": 8,
    "Ю": 8,
    "Я": 3
}


def get_random_letter() -> str:
    all_letters = list(LETTER_SCORES.keys())
    return random.choice(all_letters)


def get_word_with_letter(letter: str) -> str:
    while True:
        chosen_word = input(f"Введите слово на букву {letter}:")
        if chosen_word.upper()[0] == letter:
            print("Слово выбрано.")
            return chosen_word
        else:
            print(f"Слово не начинается на букву {letter}. Введите слово заново.")


def calculate_score(word: str) -> int:
    total_score = 0
    for letter in word:
        total_score += LETTER_SCORES.get(letter.upper(), 0)
    return total_score


def main():
    letter = get_random_letter()
    print(f"Начальная буква: {letter}")
    print("Ход игрока 1!")
    player_one_word = get_word_with_letter(letter)
    print("Ход игрока 2!")
    player_two_word = get_word_with_letter(letter)
    player_one_score = calculate_score(player_one_word)
    player_two_score = calculate_score(player_two_word)
    print(f"Очки игрока 1: {player_one_score}")
    print(f"Очки игрока 2: {player_two_score}")
    if player_one_score > player_two_score:
        print("Победил игрок 1!")
    elif player_two_score > player_one_score:
        print("Победил игрок 2!")
    else:
        print("Ничья")


if __name__ == "__main__":
    main()
