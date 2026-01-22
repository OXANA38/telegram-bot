import logging
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from telegram import BotCommand

# Импорт конфигурации
from config import TOKEN, ADMIN_CHAT_ID

# Импорт обработчиков
from handlers.start import start, test
from handlers.messages import handle_message
from handlers.callbacks import callback_handler
from handlers.admin import forward_to_user

# Настройка логирования
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def main():
    # Создаем приложение
    app = Application.builder().token(TOKEN).build()
    
    # Установка команд бота
    await app.bot.set_my_commands([
        BotCommand("start", "Начать работу"),
        BotCommand("test", "Проверка работоспособности")
    ])
    
    # Добавляем обработчики
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("test", test))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(CallbackQueryHandler(callback_handler))
    app.add_handler(MessageHandler(filters.TEXT & filters.User(user_id=ADMIN_CHAT_ID), forward_to_user))
    
    # Запускаем бота
    print("✅ Бот запущен!")
    logger.info("Бот успешно запущен")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())


