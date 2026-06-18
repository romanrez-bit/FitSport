import sqlite3
from pathlib import Path


class Database:
    def __init__(self, db_path="data/fitness.db"):
        Path("data").mkdir(exist_ok=True)
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # ФИЗИЧЕСКОЕ РАЗВИТИЕ
        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS exercises
                            (
                                id
                                INTEGER
                                PRIMARY
                                KEY
                                AUTOINCREMENT,
                                name
                                TEXT
                                NOT
                                NULL,
                                category
                                TEXT
                                NOT
                                NULL,
                                description
                                TEXT,
                                target_muscles
                                TEXT,
                                difficulty
                                INTEGER
                                DEFAULT
                                3,
                                alternatives
                                TEXT,
                                created_at
                                TIMESTAMP
                                DEFAULT
                                CURRENT_TIMESTAMP
                            )
                            ''')

        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS complexes
                            (
                                id
                                INTEGER
                                PRIMARY
                                KEY
                                AUTOINCREMENT,
                                name
                                TEXT
                                NOT
                                NULL,
                                type
                                TEXT
                                NOT
                                NULL,
                                duration_minutes
                                INTEGER,
                                description
                                TEXT,
                                notes
                                TEXT,
                                created_at
                                TIMESTAMP
                                DEFAULT
                                CURRENT_TIMESTAMP
                            )
                            ''')

        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS complex_exercises
                            (
                                id
                                INTEGER
                                PRIMARY
                                KEY
                                AUTOINCREMENT,
                                complex_id
                                INTEGER
                                NOT
                                NULL,
                                exercise_id
                                INTEGER
                                NOT
                                NULL,
                                order_num
                                INTEGER
                                NOT
                                NULL,
                                sets
                                INTEGER
                                DEFAULT
                                3,
                                reps
                                INTEGER,
                                duration_seconds
                                INTEGER,
                                rest_between_sets
                                INTEGER,
                                rest_between_exercises
                                INTEGER,
                                tempo
                                TEXT
                                DEFAULT
                                '2-1-2',
                                target_rpe
                                INTEGER,
                                notes
                                TEXT,
                                FOREIGN
                                KEY
                            (
                                complex_id
                            ) REFERENCES complexes
                            (
                                id
                            ) ON DELETE CASCADE,
                                FOREIGN KEY
                            (
                                exercise_id
                            ) REFERENCES exercises
                            (
                                id
                            )
                                )
                            ''')

        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS workout_sessions
                            (
                                id
                                INTEGER
                                PRIMARY
                                KEY
                                AUTOINCREMENT,
                                complex_id
                                INTEGER
                                NOT
                                NULL,
                                date
                                DATE
                                NOT
                                NULL,
                                start_time
                                TIME,
                                end_time
                                TIME,
                                overall_rpe
                                INTEGER,
                                feeling_before
                                INTEGER,
                                feeling_after
                                INTEGER,
                                notes
                                TEXT,
                                FOREIGN
                                KEY
                            (
                                complex_id
                            ) REFERENCES complexes
                            (
                                id
                            )
                                )
                            ''')

        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS workout_exercise_results
                            (
                                id
                                INTEGER
                                PRIMARY
                                KEY
                                AUTOINCREMENT,
                                session_id
                                INTEGER
                                NOT
                                NULL,
                                complex_exercise_id
                                INTEGER
                                NOT
                                NULL,
                                actual_sets
                                INTEGER,
                                actual_reps
                                TEXT,
                                actual_duration_seconds
                                INTEGER,
                                actual_rpe
                                INTEGER,
                                weight_used
                                REAL,
                                notes
                                TEXT,
                                FOREIGN
                                KEY
                            (
                                session_id
                            ) REFERENCES workout_sessions
                            (
                                id
                            ) ON DELETE CASCADE,
                                FOREIGN KEY
                            (
                                complex_exercise_id
                            ) REFERENCES complex_exercises
                            (
                                id
                            )
                                )
                            ''')

        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS nutrition_log
                            (
                                id
                                INTEGER
                                PRIMARY
                                KEY
                                AUTOINCREMENT,
                                date
                                DATE
                                NOT
                                NULL,
                                meal_type
                                TEXT
                                NOT
                                NULL,
                                description
                                TEXT,
                                plate_method_followed
                                BOOLEAN,
                                notes
                                TEXT
                            )
                            ''')

        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS water_log
                            (
                                id
                                INTEGER
                                PRIMARY
                                KEY
                                AUTOINCREMENT,
                                date
                                DATE
                                NOT
                                NULL,
                                amount_liters
                                REAL
                                NOT
                                NULL,
                                notes
                                TEXT
                            )
                            ''')

        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS body_metrics
                            (
                                id
                                INTEGER
                                PRIMARY
                                KEY
                                AUTOINCREMENT,
                                date
                                DATE
                                NOT
                                NULL,
                                weight_kg
                                REAL,
                                morning_pulse
                                INTEGER,
                                waist_cm
                                REAL,
                                notes
                                TEXT
                            )
                            ''')

        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS personal_records
                            (
                                id
                                INTEGER
                                PRIMARY
                                KEY
                                AUTOINCREMENT,
                                exercise_id
                                INTEGER
                                NOT
                                NULL,
                                record_type
                                TEXT
                                NOT
                                NULL,
                                record_value
                                REAL
                                NOT
                                NULL,
                                date_achieved
                                DATE
                                NOT
                                NULL,
                                notes
                                TEXT,
                                FOREIGN
                                KEY
                            (
                                exercise_id
                            ) REFERENCES exercises
                            (
                                id
                            )
                                )
                            ''')

        # ДУХОВНОЕ РАЗВИТИЕ
        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS spiritual_activities
                            (
                                id
                                INTEGER
                                PRIMARY
                                KEY
                                AUTOINCREMENT,
                                name
                                TEXT
                                NOT
                                NULL,
                                category
                                TEXT
                                NOT
                                NULL,
                                activity_type
                                TEXT,
                                content
                                TEXT,
                                author
                                TEXT,
                                difficulty
                                INTEGER
                                DEFAULT
                                2,
                                target_duration_minutes
                                INTEGER,
                                notes
                                TEXT,
                                created_at
                                TIMESTAMP
                                DEFAULT
                                CURRENT_TIMESTAMP
                            )
                            ''')

        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS spiritual_log
                            (
                                id
                                INTEGER
                                PRIMARY
                                KEY
                                AUTOINCREMENT,
                                activity_id
                                INTEGER,
                                date
                                DATE
                                NOT
                                NULL,
                                category
                                TEXT
                                NOT
                                NULL,
                                activity_name
                                TEXT,
                                duration_minutes
                                INTEGER,
                                pages_read
                                INTEGER,
                                progress_percent
                                INTEGER,
                                quality
                                INTEGER,
                                mood_before
                                INTEGER,
                                mood_after
                                INTEGER,
                                score
                                INTEGER,
                                notes
                                TEXT,
                                created_at
                                TIMESTAMP
                                DEFAULT
                                CURRENT_TIMESTAMP,
                                FOREIGN
                                KEY
                            (
                                activity_id
                            ) REFERENCES spiritual_activities
                            (
                                id
                            ) ON DELETE SET NULL
                                )
                            ''')

        self.conn.commit()
        print("✅ Все таблицы созданы/проверены")

    def get_all_tables(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
        return [row[0] for row in self.cursor.fetchall()]

    def close(self):
        self.conn.close()


if __name__ == "__main__":
    db = Database()
    print("\n📊 Таблицы в базе данных:")
    tables = db.get_all_tables()
    for i, table in enumerate(tables, 1):
        print(f"  {i}. {table}")
    print(f"\n✅ Всего таблиц: {len(tables)}")
    db.close()