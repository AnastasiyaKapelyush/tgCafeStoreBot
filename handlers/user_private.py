# Обработчики событий общения пользователя с ботом в личке
from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f
from aiogram.utils.formatting import as_list, as_marked_section, Bold

from filters.chat_types import ChatTypeFilter
from keyboards import reply

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter({'private'}))

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет, я виртуальный помощник', reply_markup=reply.start_kb)

@user_private_router.message(or_f(Command('menu'), F.text.lower().contains('меню')))
async def menu_cmd(message: types.Message):
    await message.answer("Вот меню:", reply_markup=reply.remove_kb)

@user_private_router.message(or_f(Command('about'), F.text.lower().contains('о магазине')))
async def about_cmd(message: types.Message):
    await message.answer("О нас:", reply_markup=reply.remove_kb)

@user_private_router.message(or_f(Command('payment'), F.text.lower().contains('оплат')))
async def payment_cmd(message: types.Message):
    text = as_marked_section(
        Bold("Варианты оплаты:"),
        "Онлайн в боте",
        "Картой при получении",
        "Наличными при получении",
        "В заведении",
        marker="✅ "
    )
    await message.answer(text.as_html(), reply_markup=reply.remove_kb)

@user_private_router.message(or_f(Command('shipping'), F.text.lower().contains('доставк')))
async def shipping_cmd(message: types.Message):
    text = as_list(
        as_marked_section(
            Bold("Варианты доставки:"),
            "Самовывоз",
            "Курьерская доставка",
            marker="✅ "
        ),
        as_marked_section(
            Bold("Невозможно:"),
            "Почтой", 
            "Голубями",
            marker="❌ "
        ),
        sep="\n \n"
    )
    await message.answer(text.as_html(), reply_markup=reply.remove_kb)