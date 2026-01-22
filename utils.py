import logging
import os

# Настройка логирования
def setup_logging():
    """Настройка логирования в файл"""
    logging.basicConfig(
        filename="bot.log",
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
        filemode='a'
    )
    return logging.getLogger(__name__)

def check_presentation_file(file_path):
    """Проверка существования файла презентации"""
    if not os.path.exists(file_path):
        logger = logging.getLogger(__name__)
        logger.warning(f"Файл презентации не найден: {file_path}")
        return False
    return True