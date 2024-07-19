from aiogram import Dispatcher, types, F, filters, Bot
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import asyncio

bot = Bot(token="7271305318:AAGmZKpCipa_4sLbXri0omXv1za6R8Meeco")
dp = Dispatcher(bot=bot)


keyboards = [
    [KeyboardButton(text='Lavash'), KeyboardButton(text="Clab Sandwich")],
    [KeyboardButton(text="Hot-dog"),KeyboardButton(text="Donar")],
    [KeyboardButton(text="Hamburger"), KeyboardButton(text="Free")],
    [KeyboardButton(text="Orders")]
]
main_button = ReplyKeyboardMarkup(keyboard=keyboards, resize_keyboard=True)

keyboards1 = [
    [KeyboardButton(text='Купить'), KeyboardButton(text="Не купить")]
]

buy_or_not = ReplyKeyboardMarkup(keyboard=keyboards1, resize_keyboard=True)



Orders = []



@dp.message(filters.Command("start"))
async def start(message: types.Message):
    await message.answer(f"Xush kelibsiz {message.from_user.full_name}, qorniz ochmi?", reply_markup=main_button)

@dp.message(F.text=="Free")
async def start(message: types.Message):
    await message.answer_photo(photo="https://i0.wp.com/images-prod.healthline.com/hlcmsresource/images/topic_centers/Food-Nutrition/1296x728_HEADER_Are-potatoes-gluten-free.jpg?w=1155&h=1528",
                               caption="Free tanladiz")

@dp.message(F.text=="Lavash")
async def start(message: types.Message):
    Orders.append("Lavash")
    await message.answer_photo(photo="https://yukber.uz/image/cache/catalog/lavash-700x700.jpg",
                               caption="Lavash tanladiz")



@dp.message(F.text=="Hot-dog")
async def start(message: types.Message):
    Orders.append("Hot-dog")
    await message.answer_photo(photo="https://upload.wikimedia.org/wikipedia/commons/b/b1/Hot_dog_with_mustard.png",
                               caption="Hot-Dog tanladiz")

@dp.message(F.text=="Clab Sandwich")
async def start(message: types.Message):
    Orders.append("Clab Sendwich")
    await message.answer_photo(photo="https://static.toiimg.com/thumb/83740315.cms?imgsize=361903&width=800&height=800",
                               caption="Clab Sandwich tanladiz")

@dp.message(F.text=="Hamburger")
async def start(message: types.Message):
    Orders.appen("Hamburger")
    await message.answer_photo(photo="https://heygrillhey.com/wp-content/uploads/2018/05/Smoked-Hamburgers-Feature.png",
                               caption="Hamburger tanladiz")



@dp.message(F.text=="Donar")
async def start(message: types.Message):
    Orders.append("Donar")
    await message.answer_photo(photo="https://cdn.fishandbread.com/products/9_1698040345.jpg",
                               caption="Donar tanladiz")



@dp.message(F.text == "Orders")
async def start(message: types.Message):
   
    await message.answer(f"{Orders}", reply_markup=buy_or_not)
    

@dp.message(F.text=="Купить")
async def start(message: types.Message):
    Orders.clear()
    await message.answer(f'siz sotib oldingiz')

@dp.message(F.text=="Не купить")
async def start(message: types.Message):
    Orders.clear()
    await message.answer(f'siz bekor qildingiz')

async def main():
    await dp.start_polling(bot)


if __name__ == 'main':
    asyncio.run(main())