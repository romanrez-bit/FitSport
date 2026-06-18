"""
Скрипт для заполнения базы данных начальными данными.
Запускается ОДИН РАЗ при первом старте приложения.
"""

from database import Database
from datetime import date


def init_exercises(db):
    """Добавляет упражнения из программы тренировок"""

    exercises = [
        # ТРЕНИРОВКА 1: ТЯНИ + КОР
        {
            "name": "Подтягивания широким хватом",
            "category": "Тяни",
            "description": "Хват шире плеч, подтягиваться до касания перекладины грудью. Темп 2-1-2.",
            "target_muscles": "Широчайшие, бицепс, предплечья",
            "difficulty": 3,
            "alternatives": "Австралийские подтягивания, тяга гири в наклоне"
        },
        {
            "name": "Австралийские подтягивания на кольцах",
            "category": "Тяни",
            "description": "Тело горизонтально, ноги на земле. Подтягивать грудь к кольцам. Темп 2-1-2.",
            "target_muscles": "Середина спины, ромбовидные, задняя дельта",
            "difficulty": 2,
            "alternatives": "Австралийские на турнике, тяга гантели в наклоне"
        },
        {
            "name": "Подтягивания обратным хватом",
            "category": "Тяни",
            "description": "Хват снизу, ладони к себе. Акцент на бицепс. Темп 2-1-2.",
            "target_muscles": "Бицепс, широчайшие",
            "difficulty": 3,
            "alternatives": "Тяга гири 15 кг в наклоне, тяга гантелей"
        },
        {
            "name": "Тяга гири 15 кг в наклоне",
            "category": "Тяни",
            "description": "Наклон корпуса 45°, тянуть гирю к поясу. Спина прямая.",
            "target_muscles": "Широчайшие, бицепс",
            "difficulty": 2,
            "alternatives": "Подтягивания обратным хватом"
        },
        {
            "name": "Подъем ног в висе на турнике",
            "category": "Кор",
            "description": "Вис на турнике, поднимать прямые ноги до угла 90°. Без раскачки.",
            "target_muscles": "Пресс, подвздошно-поясничная",
            "difficulty": 4,
            "alternatives": "Подъем коленей к груди, уголок на брусьях"
        },
        {
            "name": "L-sit (уголок) на брусьях",
            "category": "Кор",
            "description": "Удержание уголка на брусьях или кольцах. Тело в форме буквы L.",
            "target_muscles": "Пресс, квадрицепсы, стабилизаторы",
            "difficulty": 4,
            "alternatives": "Удержание уголка на полу, планка"
        },
        {
            "name": "Планка на кольцах",
            "category": "Кор",
            "description": "Кольца на уровне груди, тело прямо. Удержание. Не проваливать плечи.",
            "target_muscles": "Кор, стабилизаторы плечевого пояса",
            "difficulty": 3,
            "alternatives": "Планка на полу, планка на брусьях"
        },

        # ТРЕНИРОВКА 2: ЖМИ + НОГИ
        {
            "name": "Отжимания на брусьях",
            "category": "Жми",
            "description": "Опускаться до угла 90° в локтях, подниматься мощно. Темп 2-1-2.",
            "target_muscles": "Грудь, трицепс, передняя дельта",
            "difficulty": 3,
            "alternatives": "Отжимания от пола, отжимания с акцентом на трицепс"
        },
        {
            "name": "Отжимания от пола с ногами на возвышении",
            "category": "Жми",
            "description": "Ноги на скамье/турнике, акцент на верх груди. Темп 2-1-2.",
            "target_muscles": "Верх груди, передняя дельта",
            "difficulty": 3,
            "alternatives": "Обычные отжимания от пола, отжимания с хлопком"
        },
        {
            "name": "Пистолетик (приседания на одной ноге)",
            "category": "Ноги",
            "description": "Приседание на одной ноге, вторая вытянута вперёд. Держаться за опору при необходимости.",
            "target_muscles": "Квадрицепсы, ягодицы, стабилизаторы",
            "difficulty": 5,
            "alternatives": "Болгарские выпады с блином 15 кг"
        },
        {
            "name": "Болгарские выпады с блином 15 кг",
            "category": "Ноги",
            "description": "Задняя нога на скамье, в руках блин 15 кг. Приседать на передней ноге.",
            "target_muscles": "Квадрицепсы, ягодицы",
            "difficulty": 3,
            "alternatives": "Пистолетик, обычные выпады"
        },
        {
            "name": "Махи гирей/блином 15 кг (русские махи)",
            "category": "Ноги",
            "description": "Мощный выброс таза вперёд, гиря/блин поднимается до уровня глаз. Спина прямая.",
            "target_muscles": "Ягодицы, бицепс бедра, поясница",
            "difficulty": 3,
            "alternatives": "Становая тяга, гиперэкстензия"
        },
        {
            "name": "Ягодичный мостик на одной ноге",
            "category": "Ноги",
            "description": "Лежа на спине, одна нога вытянута, поднимать таз за счёт ягодиц.",
            "target_muscles": "Ягодицы, бицепс бедра",
            "difficulty": 2,
            "alternatives": "Ягодичный мостик на двух ногах"
        },
        {
            "name": "Подъемы на носки на ступеньке",
            "category": "Ноги",
            "description": "Стоя на ступеньке, подниматься на носки до максимума, медленно опускаться.",
            "target_muscles": "Икроножные, камбаловидная",
            "difficulty": 1,
            "alternatives": "Подъемы на носки стоя на полу"
        },

        # ДОПОЛНИТЕЛЬНЫЕ
        {
            "name": "Скакалка (интервалы)",
            "category": "Кардио",
            "description": "30 сек прыгаем / 30 сек отдых. 10-15 циклов.",
            "target_muscles": "Икры, кардио-система",
            "difficulty": 2,
            "alternatives": "Бег на месте, берпи"
        },
        {
            "name": "Боксерский комплекс с гантелями 2-4 кг",
            "category": "Кардио",
            "description": "Джеб, кросс, хук, апперкот. 3 раунда по 3 минуты.",
            "target_muscles": "Плечи, кор, кардио",
            "difficulty": 3,
            "alternatives": "Работа со жгутом, удары без веса"
        },
        {
            "name": "Баланс-борд",
            "category": "Баланс",
            "description": "Стойка на одной ноге, приседания, перенос веса.",
            "target_muscles": "Стабилизаторы, голеностоп",
            "difficulty": 2,
            "alternatives": "Стойка на одной ноге с закрытыми глазами"
        }
    ]

    # Проверяем, есть ли уже упражнения
    db.cursor.execute("SELECT COUNT(*) FROM exercises")
    if db.cursor.fetchone()[0] > 0:
        print("⚠️  Упражнения уже есть в базе. Пропускаем.")
        return

    for ex in exercises:
        db.cursor.execute('''
                          INSERT INTO exercises (name, category, description, target_muscles, difficulty, alternatives)
                          VALUES (?, ?, ?, ?, ?, ?)
                          ''', (ex["name"], ex["category"], ex["description"],
                                ex["target_muscles"], ex["difficulty"], ex["alternatives"]))

    db.conn.commit()
    print(f"✅ Добавлено упражнений: {len(exercises)}")


def init_complexes(db):
    """Создает комплексы тренировок"""

    # Проверяем, есть ли уже комплексы
    db.cursor.execute("SELECT COUNT(*) FROM complexes")
    if db.cursor.fetchone()[0] > 0:
        print("⚠️  Комплексы уже есть в базе. Пропускаем.")
        return

    # Комплекс 1: Тяни + Кор
    db.cursor.execute('''
                      INSERT INTO complexes (name, type, duration_minutes, description, notes)
                      VALUES (?, ?, ?, ?, ?)
                      ''', ("Тяни + Кор (День 2)", "Силовая", 70,
                            "Основная силовая тренировка на спину и кор. День 2 после смены.",
                            "Темп 2-1-2. Выдох на усилии. RPE 7-8. Отдых 2-3 мин в базе, 1-1.5 мин в остальных."))
    complex1_id = db.cursor.lastrowid

    # Упражнения для комплекса 1
    complex1_exercises = [
        {"exercise_name": "Подтягивания широким хватом", "order": 1, "sets": 4, "reps": 8, "rest_sets": 180,
         "tempo": "2-1-2", "rpe": 8},
        {"exercise_name": "Австралийские подтягивания на кольцах", "order": 2, "sets": 3, "reps": 11, "rest_sets": 120,
         "tempo": "2-1-2", "rpe": 7},
        {"exercise_name": "Подтягивания обратным хватом", "order": 3, "sets": 3, "reps": 9, "rest_sets": 120,
         "tempo": "2-1-2", "rpe": 7},
        {"exercise_name": "Подъем ног в висе на турнике", "order": 4, "sets": 3, "reps": 10, "rest_sets": 90,
         "tempo": "2-1-2", "rpe": 7},
        {"exercise_name": "L-sit (уголок) на брусьях", "order": 5, "sets": 3, "duration_seconds": 20, "rest_sets": 90,
         "tempo": "-", "rpe": 7},
        {"exercise_name": "Планка на кольцах", "order": 6, "sets": 3, "duration_seconds": 40, "rest_sets": 60,
         "tempo": "-", "rpe": 7},
    ]

    for ex in complex1_exercises:
        db.cursor.execute("SELECT id FROM exercises WHERE name = ?", (ex["exercise_name"],))
        exercise_id = db.cursor.fetchone()[0]

        db.cursor.execute('''
                          INSERT INTO complex_exercises
                          (complex_id, exercise_id, order_num, sets, reps, duration_seconds, rest_between_sets, tempo,
                           target_rpe)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                          ''', (complex1_id, exercise_id, ex["order"], ex["sets"],
                                ex.get("reps"), ex.get("duration_seconds"),
                                ex["rest_sets"], ex["tempo"], ex["rpe"]))

    # Комплекс 2: Жми + Ноги
    db.cursor.execute('''
                      INSERT INTO complexes (name, type, duration_minutes, description, notes)
                      VALUES (?, ?, ?, ?, ?)
                      ''', ("Жми + Ноги (День 3)", "Силовая", 70,
                            "Основная силовая тренировка на грудь и ноги. День 3 перед сменой.",
                            "Темп 2-1-2. Выдох на усилии. RPE 7-8. Отдых 2-3 мин в базе, 1-1.5 мин в остальных."))
    complex2_id = db.cursor.lastrowid

    # Упражнения для комплекса 2
    complex2_exercises = [
        {"exercise_name": "Отжимания на брусьях", "order": 1, "sets": 4, "reps": 12, "rest_sets": 180, "tempo": "2-1-2",
         "rpe": 8},
        {"exercise_name": "Отжимания от пола с ногами на возвышении", "order": 2, "sets": 3, "reps": 14,
         "rest_sets": 120, "tempo": "2-1-2", "rpe": 7},
        {"exercise_name": "Пистолетик (приседания на одной ноге)", "order": 3, "sets": 3, "reps": 6, "rest_sets": 180,
         "tempo": "2-1-2", "rpe": 8},
        {"exercise_name": "Махи гирей/блином 15 кг (русские махи)", "order": 4, "sets": 3, "reps": 18, "rest_sets": 120,
         "tempo": "2-1-2", "rpe": 7},
        {"exercise_name": "Ягодичный мостик на одной ноге", "order": 5, "sets": 3, "reps": 14, "rest_sets": 90,
         "tempo": "2-1-2", "rpe": 7},
        {"exercise_name": "Подъемы на носки на ступеньке", "order": 6, "sets": 3, "reps": 22, "rest_sets": 60,
         "tempo": "2-1-2", "rpe": 7},
    ]

    for ex in complex2_exercises:
        db.cursor.execute("SELECT id FROM exercises WHERE name = ?", (ex["exercise_name"],))
        exercise_id = db.cursor.fetchone()[0]

        db.cursor.execute('''
                          INSERT INTO complex_exercises
                          (complex_id, exercise_id, order_num, sets, reps, duration_seconds, rest_between_sets, tempo,
                           target_rpe)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                          ''', (complex2_id, exercise_id, ex["order"], ex["sets"],
                                ex.get("reps"), ex.get("duration_seconds"),
                                ex["rest_sets"], ex["tempo"], ex["rpe"]))

    db.conn.commit()
    print("✅ Добавлено комплексов: 2")


def init_spiritual_activities(db):
    """Добавляет духовные активности"""

    # Проверяем, есть ли уже активности
    db.cursor.execute("SELECT COUNT(*) FROM spiritual_activities")
    if db.cursor.fetchone()[0] > 0:
        print("⚠️  Духовные активности уже есть в базе. Пропускаем.")
        return

    activities = [
        # Медитация
        {
            "name": "Осознанное дыхание",
            "category": "meditation",
            "activity_type": "техника",
            "content": "Сядьте удобно. Сосредоточьтесь на дыхании. Вдох на 4 счета, задержка 2 счета, выдох на 6 счетов. Повторять 10 минут.",
            "difficulty": 1,
            "target_duration_minutes": 10,
            "notes": "Лучшее время — утро или перед сном"
        },
        {
            "name": "Сканирование тела",
            "category": "meditation",
            "activity_type": "техника",
            "content": "Лежа на спине, последовательно концентрируйте внимание на каждой части тела, от стоп до макушки. Расслабляйте каждую зону.",
            "difficulty": 2,
            "target_duration_minutes": 15,
            "notes": "Отлично подходит после тренировки"
        },

        # Развитие памяти (стихи)
        {
            "name": "Зимний вечер (первый куплет)",
            "category": "memory",
            "activity_type": "стихотворение",
            "content": "Буря мглою небо кроет,\nВихри снежные крутя;\nТо, как зверь, она завоет,\nТо заплачет, как дитя.",
            "author": "А.С. Пушкин",
            "difficulty": 2,
            "notes": "Классика для тренировки памяти"
        },
        {
            "name": "Ночь, улица, фонарь, аптека",
            "category": "memory",
            "activity_type": "стихотворение",
            "content": "Ночь, улица, фонарь, аптека,\nБессмысленный и тусклый свет.\nЖиви еще — хоть нет ответа —\nВсе будет так. Исхода нет.",
            "author": "А.А. Блок",
            "difficulty": 3,
            "notes": "Короткое, но глубокое"
        },
        {
            "name": "Письмо Татьяны (фрагмент)",
            "category": "memory",
            "activity_type": "стихотворение",
            "content": "Я к вам пишу — чего же боле?\nЧто я могу еще сказать?\nТеперь, я знаю, в вашей воле\nМеня презреньем наказать.",
            "author": "А.С. Пушкин",
            "difficulty": 3,
            "notes": "Эмоциональный текст, легче запоминается"
        },

        # Нейрогимнастика
        {
            "name": "Нерабочая рука",
            "category": "neurobics",
            "activity_type": "упражнение",
            "content": "Выполняйте привычные действия нерабочей рукой: чистка зубов, расчесывание, использование мыши. Это активирует новые нейронные связи.",
            "difficulty": 2,
            "notes": "Можно делать ежедневно в быту"
        },
        {
            "name": "Счет наоборот",
            "category": "neurobics",
            "activity_type": "упражнение",
            "content": "Считайте от 100 до 1, отнимая по 7: 100, 93, 86, 79... Усложняйте: от 1000 отнимайте по 13.",
            "difficulty": 3,
            "notes": "Тренирует концентрацию и рабочий память"
        },

        # Чтение книг
        {
            "name": "Атомные привычки",
            "category": "reading",
            "activity_type": "книга",
            "author": "Джеймс Клир",
            "content": "Книга о том, как маленькие изменения приводят к большим результатам. Формирование привычек через систему, а не силу воли.",
            "difficulty": 2,
            "notes": "Читать по 20 страниц в день. Отлично сочетается с тренировками."
        },
        {
            "name": "Думай медленно, решай быстро",
            "category": "reading",
            "activity_type": "книга",
            "author": "Даниэль Канеман",
            "content": "О двух системах мышления: быстрой (интуитивной) и медленной (рациональной). Как мы принимаем решения.",
            "difficulty": 4,
            "notes": "Серьезная книга, читать по 10-15 страниц в день"
        },

        # Тренажер мозга
        {
            "name": "Таблицы Шульте",
            "category": "brain_game",
            "activity_type": "упражнение",
            "content": "Найдите все числа от 1 до 25 в таблице 5x5 в порядке возрастания, глядя только в центральную клетку. Цель — быстрее 30 секунд.",
            "difficulty": 3,
            "notes": "Развивает периферическое зрение и скорость реакции"
        },

        # Благодарность
        {
            "name": "Три благодарности дня",
            "category": "gratitude",
            "activity_type": "практика",
            "content": "Каждый вечер запиши 3 вещи, за которые ты благодарен сегодня. Мелочи тоже считаются.",
            "difficulty": 1,
            "notes": "Мощная практика для повышения удовлетворенности жизнью"
        }
    ]

    for act in activities:
        db.cursor.execute('''
                          INSERT INTO spiritual_activities
                          (name, category, activity_type, content, author, difficulty, target_duration_minutes, notes)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                          ''', (act["name"], act["category"], act["activity_type"],
                                act.get("content"), act.get("author"),
                                act.get("difficulty", 2),  # ← ИСПРАВЛЕНО: безопасное получение с дефолтом
                                act.get("target_duration_minutes"),
                                act.get("notes")))

    db.conn.commit()
    print(f"✅ Добавлено духовных активностей: {len(activities)}")


def main():
    """Главная функция инициализации"""
    print("🚀 Запуск инициализации базы данных...\n")

    db = Database()

    try:
        init_exercises(db)
        init_complexes(db)
        init_spiritual_activities(db)

        print("\n📊 Итоговая статистика:")
        tables = db.get_all_tables()
        for table in tables:
            if table == 'sqlite_sequence':
                continue
            db.cursor.execute(f"SELECT COUNT(*) FROM {table}")
            count = db.cursor.fetchone()[0]
            if count > 0:
                print(f"  • {table}: {count} записей")

        print("\n✅ Инициализация завершена успешно!")
        print("💡 Теперь можно запускать main.py")

    except Exception as e:
        print(f"\n❌ Ошибка при инициализации: {e}")
        db.conn.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    main()