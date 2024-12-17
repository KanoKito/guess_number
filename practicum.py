from random import randint


def guess_the_number():
    # Определяем константы
    MIN_NUMBER = 1
    MAX_NUMBER = 100

    # Получаем случайное число в заданном диапазоне
    number = randint(MIN_NUMBER, MAX_NUMBER)
    print(f'Угадайте число от {MIN_NUMBER} до {MAX_NUMBER}')

    attempts = 0  # Счетчик попыток

    while True:
        try:
            # Получаем число от пользователя и сохраняем его в переменную.
            guess = int(input('Введите число: '))
            attempts += 1  # Увеличиваем счетчик попыток

            # Проверяем диапазон введенного числа
            if guess < MIN_NUMBER or guess > MAX_NUMBER:
                print(
                    f'Пожалуйста, введите число в диапазоне от'
                    f'{MIN_NUMBER} до {MAX_NUMBER}.'
                    )
                continue

            # Если число меньше загаданного...
            if guess < number:
                print('Ваше число меньше того, что загадано.')

            # Если число больше загаданного...
            elif guess > number:
                print('Ваше число больше того, что загадано.')

            # Если число угадано...
            else:
                print(
                    f'Отличная интуиция!' 
                    f'Вы угадали число за {attempts} попыток :)'
                    )
                break

        except ValueError:
            print('Пожалуйста, введите корректное целое число.')


# Запускаем игру
guess_the_number()
