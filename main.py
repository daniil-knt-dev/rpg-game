import random
import json

# Функции

# Функции боя
# Атака

# Старт боя

# Функции сохранения
# Выгрузка из файла:
def unload_data():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data

# Загрузка в файл:
def upload_data():
    data_to_save = {
    "money": money,
    "hero_leveling": {
        "множитель урона": hero_leveling['множитель урона'],
        "максимальное здоровье": hero_leveling['максимальное здоровье']
    },
    "inventory": inventory}
    with open('data.json', 'w') as f:
        json.dump(data_to_save, f, ensure_ascii=False, indent=4)

# Данные
data = unload_data()

money = data['money']

words = ('удар', 'выпад', 'укол', 'замах')

hero_leveling = {
    'множитель урона': 1,
    'максимальное здоровье': 20
                 }

hero_fight_characters = {
    'hp': hero_leveling['максимальное здоровье']
}

inventory = ['меч']

shop = {
    'копье': 100
}
data_to_save = {
    "money": money,
    "hero_leveling": {
        "множитель урона": hero_leveling['множитель урона'],
        "максимальное здоровье": hero_leveling['максимальное здоровье']
    },
    "inventory": inventory}

# Цикл игры
while True:
    choice = int(input().strip())
    
    if choice == 1:
        
    elif choice == 2:
        
    elif choice == 3:
        
    elif choice == 4:
        
    elif choice == 5:
        
    else:
        