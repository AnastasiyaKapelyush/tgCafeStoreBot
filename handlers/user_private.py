# Обработчики событий общения пользователя с ботом в личке
from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f
from filters.chat_types import ChatTypeFilter

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter({'private'}))

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет, я виртуальный помощник')

@user_private_router.message(or_f(Command('menu'), F.text.lower().contains('меню')))
async def menu_cmd(message: types.Message):
    await message.answer("Вот меню:")

@user_private_router.message(Command('about'))
async def about_cmd(message: types.Message):
    await message.answer("О нас:")

@user_private_router.message(F.text.lower().contains('оплат'))
@user_private_router.message(Command('payment'))
async def payment_cmd(message: types.Message):
    await message.answer("Варианты оплаты:")

@user_private_router.message(F.text.lower().contains('доставк'))
@user_private_router.message(Command('shipping'))
async def shipping_cmd(message: types.Message):
    await message.answer("Варианты доставки:")