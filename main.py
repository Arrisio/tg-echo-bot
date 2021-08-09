from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram import executor

from settings import Settings

settings = Settings()
bot = Bot(settings.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


def escape_spec_characters(text: str) -> str:
    return text.replace(">", "&#62;").replace("<", "&#60")

# @dp.message_handler(Command("test"), state=None)
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(escape_spec_characters(message.text))



async def on_startup_notify(dp: Dispatcher):
    if admin := settings.ADMIN_TG_ID:
        try:
            await dp.bot.send_message(admin, "Бот Запущен и готов к работе!")
        except Exception:
            pass





async def on_startup(dp):
    # import middlewares
    # middlewares.setup(dp)
    await on_startup_notify(dp)

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
