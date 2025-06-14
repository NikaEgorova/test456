
txt_index = "Ваш індекс Руф'є: "
txt_workheart = "Працездатність серця: "
txt_nodata = " Немає даних для такого віку"
txt_res = []
txt_res.append(""" Низька. Терміново зверніться до лікаря! """)
txt_res.append(""" Задовільна. Зверніться до лікаря! """)
txt_res.append(""" Середня. Можливо, варто додатково обстежитись лікаря. """)
txt_res.append(""" Вище середнього """)
txt_res. append(""" Висока """)

def ruffier_index(P1, P2, P3): # повертає значення індексу за трьома показниками пульсу для звірки з таблицею
    return (4 * (P1 + P2 + P3) - 200) / 10

def neud_level(age): # варіанти з віком менше 7 і дорослим треба обробляти окремо, тут підбираємо рівень "незадовільно тільки всередині таблиці
    norm_age = (min(age, 15) - 7) // 2 # кожні 2 роки різниці від 7 років перетворюються на одиницю - аж до 15 років
    result = (21 - norm_age * 1.5) # множимо кожні 2 роки різниці на 1.5, так розподілені рівні у таблиці
    return result

def ruffier_result(r_index, level): # функція отримує індекс Руф'є і інтерпретує його, повертає рівень готовності: число від 0 до 4
    if r_index >= level:
        return 0
    level = level - 4
    if r_index >= level:
        return 1
    level = level - 5
    if r_index >= level:
        return 2
    level = level - 5.5
    if r_index >= level:
        return 3
    return 4

def test(P1, P2, P3, age): # цю функцію можна використовувати зовні модуля для підрахунків індексу Руф'є.
    if age < 7:
        return (txt_index + "0", txt_nodata)
    else:
        ruff_index = ruffier_index(P1, P2, P3)
        result = txt_res[ruffier_result(ruff_index, neud_level(age))]
        res = txt_index + str(ruff_index) + "\n" + txt_workheart + result
        return res