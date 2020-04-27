import numpy as np

def game_core_v3(number):
    '''
    Функция, которая на входе принимает число и возвращает количество попыток, за которое она его "угадывает".
    Входной параметр: целое число в диапазоне от 1 до 100 (не проверяется!), которое ф-ия должна "угадать".
    Выходной параметр: целое число - кол-во попыток, за которое получилось "угадать" входной параметр.
    '''
    maximum = 100    # Максимум диапазона, в котором "угадываем"
    minimum = 1      # Минимум диапазона, в котором "угадываем"
    count = 0        # Инициализируем переменную-счётчик попыток
    x = 0            # Переменная, которую будем сравнивать с искомым числом

    while x != number:
        
        # Делим диапазон условно пополам и определяем нижнюю и верхнюю границы обоих "половинок"; увеличиваем счётчик
        upper_top    = maximum
        lower_top    = minimum + (maximum - minimum) // 2
        upper_bottom = lower_top - 1
        lower_bottom = minimum
        count += 1

        if number in range(lower_top, upper_top + 1):
            if upper_top - lower_top > 1:                     # Искомое число в верхнем диапазоне и диапазон не из 2 цифр
                minimum = lower_top
                maximum = upper_top
            else:                                             # Диапазон из 2 цифр: одна из цифр - угадываемая
                if number == lower_top: x = lower_top
                else: x = upper_top

        elif number in range(lower_bottom, upper_bottom + 1): # Искомое число в нижнем диапазоне и диапазон не из 2 цифр
            if upper_bottom - lower_bottom > 1:
                minimum = lower_bottom
                maximum = upper_bottom
            else:                                             # Диапазон из 2 цифр: одна из цифр - угадываемая
                if number == lower_bottom: x = lower_bottom
                else: x = upper_bottom

        else:
            print('Error: Unexpected number in "game_core_v3()" function!')   # На всякий случай :)
            break
        
    return(count)
        

        
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
#     np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(game_core(number))
    
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    
    return(score)



# Проверяем
score_game(game_core_v3)