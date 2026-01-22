import logging
import os
import asyncio
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from config import (
    UAUTO_IMAGE_URL, UBITLIME_IMAGE_URL, MAGICDRIVE_IMAGE_URL, UHOUSE_IMAGE_URL,
    PRESENTATION_PATHS
)
from keyboards import (
    get_lime_withdrawal_inline_menu, get_ulime_withdrawal_inline_menu,
    get_bitlime_withdrawal_inline_menu, get_back_to_menu_button
)
from utils import check_presentation_file
from handlers.messages import handle_withdrawal

logger = logging.getLogger(__name__)

async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик всех inline-кнопок"""
    query = update.callback_query
    await query.answer()
    data = query.data

    # === ОБРАБОТКА ВЫВОДА СРЕДСТВ ===
    if data == "lime_rub":
        await query.edit_message_text(
            text="📤 Вывод *Lime* в *RUB*.\n\n"
                 "Для оформления заявки на вывод, пожалуйста, свяжитесь с менеджером через кнопку '📞 Связь с менеджером' в главном меню.",
            parse_mode="Markdown",
            reply_markup=get_back_to_menu_button("lime")
        )

    elif data == "back_to_lime_menu":
        await query.edit_message_text(
            text="📤 Выберите опцию для вывода *Lime*:",
            parse_mode="Markdown",
            reply_markup=get_lime_withdrawal_inline_menu()
        )

    elif data == "ulime_rub":
        await query.edit_message_text(
            text="📤 Вывод *uLime* в *RUB*.\n\n"
                 "Для оформления заявки на вывод, пожалуйста, свяжитесь с менеджером через кнопку '📞 Связь с менеджером' в главном меню.",
            parse_mode="Markdown",
            reply_markup=get_back_to_menu_button("ulime")
        )

    elif data == "ulime_usdt":
        await query.edit_message_text(
            text="📤 Вывод *uLime* в *USDT*.\n\n"
                 "Для оформления заявки на вывод, пожалуйста, свяжитесь с менеджером через кнопку '📞 Связь с менеджером' в главном меню.",
            parse_mode="Markdown",
            reply_markup=get_back_to_menu_button("ulime")
        )

    elif data == "back_to_ulime_menu":
        await query.edit_message_text(
            text="📤 Выберите валюту для вывода *uLime*:",
            parse_mode="Markdown",
            reply_markup=get_ulime_withdrawal_inline_menu()
        )

    elif data == "bitlime_rub":
        await query.edit_message_text(
            text="📤 Вывод *Bitlime* в *RUB*.\n\n"
                 "Для оформления заявки на вывод, пожалуйста, свяжитесь с менеджером через кнопку '📞 Связь с менеджером' в главном меню.",
            parse_mode="Markdown",
            reply_markup=get_back_to_menu_button("bitlime")
        )

    elif data == "bitlime_btc":
        await query.edit_message_text(
            text="📤 Вывод *Bitlime* в *BTC*.\n\n"
                 "Для оформления заявки на вывод, пожалуйста, свяжитесь с менеджером через кнопку '📞 Связь с менеджером' в главном меню.",
            parse_mode="Markdown",
            reply_markup=get_back_to_menu_button("bitlime")
        )

    elif data == "back_to_bitlime_menu":
        await query.edit_message_text(
            text="📤 Выберите валюту для вывода *Bitlime*:",
            parse_mode="Markdown",
            reply_markup=get_bitlime_withdrawal_inline_menu()
        )

    elif data == "back_to_withdrawal_menu":
        # Возврат к текстовому меню "Вывод средств"
        await handle_withdrawal(update, context)

    # === ОБРАБОТКА CITRO WALLET КНОПОК ===
    elif data == "citro_empty_1":
        await context.bot.copy_message(
            chat_id=query.message.chat_id,
            from_chat_id="@dgagidga",
            message_id=21,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🌀 Что такое CITRO", callback_data="citro_empty_3")],
                [InlineKeyboardButton("📦 Что такое C-Box", callback_data="citro_empty_2")]
            ])
        )

    elif data == "citro_empty_2":
        await context.bot.copy_message(
            chat_id=query.message.chat_id,
            from_chat_id="@dgagidga",
            message_id=23,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📝 Как участвовать в C-Box", callback_data="citro_cbox_howto")],
                [InlineKeyboardButton("🔐 Что такое C-Wallet", callback_data="citro_empty_1")]
            ])
        )

    elif data == "citro_empty_3":
        await context.bot.copy_message(
            chat_id=query.message.chat_id,
            from_chat_id="@dgagidga",
            message_id=22,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔐 Что такое C-Wallet", callback_data="citro_empty_1")],
                [InlineKeyboardButton("📦 Что такое C-Box", callback_data="citro_empty_2")]
            ])
        )

    elif data == "citro_cbox_howto":
        await context.bot.copy_message(
            chat_id=query.message.chat_id,
            from_chat_id="@dgagidga",
            message_id=24,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📊 Что по цифрам?", callback_data="citro_cbox_numbers")],
                [InlineKeyboardButton("🔐 Что такое C-Wallet", callback_data="citro_empty_1")]
            ])
        )

    elif data == "citro_cbox_numbers":
        try:
            # 1. Отправляем пост 25
            await context.bot.copy_message(
                chat_id=query.message.chat_id,
                from_chat_id="@dgagidga",
                message_id=25,
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("1️⃣ Минимальный старт", callback_data="sbox_minimal")],
                    [InlineKeyboardButton("2️⃣ Комфортный 1+2", callback_data="sbox_comfort")],
                    [InlineKeyboardButton("3️⃣ Скоростной 1+6", callback_data="sbox_speed")]
                ])
            )

            # 2. Отправляем PDF презентацию
            await asyncio.sleep(1)
            pdf_path = "/home/VitokStar/C-Box_programm.pdf"

            if os.path.exists(pdf_path):
                with open(pdf_path, "rb") as pdf_file:
                    await query.message.reply_document(
                        document=pdf_file,
                        filename="C-Box_programm.pdf",
                        caption="📄 Презентация C-Box программы"
                    )
            else:
                await query.message.reply_text(f"❌ Файл презентации не найден:\n{pdf_path}")

        except Exception as e:
            logger.error(f"Ошибка в 'Что по цифрам': {e}")
            await query.edit_message_text(
                text="📊 *Что по цифрам?*\n\nhttps://t.me/dgagidga/25",
                parse_mode="Markdown",
                disable_web_page_preview=False
            )

    elif data == "sbox_minimal":
        await context.bot.copy_message(
            chat_id=query.message.chat_id,
            from_chat_id="@dgagidga",
            message_id=27,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("💎 Комфортный 1+2", callback_data="sbox_comfort")],
                [InlineKeyboardButton("⚡ Скоростной 1+6", callback_data="sbox_speed")],
                [InlineKeyboardButton("✅ Выбираю минимальный", callback_data="sbox_choose_minimal")]
            ])
        )

    elif data == "sbox_comfort":
        await context.bot.copy_message(
            chat_id=query.message.chat_id,
            from_chat_id="@dgagidga",
            message_id=29,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("✅ Выбираю комфортный", callback_data="sbox_choose_comfort")],
                [InlineKeyboardButton("1️⃣ Минимальный старт", callback_data="sbox_minimal")],
                [InlineKeyboardButton("3️⃣ Скоростной 1+6", callback_data="sbox_speed")]
            ])
        )

    elif data == "sbox_speed":
        # 1. Отправляем пост 30
        await context.bot.copy_message(
            chat_id=query.message.chat_id,
            from_chat_id="@dgagidga",
            message_id=30
        )

        # 2. Отправляем видео 31
        await context.bot.copy_message(
            chat_id=query.message.chat_id,
            from_chat_id="@dgagidga",
            message_id=31
        )

        # 3. Кнопки после видео
        await query.message.reply_text(
            "⚡ *Скоростной 1+6*\n\nВыберите действие:",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("✅ Выбираю скоростной", callback_data="sbox_choose_speed")],
                [InlineKeyboardButton("1️⃣ Минимальный старт", callback_data="sbox_minimal")],
                [InlineKeyboardButton("2️⃣ Комфортный 1+2", callback_data="sbox_comfort")]
            ])
        )

    elif data == "sbox_choose_minimal":
        await context.bot.copy_message(
            chat_id=query.message.chat_id,
            from_chat_id="@dgagidga",
            message_id=28,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("1️⃣ Написать Оксане", url="https://t.me/Oksanasana197")],
                [InlineKeyboardButton("2️⃣ Зарегистрироваться", url="https://t.me/Citro_wallet_bot?start=NDE3Mjc5OTIyOmQ2ZTAyOTgwNDYyNzZjN2Q2Mjc4MzQ3NA")]
            ])
        )

    elif data == "sbox_choose_comfort":
        await context.bot.copy_message(
            chat_id=query.message.chat_id,
            from_chat_id="@dgagidga",
            message_id=28,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("1️⃣ Написать Оксане", url="https://t.me/Oksanasana197")],
                [InlineKeyboardButton("2️⃣ Зарегистрироваться", url="https://t.me/Citro_wallet_bot?start=NDE3Mjc5OTIyOmQ2ZTAyOTgwNDYyNzZjN2Q2Mjc4MzQ3NA")]
            ])
        )

    elif data == "sbox_choose_speed":
        await context.bot.copy_message(
            chat_id=query.message.chat_id,
            from_chat_id="@dgagidga",
            message_id=28,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("1️⃣ Написать Оксане", url="https://t.me/Oksanasana197")],
                [InlineKeyboardButton("2️⃣ Зарегистрироваться", url="https://t.me/Citro_wallet_bot?start=NDE3Mjc5OTIyOmQ2ZTAyOTgwNDYyNzZjN2Q2Mjc4MzQ3NA")]
            ])
        )

    # === ОБРАБОТКА BNP ПРОГРАММ ===
    elif data == "bnp_uauto":
        await handle_bnp_program(
            query, context,
            image_url=UAUTO_IMAGE_URL,
            presentation_path=PRESENTATION_PATHS.get("uauto", "presentation_uauto.pptx"),
            description=(
                "🚗 *uAUTO – это ваш прямой путь к новому автомобилю из автосалона, без переплат и стресса.*\n\n"
                "*🔥 Почему uAUTO – Лучший Выбор для Автолюбителей:*\n\n"
                "• *⏱️ Быстрый Результат – Всего 5 Уровней:* Ваша мечта станет реальности быстрее, чем вы думаете! Всего *5 простых уровней* отделяют вас от ключей от нового авто.\n"
                "• *🎯 Целевая Программа:* Мы знаем, чего вы хотите! *Цель программы – покупка любого нового автомобиля* из любого автосалона. Никаких отвлечений, только результат.\n"
                "• *💱 Удобные Расчёты в USDT:* Современное решение для современных людей. Все операции проходят в *стабильной криптовалюте USDT*, обеспечивая прозрачность и удобство.\n"
                "• *🚀 Быстрый Возврат Вложений:* Начните получать *средства обратно уже на ранних этапах*. Ваши средства возвращаются быстро, позволяя вам двигаться к цели с минимальными финансовыми вложениями.\n"
                "• *💰 Мощная Партнёрская Программа:* Приглашайте друзей и единомышленников! Получайте *до $15 000 с каждого лично приглашённого партнёра*. Помогайте другим, пока строите собственный бизнес и приближаетесь к своей цели!\n\n"
                "*uAUTO – это не просто программа, это ваш личный автосалон с уникальными условиями и мощной поддержкой!*"
            ),
            program_name="uAUTO"
        )

    elif data == "bnp_ubitlime":
        await handle_bnp_program(
            query, context,
            image_url=UBITLIME_IMAGE_URL,
            presentation_path=PRESENTATION_PATHS["ubitlime"],
            description=(
                "💼 *uBitlime: Ваш Ежедневный Доход и Финансовая Свобода!*\n\n"
                "Мечтаете о стабильном пассивном доходе, который растет каждый день? *uBitlime* – это ваш ключ к *ежедневному денежному потоку* с мощными партнёрскими бонусами!\n\n"
                "*🚀 Почему uBitlime – Идеальный Выбор для Финансового Роста:*\n\n"
                "*   💰 Деньги на Каждый День:* Получайте *регулярные выплаты* уже с первых дней участия. Ваш доход становится предсказуемым и стабильным.\n"
                "*   📈 Выплаты и Партнёрские на Каждом Уровне:* Каждый из уровней приносит вам *доход и щедрые вознаграждения* от вашей команды. Зарабатывайте на всех этапах программы.\n"
                "*   💱 Удобные Расчёты в USDT:* Все операции проводятся в *стабильной криптовалюте USDT*, обеспечивая надежность и прозрачность ваших финансов.\n"
                "*   ⚡ Быстрые X20:* Достигайте *множителей дохода до X20* на ранних этапах. Быстрые результаты мотивируют двигаться дальше.\n"
                "*   👥 Масштабирование с Клонами:* Увеличивайте свой заработок экспоненциально, используя *гибкую систему клонов*. Стройте мощную команду и расширяйте бизнес без ограничений.\n\n"
                "*uBitlime – это не просто программа, это ваш личный финансовый двигатель для ежедневного роста и стабильности!*"
            ),
            program_name="uBitlime"
        )

    elif data == "bnp_magicdrive":
        await handle_bnp_program(
            query, context,
            image_url=MAGICDRIVE_IMAGE_URL,
            presentation_path=PRESENTATION_PATHS["magicdrive"],
            description=(
                "₿ *Magic DRIVE — твой путь в будущее, где деньги работают на тебя в биткоинах! 💥*\n\n"
                "*🚀 Почему это не просто программа — а прорыв?*\n\n"
                "*✅ Доход в BTC* — ты зарабатываешь в настоящей цифровой валюте будущего, а не в обесценивающихся фиатах!\n"
                "*✅ Нулевые риски потерь* — никаких «всё или ничего». Твой капитал защищён, а рост — стабилен и предсказуем.\n"
                "*✅ 8 активных источников дохода* — ты не просто получаешь, ты умножаешь! Пассив, структура, бонусы, рост — всё работает на тебя, даже когда ты спишь. 🌙💰\n"
                "*✅ Реферальная система на 15 уровней* — да, ты читаешь правильно! 🤯\n"
                "Ты строишь команду — и получаешь вознаграждение глубоко вниз по структуре, как капитан, ведущий флот к успеху!\n\n"
                "*🔥 Magic DRIVE — для тех, кто мыслит масштабно.*\n"
                "Для тех, кто выбирает свободу.\n"
                "Для тех, кто готов получать BTC — не гадая, а стратегически.\n\n"
                "*Ты не вкладываешься в мечту.*\n"
                "*Ты вступаешь в движение, которое уже движется к вершине.*\n\n"
                "*💫 Время действовать.*\n"
                "₿ *Magic DRIVE — твой биткоин-двигатель. Включай! ⚡*"
            ),
            program_name="Magic DRIVE"
        )

    elif data == "bnp_uhouse":
        await handle_bnp_program(
            query, context,
            image_url=UHOUSE_IMAGE_URL,
            presentation_path=PRESENTATION_PATHS["uhouse"],
            description=(
                "🏠 *uHouse: Ваш Дом – Ваша Финансовая Крепость!*\n\n"
                "Мечтаете о собственном доме без ипотечного бремени? *uHouse* – это ваш прямой путь к *жилью мечты стоимостью до $250 000* без долгов!\n\n"
                "*🚀 Основные Преимущества uHouse:*\n\n"
                "*   🎯 Целевая Выплата $250 000:* Ваша конечная цель – получить средства на покупку недвижимости или погашение ипотеки. Четко, конкретно, измеримо.\n"
                "*   🏡 Свобода Выбора:* Купите *любую недвижимость* на ваш вкус – квартиру, дом, таунхаус – или используйте средства, чтобы *полностью закрыть ипотеку* и обрести финансовую свободу.\n"
                "*   ⏱️ Быстрый Результат – Всего 6 Уровней:* Забудьте о бесконечных марафонах! *uHouse состоит всего из 6 уровней*, что делает путь к вашей цели коротким и понятным.\n"
                "*   💰 Доход на Каждом Шаге:* Получайте *промежуточные выплаты на каждом из 6 уровней*. Ваша финансовая стабильность растет постепенно, обеспечивая мотивацию и реальные деньги уже по ходу программы.\n\n"
                "*uHouse – это не просто программа, это инвестиция в ваше стабильное и независимое будущее!*"
            ),
            program_name="uHouse"
        )

    elif data == "bnp_ukaleidoscop":
        VIDEO_URL = "https://t.me/dgagidga/33"
        DESCRIPTION_TEXT = """🎭 uKaleidoscop: Ваша Фрактальная Финансовая Вселенная и 5 Источников Дохода в Одном!
Мечтаете не просто о пассивном доходе, а о целой экосистеме, которая автоматически множит ваши возможности? uKaleidoscop — это не очередная линейная программа, а ваш персональный финансовый «калейдоскоп», где один взмах создает множество прибыльных паттернов!

🚀 Почему uKaleidoscop — Эволюция в Мире Доходов:

🎯 Один вход — Пять Вселенных: Совершив всего один стартовый взнос (~130$), вы автоматически активируете 5 независимых источников дохода в USDT. Ваш капитал начинает работать одновременно в uKaleidoscop, uBitlime, uAuto, uHouse и программе Lime. Это как купить один билет и получить доступ на все финансовые аттракционы!

💰 Доход по пути к Вершине: Цель — 25 000$, но настоящая магия в пути. Вы зарабатываете в разы больше этой суммы благодаря сложным процентам, партнерским бонусам и клонированию на всех уровнях каждой из пяти программ. Ваш общий доход ограничен только скоростью роста вашей команды.

⚡ Автозапуск Клонов и Масштабирование: С самого старта uKaleidoscop автоматически «запускает клонов» во все связанные программы. Вы строите не одну, а пять синергичных команд одновременно, экспоненциально умножая поступления с каждого уровня каждой программы.

🔁 Синергия и Стабильность: Разные программы — разные циклы и темпы роста. Если в одной временная пауза, остальные четыре продолжают генерировать поток. Это создает беспрецедентную стабильность и регулярность выплат.

💎 Низкий Порог, Высокий Потолок: Начать финансовую трансформацию можно с суммы около 130$. Это делает вход максимально доступным, в то время как потенциал дохода стремится к бесконечности благодаря фрактальной модели.

uKaleidoscop — это не просто «еще одна программа». Это готовый, автоматизированный финансовый конструктор, который строит для вас многомерную матрицу дохода. Одно решение — и вы становитесь полноправным участником пяти прибыльных экосистем, где ваш рост умножается самим принципом синергии!"""
        PRESENTATION_URL = "https://t.me/dgagidga/34"

        try:
            await query.message.reply_video(video=VIDEO_URL, caption="")
            logger.info("Видео uKaleidoscop отправлено")
            await query.message.reply_text(DESCRIPTION_TEXT, parse_mode="Markdown")
            logger.info("Описание uKaleidoscop отправлено")
            await query.message.reply_document(document=PRESENTATION_URL, filename="presentation_ukaleidoscop.pptx")
            logger.info("Презентация uKaleidoscop отправлена")
        except Exception as e:
            logger.error(f"Ошибка при отправке материалов uKaleidoscop: {e}")
            await query.message.reply_text("❌ Произошла ошибка при загрузке материалов.")

    else:
        logger.warning(f"Неизвестный callback_data: {data}")
        await query.message.reply_text("❌ Неизвестная команда.")

async def handle_bnp_program(query, context, image_url, presentation_path, description, program_name):
    """Общая функция для обработки BNP программ"""
    try:
        # 1. Отправка изображения
        try:
            await query.message.reply_photo(photo=image_url, caption="")
            logger.info(f"Изображение {program_name} отправлено")
        except Exception as e_img:
            logger.error(f"Ошибка при отправке изображения {program_name}: {e_img}")

        # 2. Отправка описания
        try:
            await query.message.reply_text(description, parse_mode="Markdown")
            logger.info(f"Описание {program_name} отправлено")
        except Exception as e_text:
            logger.error(f"Ошибка при отправке текста {program_name}: {e_text}")

        # 3. Отправка презентации
        if check_presentation_file(presentation_path):
            try:
                with open(presentation_path, "rb") as file:
                    await query.message.reply_document(
                        document=file,
                        filename=f"presentation_{program_name.lower().replace(' ', '_')}.pptx"
                    )
                logger.info(f"Презентация {program_name} отправлена")
            except Exception as e_file:
                logger.error(f"Ошибка при отправке файла {program_name}: {e_file}")

        else:
            await query.message.reply_text(f"❌ Файл презентации {program_name} не найден.")

    except Exception as e:
        logger.error(f"Ошибка при обработке {program_name}: {e}", exc_info=True)
        await query.message.reply_text(f"❌ Произошла ошибка при обработке запроса {program_name}.")