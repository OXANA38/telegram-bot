from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# === ТЕКСТОВЫЕ МЕНЮ ===
def get_main_menu():
    """Главное меню"""
    return ReplyKeyboardMarkup([
        ['📚 Школа новичка'],
        ['📞 Связь с менеджером'],
        ['👉 Зарегистрироваться в Lime'],
        ['💼 Citro Wallet'],
        ['➡ Выбор БНП']
    ], resize_keyboard=True)

def get_lessons_menu():
    """Меню 'Школа новичка'"""
    return ReplyKeyboardMarkup([
        ['⬅ Назад', '✅ Как зарегистрироваться'],
        ['💰 ВВОД СРЕДСТВ'],
        ['📘 Активация подписки'],
        ['💸 ВЫВОД СРЕДСТВ']
    ], resize_keyboard=True)

def get_funds_menu():
    """Меню 'Ввод средств'"""
    return ReplyKeyboardMarkup([
        ['1. ВВОД LIME'],
        ['2. ВВОД uLIME'],
        ['⬅ Назад к урокам']
    ], resize_keyboard=True)

def get_lime_submenu():
    """Подменю 'Ввод LIME'"""
    return ReplyKeyboardMarkup([
        ['1.1 За USDT'],
        ['1.2 За BTC'],
        ['1.3 За RUB'],
        ['⬅ Назад к ВВОДУ СРЕДСТВ']
    ], resize_keyboard=True)

def get_ulime_submenu():
    """Подменю 'Ввод uLIME'"""
    return ReplyKeyboardMarkup([
        ['2.1 За USDT'],
        ['2.2 За RUB'],
        ['⬅ Назад к ВВОДУ СРЕДСТВ']
    ], resize_keyboard=True)

def get_withdrawal_submenu():
    """Подменю 'Вывод средств'"""
    return ReplyKeyboardMarkup([
        ['1. Lime'],
        ['2. uLime'],
        ['3. Bitlime'],
        ['⬅ Назад к урокам']
    ], resize_keyboard=True)

def get_lesson_menu():
    """Меню урока"""
    return ReplyKeyboardMarkup([
        ['Следующий урок', '⬅ Назад к урокам']
    ], resize_keyboard=True)

def get_support_menu():
    """Меню поддержки"""
    return ReplyKeyboardMarkup([
        ['⬅ Назад']
    ], resize_keyboard=True)

# === INLINE МЕНЮ ===
def get_bnp_inline_menu():
    """Inline-меню выбора БНП"""
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("uAUTO", callback_data="bnp_uauto")],
        [InlineKeyboardButton("uBitlime", callback_data="bnp_ubitlime")],
        [InlineKeyboardButton("uKaleidoscop", callback_data="bnp_ukaleidoscop")],
        [InlineKeyboardButton("MagicDRIVE", callback_data="bnp_magicdrive")],
        [InlineKeyboardButton("uHouse", callback_data="bnp_uhouse")]
    ])

def get_ulime_withdrawal_inline_menu():
    """Inline-меню вывода uLime"""
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Вывести uLime в RUB", callback_data="ulime_rub")],
        [InlineKeyboardButton("Вывести uLime в USDT", callback_data="ulime_usdt")],
        [InlineKeyboardButton("⬅ Назад", callback_data="back_to_withdrawal_menu")]
    ])

def get_lime_withdrawal_inline_menu():
    """Inline-меню вывода Lime"""
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Вывести Lime в RUB", callback_data="lime_rub")],
        [InlineKeyboardButton("⬅ Назад", callback_data="back_to_withdrawal_menu")]
    ])

def get_bitlime_withdrawal_inline_menu():
    """Inline-меню вывода Bitlime"""
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Вывести Bitlime в RUB", callback_data="bitlime_rub")],
        [InlineKeyboardButton("Вывести Bitlime в BTC", callback_data="bitlime_btc")],
        [InlineKeyboardButton("⬅ Назад", callback_data="back_to_withdrawal_menu")]
    ])

def get_back_to_menu_button(menu_type):
    """Кнопка 'Назад' для inline-меню"""
    if menu_type == "lime":
        return InlineKeyboardMarkup([[InlineKeyboardButton("⬅ Назад", callback_data="back_to_lime_menu")]])
    elif menu_type == "ulime":
        return InlineKeyboardMarkup([[InlineKeyboardButton("⬅ Назад", callback_data="back_to_ulime_menu")]])
    elif menu_type == "bitlime":
        return InlineKeyboardMarkup([[InlineKeyboardButton("⬅ Назад", callback_data="back_to_bitlime_menu")]])
    else:

        return InlineKeyboardMarkup([[InlineKeyboardButton("⬅ Назад", callback_data="back_to_withdrawal_menu")]])

