#Данные
from _ast import While

questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]

counter = 0  # counter - баллы за ответ (10 за один правильный, 0 - за неправильный)
score = 0    # score - количество правильных ответов на вопрос

#Запуск программы

privet_proga = None

while privet_proga != "ready":
    privet_proga = str(input("Привет! Предлагаю проверить свои знания английского! Наберите ready, чтобы начать!\n"))
    if privet_proga != "ready":
        print("Кажется, вы не хотите играть. Очень жаль.")
        break
    else:
        print(" ")


#Вопросы

# questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
# answers = ["is", "am", "in"]

#Вопрос 1

    quest_1 = str(input(questions[0]))
    ask_1 = answers[0]
    ask_true_1 = quest_1 == ask_1
    if ask_true_1:
        counter += 10
        score += 1
        print(f"Ответ верный!\n Вы получаете {counter} баллов")
    if not ask_true_1:
        counter = counter
        score = score
        print(f"Неверно!\n Правильный ответ {ask_1}\n")


#Вопрос 2

    quest_2 = str(input(questions[1]))
    ask_2 = answers[1]
    ask_true_2 = quest_2 == ask_2
    if ask_true_2:
        counter += 10
        score += 1
        print(f"Ответ верный!\n Вы получаете {counter} баллов")
    if not ask_true_2:
        counter = counter
        score = score
        print(f"Неверно!\n Правильный ответ {ask_2}\n")

#Вопрос 3

    quest_3 = str(input(questions[-1]))
    ask_3 = answers[-1]
    ask_true_3 = quest_3 == ask_3
    if ask_true_3:
        counter += 10
        score += 1
        print(f"Ответ верный!\n Вы получаете {counter} баллов")
    if not ask_true_3:
        counter = counter
        score = score
        print(f"Неверно!\n Правильный ответ {ask_3}\n")

# Прощание программы

progress_procent = round(score * 100 / 3)
print(f"Вот и все!")
print(f"Вы ответили на {score} вопросов из 3 верно.")
print(f"Вы заработали {counter} баллов.")
print(f"Это {progress_procent} процентов.")
