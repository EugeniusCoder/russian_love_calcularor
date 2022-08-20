print("Рассчитываете на взаимность?) Воспользуйтесь калькулятором любви!")
name1 = input("Напишите свои имя и фамилию \n")
name2 = input("Напишите имя и фамилию понравившегося человека \n")

names_together = name1.lower() + name2.lower()

imena_word_i = names_together.count("и")
imena_word_m = names_together.count("м")
imena_word_e = names_together.count("е")
imena_word_n = names_together.count("н")
imena_word_a = names_together.count("а")
lyubvi_word_l = names_together.count("л")
lyubvi_word_yu = names_together.count("ю")
lyubvi_word_b = names_together.count("б")
lyubvi_word_v = names_together.count("в")
lyubvi_word_i = names_together.count("и")

sum_of_imena = imena_word_i + imena_word_m + imena_word_e + imena_word_n + imena_word_a
sum_of_lyubvi = lyubvi_word_l + lyubvi_word_yu + lyubvi_word_b + lyubvi_word_v + lyubvi_word_i

love_score_length = len(str(sum_of_imena) + str(sum_of_lyubvi))

if love_score_length <= 2:
    love_score = int(str(sum_of_imena) + str(sum_of_lyubvi))
else:
    love_score = 0
    for digit in str(sum_of_imena + sum_of_lyubvi):
        love_score += int(digit)

if love_score == 0:
    print(f"Увы, не пара вы( Ваш счет: {love_score}")
elif love_score == 1:
    print(f"Все возможно. Но, возможно, не с этим человеком. Или просто не сейчас. Ваш счет: {love_score}")
elif love_score == 2:
    print(f"Почему бы и нет? - говорит судьба. Ваш счет: {love_score}")
elif love_score == 3:
    print(f"Не торопитесь. Дождитесь звонка или сообщения от вашей симпатии. Ваш счет: {love_score}")
elif love_score == 4:
    print(f"Вам решать, но калькулятор говорит - попробуйте! Ваш счет: {love_score}")
elif love_score == 5:
    print(f"Звезды сошлись, калькулятор сошел с ума! Страстное сочетание! Ваш счет: {love_score}")
elif love_score == 6:
    print(f"Узнайте друг друга получше. И тогда все получится! Ваш счет: {love_score}")
elif love_score == 7:
    print(f"Лавстори. Будет лавстори! Ваш счет: {love_score}")
elif love_score == 8:
    print(f"Калькулятор говорит: вы - пара месяца. А возможно и года! Ваш счет: {love_score}")
elif love_score == 9:
    print(f"Вас ждет чудесная история любви! Ваш счет: {love_score}")
elif 10 <= love_score <= 19:
    print(f"Сама судьба объединяет ваши сердца! Ваш счет: {love_score}")
elif 20 <= love_score <= 29:
    print(f"От вас ждут сообщения, напишите вашей симпатии. Ваш счет: {love_score}")
elif 30 <= love_score <= 39:
    print(f"Это точно мэтч! Ваш счет: {love_score}")
elif 40 <= love_score <= 49:
    print(f"Калькулятор чуть не перегрелся! Вы чудесная пара! Ваш счет: {love_score}")
elif 50 <= love_score <= 59:
    print(f"Скоро вы будете прогуливаться вместе, держась за руки! Ваш счет: {love_score}")
elif 60 <= love_score <= 69:
    print(f"Судя по всему у вас уже скоро появится ваша общая песня! Ваш счет: {love_score}")
elif 70 <= love_score <= 79:
    print(f"Великолепное сочетание. Клубника со сливками! Ваш счет: {love_score}")
elif 80 <= love_score <= 89:
    print(f"Вы вместе как Бонни и Клайд. Опасно, но будоражит! Ваш счет: {love_score}")
elif 90 <= love_score <= 99:
    print(f"Высочайшая степень совпадения. Сама судьба объединяет ваши сердца! Ваш счет: {love_score}")
