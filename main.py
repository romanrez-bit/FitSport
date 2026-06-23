import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow


def main():
    """Точка входа в приложение"""
    app = QApplication(sys.argv)

    # Создаём и показываем главное окно
    window = MainWindow()
    window.show()

    # Запускаем цикл обработки событий
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
