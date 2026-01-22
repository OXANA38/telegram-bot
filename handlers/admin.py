import logging
from telegram import Update
from telegram.ext import ContextTypes
from config import ADMIN_CHAT_ID

logger = logging.getLogger(__name__)

async def forward_to_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Пересылка ответа админа пользователю"""
    if update.message.from_user.id == ADMIN_CHAT_ID and update.message.reply_to_message:
        try:
            user_id = int(update.message.reply_to_message.text.split("(ID: ")[1].split(")")[0])
            await context.bot.send_message(
                chat_id=user_id, 
                text=f"💬 Ответ менеджера: {update.message.text}"
            )
            await update.message.reply_text("✅ Сообщение отправлено пользователю.")
        except Exception as e:
            logger.error(f"Ошибка при отправке сообщения пользователю: {e}")
            await update.message.reply_text("❌ Не удалось отправить сообщение пользователю.")