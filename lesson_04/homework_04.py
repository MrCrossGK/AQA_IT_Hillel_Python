adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
# print(adwentures_of_tom_sawer, "\n")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
# print(adwentures_of_tom_sawer) # Додав прінти для наглядності змін і розуміння того що коїться зі змінною в процессі того як ми її редагуємо

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ") # Заміняємо "...." на 1 пробіл
# print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.strip() # Прибираємо на всяк випадок усі можливі пробіли в початку і кінці строки, хоча в конкретно данному випадку воно не потрібно
adwentures_of_tom_sawer = adwentures_of_tom_sawer.split() # Перетворюємо стрінг у списокб тим самим прибираючи зайві пробіли
adwentures_of_tom_sawer = ' '.join(adwentures_of_tom_sawer) # Ну і складаємо все назад де вже все гарно виглядатиме з 1 пробілом між кожним словом
# adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split()) # Зробив те саме але в більш короткій формі і як бачимо .strip() не знадобилось
# print(adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
h_count = adwentures_of_tom_sawer.count("h") # Просто порахував за допомогою метода .count()
print(f"У тексті 'adwentures_of_tom_sawer' літера \"h\" зустрічається {h_count} разів.\n")
# h_count_2 = 0
# for i in adwentures_of_tom_sawer:
#     if i == "h":
#         h_count_2 += 1
# print(f"У тексті 'adwentures_of_tom_sawer' літера \"h\" зустрічається {h_count_2} разів.") # В принципі те саме тільки через цикл, як раз перевірили що каунт відпрацював правильно


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
title_count = 0 # Лічильник слів у тексті що починаються з Великої літери
for i in adwentures_of_tom_sawer: # Цикл де перебираєм всі літери
    if i.istitle(): # Перевірка, якщо літера велика то..
        title_count += 1 # .. то дадємо +1 до лічильника
print(f"У тексті 'adwentures_of_tom_sawer' {title_count} слів починається з Великої літери.\n") # В принципі той самий цикл що в попередньому завданні, але перевірка інша

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
index_tom = adwentures_of_tom_sawer.find("Tom") # Знаходимо перше входження "Tom"
second_index = adwentures_of_tom_sawer.find("Tom", index_tom + 1) # Шукаємо друге входження "Tom" додаючи до стартового індекса пошуку, перше входження де знайшло "Tom" + 1
print(f"Позиція, на якій слово Tom зустрічається вдругe: {second_index}\n")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
dot_numb = adwentures_of_tom_sawer.count(".") # Рахуємо всі точки в тексті
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(".", dot_numb - 1) # Додаємо додатковий параметр, на максимальну кількість розділень, бо якщо цього не зробити після останньої крапки він нам видасть пусті лапки
print(adwentures_of_tom_sawer_sentences, f"\n")

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print((adwentures_of_tom_sawer_sentences[3]).lower(), f"\n") # Так як відрахування іде з нуля то четверте речення буде з індексом 3, ну а метод .lower() робить нижній регістр

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for i in adwentures_of_tom_sawer_sentences: # Перебираємо кожне речення
    if (i.strip()).startswith("By the time"): # Кожний елемент стріпаємо щоб впевнетись що на початку і кінці речення не було пробілів
        print("Так якесь речення починається з 'By the time'\n")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sent_index = len(adwentures_of_tom_sawer_sentences) - 1 # Визначаємо індекс останнього речення, та мінусуємо 1 бо відлік починається з 0
last_sent_len = len((adwentures_of_tom_sawer_sentences[last_sent_index]).split()) # Беремо останнє речення підставляючи його індекс, розділяємо за допомогою split() і виводимо кількість слів
print(f"Кількість слів останнього речення з adwentures_of_tom_sawer_sentences складає - {last_sent_len}.")
