from PyQt6.QtWidgets import (QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
                             QListWidget, QListWidgetItem, QStackedWidget, QLabel)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

# Импортируем наши виджеты
from ui.exercises_widget import ExercisesWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Настройки окна
        self.setWindowTitle("FitSport - Твой персональный тренер")
        self.setMinimumSize(1200, 800)

        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Главный layout (горизонтальный)
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Боковое меню (слева)
        self.sidebar = QListWidget()
        self.sidebar.setFixedWidth(250)
        self.sidebar.setStyleSheet("""
            QListWidget {
                background-color: #2c3e50;
                color: white;
                border: none;
                font-size: 14px;
            }
            QListWidget::item {
                padding: 15px 20px;
                border-bottom: 1px solid #34495e;
            }
            QListWidget::item:selected {
                background-color: #3498db;
                border-left: 4px solid #2980b9;
            }
            QListWidget::item:hover {
                background-color: #34495e;
            }
        """)

        # Добавляем пункты меню
        menu_items = [
            "💪 Упражнения",
            "📋 Комплексы",
            "📝 Дневник тренировок",
            "🍎 Питание",
            "🧘 Духовное развитие",
            "📊 Прогресс"
        ]

        for item_text in menu_items:
            item = QListWidgetItem(item_text)
            self.sidebar.addItem(item)

        # Рабочая область (справа)
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setStyleSheet("background-color: #ecf0f1;")

        # Создаём страницы для каждого модуля
        self.create_pages()

        # Добавляем виджеты в layout
        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.stacked_widget, 1)

        # Подключаем сигнал переключения страниц
        self.sidebar.currentRowChanged.connect(self.stacked_widget.setCurrentIndex)

        # Выбираем первый пункт по умолчанию
        self.sidebar.setCurrentRow(0)

    def create_pages(self):
        """Создаёт страницы для каждого модуля"""

        # 1. Упражнения (ПОЛНОЦЕННЫЙ ВИДЖЕТ)
        exercises_page = ExercisesWidget()
        self.stacked_widget.addWidget(exercises_page)

        # 2. Комплексы (заглушка)
        complexes_page = self.create_placeholder_page("📋 Модуль: Комплексы",
                                                      "Здесь будут тренировки")
        self.stacked_widget.addWidget(complexes_page)

        # 3. Дневник тренировок (заглушка)
        diary_page = self.create_placeholder_page("📝 Модуль: Дневник тренировок",
                                                  "Здесь будут записи о тренировках")
        self.stacked_widget.addWidget(diary_page)

        # 4. Питание (заглушка)
        nutrition_page = self.create_placeholder_page("🍎 Модуль: Питание",
                                                      "Здесь будет дневник питания и воды")
        self.stacked_widget.addWidget(nutrition_page)

        # 5. Духовное развитие (заглушка)
        spiritual_page = self.create_placeholder_page("🧘 Модуль: Духовное развитие",
                                                      "Медитация, память, нейрогимнастика, книги")
        self.stacked_widget.addWidget(spiritual_page)

        # 6. Прогресс (заглушка)
        progress_page = self.create_placeholder_page("📊 Модуль: Прогресс",
                                                     "Графики веса, силовых, статистика")
        self.stacked_widget.addWidget(progress_page)

    def create_placeholder_page(self, title, description):
        """Создаёт страницу-заглушку для модуля"""
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Заголовок
        title_label = QLabel(title)
        title_label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        title_label.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")
        layout.addWidget(title_label)

        # Описание
        desc_label = QLabel(description)
        desc_label.setFont(QFont("Arial", 14))
        desc_label.setStyleSheet("color: #7f8c8d;")
        layout.addWidget(desc_label)

        return page