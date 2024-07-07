import random
import time

for i in range(5):
    r = random.randint(0, 1)
    time.sleep(1)
    if r == 1:
        r = "Есть выстрел"
    else: 
        r = "Нет выыстрела"
    i = 1
    print(f"Курок нажат один раз. Результат: {r}")
    if r == "Есть выстрел":
        print("Игра окончена!")
        exit()
