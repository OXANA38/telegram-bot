import asyncio
import logging
from telegram import Update
from telegram.ext import ContextTypes
from config import WELCOME_IMAGE_URL, VIDEO_TUTORIAL
from keyboards import get_main_menu

logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Обработчик команды /start.
    Сначала отправляет изображение, затем текстовое приветствие.
    """
    context.user_data.clear()
    
    try:
        # 1. Отправляем изображение ПЕРВЫМ
        await update.message.reply_photo(
            photo=WELCOME_IMAGE_URL,
            caption="",
            reply_markup=get_main_menu()
        )
        
        # 2. После успешной отправки изображения, отправляем текст
        await asyncio.sleep(0.5)
        await update.message.reply_text(
            "👋 Привет! Добро пожаловать в бота обучения! Выбери действие ниже 👇", 
            reply_markup=get_main_menu()
        )
        
        logger.info("[START] Приветственное изображение и текст успешно отправлены.")
    except Exception as e:
        logger.error(f"[START] Ошибка при отправке приветствия: {type(e).__name__}: {e}")
        await update.message.reply_text(
            "👋 Привет! Добро пожаловать в бота обучения! Выбери действие ниже 👇", 
            reply_markup=get_main_menu()
        )

    # Отправляем видео-инструкцию
    await update.message.reply_text("🎬 Видео-инструкция:")
    await update.message.reply_video(
        video=VIDEO_TUTORIAL,
        caption="Как пользоваться ботом и обучением",
        reply_markup=get_main_menu()
    )

async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /test"""
    await update.message.reply_text("✅ Бот работает корректно")