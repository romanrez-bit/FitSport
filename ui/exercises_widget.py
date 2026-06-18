from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
                             QTableWidget, QTableWidgetItem, QLabel, QMessageBox,
                             QHeaderView, QLineEdit)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from database import Database  # ← только этот импорт!


class ExercisesWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.init_ui()
        self.load_exercises()

    def init_ui(self):
        """Инициализация интерфейса"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)

        # Заголовок
        header = QLabel("💪 Библиотека упражнений")
        header.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        header.setStyleSheet("color: #2c3e50; margin-bottom: 10px;")
        layout.addWidget(header)

        # Панель инструментов
        toolbar = QHBoxLayout()

        # Поиск
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("🔍 Поиск по названию...")
        self.search_input.setStyleSheet("""
            QLineEdit {
                padding: 8px 12px;
                border: 2px solid #bdc3c7;
                border-radius: 6px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border-color: #3498db;
            }
        """)
        self.search_input.textChanged.connect(self.filter_exercises)
        toolbar.addWidget(self.search_input)

        # Кнопка "Добавить"
        self.btn_add = QPushButton("➕ Добавить упражнение")
        self.btn_add.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                padding: 8px 16px;
                border-radius: 6px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #229954;
            }
        """)
        self.btn_add.clicked.connect(self.add_exercise)
        toolbar.addWidget(self.btn_add)

        # Кнопка "Обновить"
        self.btn_refresh = QPushButton("🔄 Обновить")
        self.btn_refresh.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                padding: 8px 16px;
                border-radius: 6px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        self.btn_refresh.clicked.connect(self.load_exercises)
        toolbar.addWidget(self.btn_refresh)

        layout.addLayout(toolbar)

        # Таблица упражнений
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "ID", "Название", "Категория", "Сложность", "Целевые мышцы", "Действия"
        ])

        # Настройки таблицы
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)
        self.table.setAlternatingRowColors(True)
        self.table.setStyleSheet("""
            QTableWidget {
                background-color: white;
                border: 1px solid #bdc3c7;
                border-radius: 6px;
                gridline-color: #ecf0f1;
            }
            QTableWidget::item {
                padding: 8px;
            }
            QHeaderView::section {
                background-color: #34495e;
                color: white;
                padding: 8px;
                border: none;
                font-weight: bold;
            }
        """)

        layout.addWidget(self.table)

        # Статистика
        self.stats_label = QLabel("Загрузка...")
        self.stats_label.setStyleSheet("color: #7f8c8d; font-size: 12px; margin-top: 10px;")
        layout.addWidget(self.stats_label)

    def load_exercises(self):
        """Загружает упражнения из базы данных"""
        self.db.cursor.execute("SELECT * FROM exercises ORDER BY category, name")
        exercises = self.db.cursor.fetchall()

        self.table.setRowCount(len(exercises))

        for row, ex in enumerate(exercises):
            # ID
            id_item = QTableWidgetItem(str(ex['id']))
            id_item.setFlags(id_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(row, 0, id_item)

            # Название
            name_item = QTableWidgetItem(ex['name'])
            name_item.setFlags(name_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(row, 1, name_item)

            # Категория
            category_item = QTableWidgetItem(ex['category'])
            category_item.setFlags(category_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(row, 2, category_item)

            # Сложность
            difficulty_item = QTableWidgetItem(f"{'⭐' * ex['difficulty']}")
            difficulty_item.setFlags(difficulty_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(row, 3, difficulty_item)

            # Целевые мышцы
            muscles_item = QTableWidgetItem(ex['target_muscles'] or "")
            muscles_item.setFlags(muscles_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(row, 4, muscles_item)

            # Кнопки действий
            actions_widget = QWidget()
            actions_layout = QHBoxLayout(actions_widget)
            actions_layout.setContentsMargins(5, 2, 5, 2)

            btn_edit = QPushButton("✏️")
            btn_edit.setFixedSize(30, 30)
            btn_edit.setToolTip("Редактировать")
            btn_edit.setStyleSheet("""
                QPushButton {
                    background-color: #f39c12;
                    color: white;
                    border-radius: 4px;
                }
                QPushButton:hover {
                    background-color: #e67e22;
                }
            """)
            btn_edit.clicked.connect(lambda checked, ex_id=ex['id']: self.edit_exercise(ex_id))
            actions_layout.addWidget(btn_edit)

            btn_delete = QPushButton("🗑️")
            btn_delete.setFixedSize(30, 30)
            btn_delete.setToolTip("Удалить")
            btn_delete.setStyleSheet("""
                QPushButton {
                    background-color: #e74c3c;
                    color: white;
                    border-radius: 4px;
                }
                QPushButton:hover {
                    background-color: #c0392b;
                }
            """)
            btn_delete.clicked.connect(
                lambda checked, ex_id=ex['id'], ex_name=ex['name']: self.delete_exercise(ex_id, ex_name))
            actions_layout.addWidget(btn_delete)

            self.table.setCellWidget(row, 5, actions_widget)

        # Обновляем статистику
        self.stats_label.setText(f"📊 Всего упражнений: {len(exercises)}")

    def filter_exercises(self, text):
        """Фильтрует упражнения по поисковому запросу"""
        for row in range(self.table.rowCount()):
            name_item = self.table.item(row, 1)
            if name_item:
                name = name_item.text().lower()
                self.table.setRowHidden(row, text.lower() not in name)

    def add_exercise(self):
        """Добавляет новое упражнение (заглушка)"""
        QMessageBox.information(self, "Информация",
                                "Функция добавления упражнения будет реализована на следующем этапе")

    def edit_exercise(self, exercise_id):
        """Редактирует упражнение (заглушка)"""
        QMessageBox.information(self, "Информация",
                                f"Функция редактирования упражнения #{exercise_id} будет реализована на следующем этапе")

    def delete_exercise(self, exercise_id, exercise_name):
        """Удаляет упражнение"""
        reply = QMessageBox.question(
            self,
            "Подтверждение удаления",
            f"Вы уверены, что хотите удалить упражнение '{exercise_name}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.db.cursor.execute("DELETE FROM exercises WHERE id = ?", (exercise_id,))
            self.db.conn.commit()
            self.load_exercises()
            QMessageBox.information(self, "Успех", "Упражнение удалено")