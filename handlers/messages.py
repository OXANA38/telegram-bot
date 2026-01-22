import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from config import (
    LESSONS, VIDEO_REG, VIDEO_ACTIVATION, VIDEO_LIME_USDT, 
    VIDEO_LIME_BTC, VIDEO_LIME_RUB, VIDEO_ULIME_USDT, VIDEO_ULIME_RUB,
    ADMIN_CHAT_ID
)
from keyboards import (
    get_main_menu, get_lessons_menu, get_funds_menu, get_lime_submenu,
    get_ulime_submenu, get_withdrawal_submenu, get_lesson_menu,
    get_lime_withdrawal_inline_menu, get_ulime_withdrawal_inline_menu,
    get_bitlime_withdrawal_inline_menu
)

logger = logging.getLogger(__name__)

# === ОБРАБОТКА ГЛАВНОГО МЕНЮ ===
async def handle_citro_wallet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка кнопки '💼 Citro Wallet' с инлайн-кнопками"""
    message_text = (
        "💼 *Citro Wallet*\n\n"
        "Это ваш надежный криптокошелек для безопасного хранения и управления активами.\n\n"
        "*Основные возможности:*\n"
        "• Хранение криптовалют\n"
        "• Быстрые переводы\n"
        "• Безопасные транзакции\n"
        "• Поддержка основных токенов\n"
    )
    
    # Создаем инлайн-кнопки
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("1. Что такое C-Wallet", callback_data="citro_empty_1")],
        [InlineKeyboardButton("2. Что такое C-Box", callback_data="citro_empty_2")]
    ])
    
    await update.message.reply_text(
        message_text,
        parse_mode="Markdown",
        reply_markup=keyboard
    )

async def handle_school(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка кнопки '📚 Школа новичка'"""
    await update.message.reply_text("Выбери урок:", reply_markup=get_lessons_menu())

async def handle_support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка кнопки '📞 Связь с менеджером'"""
    context.user_data['forwarding_to_admin'] = True
    await update.message.reply_text("✉️ Напишите свой вопрос. Менеджер ответит как можно скорее.")

async def handle_registration(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка кнопки '👉 Зарегистрироваться в Lime'"""
    await update.message.reply_text(
        "🚀 Жми на кнопку ниже, чтобы перейти к регистрации:",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Зарегистрироваться", url="https://sso.magic-lime.site/registration/?partner=CR8EyKP053cSIajOQiEMFu8RasXThQQ8S7DvwUjh")]
        ])
    )

async def handle_bnp_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка кнопки '➡ Выбор БНП'"""
    from keyboards import get_bnp_inline_menu
    await update.message.reply_text("📋 Выберите программу:", reply_markup=get_bnp_inline_menu())

# === ОБРАБОТКА МЕНЮ УРОКОВ ===
async def handle_withdrawal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка кнопки '💸 ВЫВОД СРЕДСТВ'"""
    await update.message.reply_text(
        "💱 Выберите валюту для вывода средств:",
        reply_markup=get_withdrawal_submenu()
    )

async def handle_how_to_register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка кнопки '✅ Как зарегистрироваться'"""
    await update.message.reply_text(LESSONS[2], reply_markup=get_lesson_menu())
    try:
        await update.message.reply_video(video=VIDEO_REG, caption="🎥 Как зарегистрироваться", reply_markup=get_lesson_menu())
    except Exception as e:
        logger.error(f"Ошибка при отправке видео: {e}")
        await update.message.reply_text("❌ Не удалось загрузить видео.", reply_markup=get_lesson_menu())

async def handle_subscription_activation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка кнопки '📘 Активация подписки'"""
    await update.message.reply_text(LESSONS[3], reply_markup=get_lesson_menu())
    try:
        await update.message.reply_video(video=VIDEO_ACTIVATION, caption="🎥 Как активировать подписку", reply_markup=get_lesson_menu())
    except Exception as e:
        logger.error(f"Ошибка при отправке видео: {e}")
        await update.message.reply_text("❌ Не удалось загрузить видео.", reply_markup=get_lesson_menu())

async def handle_deposit_funds(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка кнопки '💰 ВВОД СРЕДСТВ'"""
    await update.message.reply_text("💳 ВВОД СРЕДСТВ\nВыберите тип пополнения:", reply_markup=get_funds_menu())

# === ОБРАБОТКА ВВОДА СРЕДСТВ ===
async def handle_lime_deposit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка кнопки '1. ВВОД LIME'"""
    await update.message.reply_text("🟢 ВВОД LIME\nВыберите способ пополнения:", reply_markup=get_lime_submenu())

async def handle_lime_usdt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка кнопки '1.1 За USDT'"""
    try:
        await update.message.reply_text("🎥 Ввод LIME за USDT")
        await update.message.reply_video(video=VIDEO_LIME_USDT, caption="Как пополнить LIME за USDT.", reply_markup=get_lime_submenu())
    except Exception as e:
        logger.error("Ошибка при отправке видео LIME за USDT: %s", e)
        await update.message.reply_text("❌ Не удалось загрузить видео.", reply_markup=get_lime_submenu())

async def handle_lime_btc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка кнопки '1.2 За BTC'"""
    try:
        await update.message.reply_text("🎥 Ввод LIME за BTC")
        await update.message.reply_video(video=VIDEO_LIME_BTC, caption="Как пополнить LIME за BTC.", reply_markup=get_lime_submenu())
    except Exception as e:
        logger.error("Ошибка при отправке видео LIME за BTC: %s", e)
        await update.message.reply_text("❌ Не удалось загрузить видео.", reply_markup=get_lime_submenu())

async def handle_lime_rub(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка кнопки '1.3 За RUB'"""
    try:
        await update.message.reply_text("🎥 Ввод LIME за RUB")
        await update.message.reply_video(video=VIDEO_LIME_RUB, caption="Как пополнить LIME за рубли.", reply_markup=get_lime_submenu())
    except Exception as e:
        logger.error("Ошибка при отправке видео LIME за RUB: %s", e)
        await update.message.reply_text("❌ Не удалось загрузить видео.", reply_markup=get_lime_submenu())

async def handle_ulime_deposit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка кнопки '2. ВВОД uLIME'"""
    await update.message.reply_text("🟢 ВВОД uLIME\nВыберите способ пополнения:", reply_markup=get_ulime_submenu())

async def handle_ulime_usdt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка кнопки '2.1 За USDT'"""
    try:
        await update.message.reply_text("🎥 Ввод uLIME за USDT")
        await update.message.reply_video(video=VIDEO_ULIME_USDT, caption="Как пополнить uLIME за USDT.", reply_markup=get_ulime_submenu())
    except Exception as e:
        logger.error("Ошибка при отправке видео uLIME за USDT: %s", e)
        await update.message.reply_text("❌ Не удалось загрузить видео.", reply_markup=get_ulime_submenu())

async def handle_ulime_rub(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка кнопки '2.2 За RUB'"""
    try:
        await update.message.reply_text("🎥 Ввод uLIME за RUB")
        await update.message.reply_video(video=VIDEO_ULIME_RUB, caption="Как пополнить uLIME за рубли.", reply_markup=get_ulime_submenu())
    except Exception as e:
        logger.error("Ошибка при отправке видео uLIME за RUB: %s", e)
        await update.message.reply_text("❌ Не удалось загрузить видео.", reply_markup=get_ulime_submenu())

# === ОБРАБОТКА ВЫВОДА СРЕДСТВ ===
async def handle_lime_withdrawal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка кнопки '1. Lime' (вывод)"""
    await update.message.reply_text(
        "📤 Выберите опцию для вывода *Lime*:",
        parse_mode="Markdown",
        reply_markup=get_lime_withdrawal_inline_menu()
    )

async def handle_ulime_withdrawal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка кнопки '2. uLime' (вывод)"""
    await update.message.reply_text(
        "📤 Выберите валюту для вывода *uLime*:",
        parse_mode="Markdown",
        reply_markup=get_ulime_withdrawal_inline_menu()
    )

async def handle_bitlime_withdrawal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка кнопки '3. Bitlime' (вывод)"""
    await update.message.reply_text(
        "📤 Выберите валюту для вывода *Bitlime*:",
        parse_mode="Markdown",
        reply_markup=get_bitlime_withdrawal_inline_menu()
    )

# === НАВИГАЦИЯ ===
async def handle_back_to_deposit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка кнопки '⬅ Назад к ВВОДУ СРЕДСТВ'"""
    await update.message.reply_text("💳 ВВОД СРЕДСТВ\nВыберите тип пополнения:", reply_markup=get_funds_menu())

async def handle_back_to_lessons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка кнопки '⬅ Назад к урокам'"""
    await update.message.reply_text("Выбери урок:", reply_markup=get_lessons_menu())

# === ГЛАВНЫЙ ОБРАБОТЧИК СООБЩЕНИЙ ===
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Главный обработчик текстовых сообщений"""
    text = update.message.text.strip().lower()

    # Проверяем, находится ли пользователь в режиме связи с менеджером
    if context.user_data.get('forwarding_to_admin'):
        # Пересылаем сообщение администратору
        admin_message = f"📩 Сообщение от пользователя {update.message.from_user.name} (ID: {update.message.from_user.id}):\n{text}"
        try:
            await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=admin_message)
            await update.message.reply_text("✅ Сообщение отправлено менеджеру. Ждите ответа.")
        except Exception as e:
            logger.error(f"Ошибка при отправке сообщения администратору: {e}")
            await update.message.reply_text("❌ Не удалось отправить сообщение менеджеру. Попробуйте позже.")

        # Сбрасываем флаг после отправки
        context.user_data['forwarding_to_admin'] = False
        return

    # Маппинг кнопок на обработчики
    handlers = {
        '📚 школа новичка': handle_school,
        '📞 связь с менеджером': handle_support,
        '👉 Зарегистрироваться в Lime': handle_registration,
        '➡ выбор бнп': handle_bnp_selection,
        '💼 citro wallet': handle_citro_wallet,
        '💸 вывод средств': handle_withdrawal,
        '✅ как зарегистрироваться': handle_how_to_register,
        '📘 активация подписки': handle_subscription_activation,
        '💰 ввод средств': handle_deposit_funds,
        '1. ввод lime': handle_lime_deposit,
        '1.1 за usdt': handle_lime_usdt,
        '1.2 за btc': handle_lime_btc,
        '1.3 за rub': handle_lime_rub,
        '2. ввод ulime': handle_ulime_deposit,
        '2.1 за usdt': handle_ulime_usdt,
        '2.2 за rub': handle_ulime_rub,
        '⬅ назад к вводу средств': handle_back_to_deposit,
        '⬅ назад к урокам': handle_back_to_lessons,
        '1. lime': handle_lime_withdrawal,
        '2. ulime': handle_ulime_withdrawal,
        '3. bitlime': handle_bitlime_withdrawal,
    }

    # Вызываем соответствующий обработчик
    handler = handlers.get(text)
    if handler:
        await handler(update, context)
    else:
        # Если пользователь выбрал другую кнопку, сбрасываем режим связи с менеджером
        if context.user_data.get('forwarding_to_admin'):
            context.user_data['forwarding_to_admin'] = False
            await update.message.reply_text("Вы вернулись в главное меню", reply_markup=get_main_menu())
        else:

            await update.message.reply_text("🤖 Используй кнопки ниже для взаимодействия.", reply_markup=get_main_menu())




