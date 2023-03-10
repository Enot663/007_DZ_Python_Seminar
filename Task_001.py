# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.
# Стихотворение Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и 
# “Пам парам”, если с ритмом все не в порядке

# Пример:

# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-дам
# Вывод:
# Парам пам-пам


puffing = input('Введите проверяемую фразу: ') # приглашение пользователю на ввод
lines = puffing.lower().split() # преобразовывваем текст в нижний регистр и разбиваем на строки
f = lambda x: sum(1 for i in x if i in 'аеёиоуыэюя') # производим подсчет гласных букв фразы
t = f(lines[0]) # присваиваем переменной значение количества гласных в первой строке

if ([f(i) == t for i in lines]): # цикл сравненич количества гласных по строкам
    print('Парам пам-пам') # вывод фразы при совпадении
else:
    print('Пам парам') # иначе
