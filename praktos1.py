import random

# Определение персонажа
class Character:
    def __init__(self, name, health, strength, defense, inventory, location):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.inventory = inventory
        self.location = location

# Создание персонажа
player = Character("Игрок", 100, 10, 0, [], "Город")

# Создание мира
locations = {
    "Город": {
        "description": "Вы находитесь на центральной площади города. Вокруг шумят люди, слышны звуки торговли и музыки.",
        "connections": {"лес": "Лес", "магазин": "Магазин"},
        "items": [],
        "monsters": []
    },
    "Лес": {
        "description": "Вы в густом лесу.  Солнечные лучи едва проникают сквозь листву.",
        "connections": {"город": "Город", "пещера": "Пещера"},
        "items": ["Меч", "Зелье лечения"],
        "monsters": ["Волк", "Медведь"]
    },
    "Пещера": {
        "description": "Вы в темной пещере.  В воздухе витает влажный, сырой запах.",
        "connections": {"лес": "Лес"},
        "items": ["Золото"],
        "monsters": ["Гоблин", "Огр"]
    },
    "Магазин": {
        "description": "Вы в небольшом магазине. На полках вы видите различные товары.",
        "connections": {"город": "Город"},
        "items": ["Щит", "Лук", "Стрелы"],
        "monsters": []
    }
}

# Создание монстров
monsters = {
    "Волк": {"health": 20, "attack": 5},
    "Медведь": {"health": 40, "attack": 10},
    "Гоблин": {"health": 15, "attack": 7},
    "Огр": {"health": 30, "attack": 15}
}

# Создание предметов
items = {
    "Меч": {"description": "Острый меч, который может помочь вам в бою.", "attack_bonus": 5},
    "Зелье лечения": {"description": "Зелье, которое восстанавливает здоровье.", "heal_amount": 20},
    "Щит": {"description": "Щит, который защищает вас от ударов.", "defense_bonus": 3},
    "Лук": {"description": "Лук для стрельбы.", "attack_bonus": 3},
    "Стрелы": {"description": "Стрелы для лука.", "attack_bonus": 2},
    "Золото": {"description": "Золотые монеты.  Они могут пригодиться в будущем."}
}

# Основной цикл игры
while True:
    # Вывод описания локации
    print(locations[player.location]["description"])

    # Проверка на наличие предметов
    if locations[player.location]["items"]:
        print("Вы видите:")
        for item in locations[player.location]["items"]:
            print(f"- {items[item]['description']}")

    # Проверка на наличие монстров
    if locations[player.location]["monsters"]:
        monster = random.choice(locations[player.location]["monsters"])
        print(f"На вас напал {monster}!")
        monster_health = monsters[monster]["health"]
        while player.health > 0 and monster_health > 0:
            print(f"Ваше здоровье: {player.health}")
            print(f"Здоровье {monster}: {monster_health}")
            action = input("Что вы хотите сделать? (атаковать / бежать): ").lower()
            if action == "атаковать":
                monster_health -= player.strength
                player.health -= monsters[monster]["attack"] - player.defense  # Применение защиты
                print(f"Вы ударили {monster}!")
                print(f"{monster} ударил вас!")
            elif action == "бежать":
                print(f"Вы убежали от {monster}!")
                break
            else:
                print("Неверный ввод!")

        if player.health <= 0:
            print(f"Вы погибли от {monster}!")
            break
        elif monster_health <= 0:
            print(f"Вы победили {monster}!")

    # Вывод доступных действий
    print("Доступные действия:")
    for direction in locations[player.location]["connections"]:
        print(f"- {direction}")

    # Ввод действия игрока
    action = input("Куда вы хотите пойти? ").lower()

    # Проверка корректности ввода
    if action in locations[player.location]["connections"]:
        player.location = locations[player.location]["connections"][action]
        # Добавление найденных предметов в инвентарь
        if locations[player.location]["items"]:
            for item in locations[player.location]["items"]:
                player.inventory.append(item)
                locations[player.location]["items"].remove(item)
    else:
        print("Неверный ввод!")

    # Проверка наличия предметов в инвентаре и применение их эффектов
    for item in player.inventory:
        if item == "Зелье лечения":
            player.health += items[item]["heal_amount"]
            player.inventory.remove(item)
            print(f"Вы выпили зелье лечения. Ваше здоровье: {player.health}")
        elif item == "Меч":
            player.strength += items[item]["attack_bonus"]
            print(f"Вы экипировали {item}. Ваша сила: {player.strength}")
        elif item == "Щит":
            player.defense = items[item]["defense_bonus"]
            print(f"Вы экипировали {item}.")
        elif item == "Лук":
            player.strength += items[item]["attack_bonus"]
            print(f"Вы экипировали {item}. Ваша сила: {player.strength}")
        elif item == "Стрелы":
            player.strength += items[item]["attack_bonus"]
            print(f"Вы экипировали {item}. Ваша сила: {player.strength}")
        elif item == "Золото":
            print(f"У вас {item}!")