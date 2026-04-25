import random
import json

# Функции
# Выгрузка из файла:
def unload_data():
    try:
        with open('DATA.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except:
        data = {
        "money": 0,
        "hero_leveling": {
            "damage multiplier": 1,
            "max hp": 20
        },
        "inventory": []
        }
        return data

# Загрузка в файл:
def upload_data():
    data_to_save = {
    "hp": DATA['hp'],
    "money": money,
    "hero_leveling": {
        "damage multiplier": hero_leveling['damage multiplier'],
        "max hp": hero_leveling['max hp']
    },
    "inventory": inventory}
    with open('DATA.json', 'w', encoding='utf-8') as f:
        json.dump(data_to_save, f, ensure_ascii=False, indent=4)
     
     
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     
# Вспомогательные функции для боя:
def is_dead(who):
    if who['hp'] <= 0:
        return True
    else:
        return False
    
def calculate_damage():
    damage = random.randint(1, 5)
    return damage
        
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   
# БОЙ: 
def fight():
    enemy = {
        "hp": random.randint(DATA['hero_leveling']["max hp"] - 10, DATA['hero_leveling']["max hp"] - 6),
        "name": 'Гоблин'
    }
    print('БОЙ НАЧАЛСЯ')
    while True:
        print(f'ВАШЕ HP: {DATA['hp']} | HP ПРОТИВНИКА: {float(enemy['hp'])}')
        if (word_attack := random.choice(words)) == (word_attack_input := 
            input(f'Ваша очередь атаковать\nВведите для атаки "{word_attack}": ').strip().lower()):
            
            enemy['hp'] -= (dmg := calculate_damage())
            print()
            print(f'Вы нанесли {dmg} урона')
            print("-"*30)
            if is_dead(enemy):
                print("Вы победили!")
                input("Нажмите Enter для выхода")
                return
            else:
                print(f"{enemy['name']} атакует")
                DATA['hp'] -= (dmg := calculate_damage())
                print()
                print(f"Вам нанесли {dmg} урона")
                print()
            if is_dead(DATA):
                print("Вы проиграли")
                DATA['hp'] = DATA['hero_leveling']['max hp'] * 0.9
                input("Нажмите Enter для выхода")
                return
        else:
            print("Промах! 0 урона")
            print()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Данные
DATA = unload_data()

money = DATA['money']

words = ('удар', 'выпад', 'укол', 'замах')

hero_leveling = {
    'damage multiplier': 1,
    'max hp': 20
                 }

inventory = ['меч']

shop = {
    'копье': 100
}


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Цикл игры
while (choice := int(input("...4. Драться на арене\n> ").strip())) != 5:
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        fight()      
        
else:
    upload_data()