import asyncio
from aiogram import Bot, Dispatcher, types, F
import logging

from aiogram.enums import ParseMode
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from inline_buttons import inline_button1, inline_button2, inline_button3
from buttons import button1

from config import TOKEN, CHANNEL


class RegisterSchool(StatesGroup):
    parents_name = State()
    child_name = State()
    child_class = State()
    month_price = State()
    finish = State()


class RegisterUniversity(StatesGroup):
    parents_name = State()
    student_name = State()
    student_class = State()
    month_price = State()
    finish = State()


class RegisterAcademy(StatesGroup):
    parents_name = State()
    child_name = State()
    child_class = State()
    month_price = State()
    finish = State()


dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"<b>Assalomu Aleykum\nXurmatli {message.from_user.mention_html()}</b>", reply_markup=button1)


@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        f"<b>Sizga qanday yordam bera olaman {message.from_user.mention_html()}\nBizda mavjud buyruqlar : /start</b>")


@dp.message(F.text == "PDP School")
async def cmd_school(message: types.Message):
    await message.answer_photo(photo="https://cdn.telegram-store.com/channels/bola-tarbiyasi/18424-2023-09-10-1-.jpg",
                               text="<b>Kiring yoki Ro'yhatdan o'ting ❗️</b>",
                               reply_markup=inline_button1.as_markup())


@dp.message(F.text == "PDP University")
async def cmd_university(message: types.Message):
    await message.answer_photo(photo="https://i.ytimg.com/vi/hCS8Hvau0dc/maxresdefault.jpg",
                               caption="<b>Kiring yoki Ro'yhatdan o'ting ❗️</b>",
                               reply_markup=inline_button2.as_markup())


@dp.message(F.text == "PDP Academy")
async def cmd_academy(message: types.Message):
    await message.answer_photo(photo="https://online.pdp.uz/assets/newPdp/gallery/pdp-03.jpg/",
                               caption="<b>Kiring yoki Ro'yhatdan o'ting ❗️</b>",
                               reply_markup=inline_button3.as_markup())


@dp.callback_query(F.data == "button2")
async def cmd_callbutton1(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("<b>Otangiz yoki Onangizni to'liq ism familiyasini kiriting ❗️</b>",
                              reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(RegisterSchool.parents_name)


@dp.message(RegisterSchool.parents_name)
async def cmd_callbutton_1(message: types.Message, state: FSMContext):
    await state.update_data(parents_name=message.text)
    await message.answer("<b>Farzandingizni to'liq ism familiyasi kiriting ❗️</b>")
    await state.set_state(RegisterSchool.child_name)


@dp.message(RegisterSchool.child_name)
async def cmd_callbutton1(message: types.Message, state: FSMContext):
    await state.update_data(child_name1=message.text)
    await message.answer("<b>Farzandingiz nechinchi sinfda o'qishini kiriting ❗️</b>")
    await state.set_state(RegisterSchool.child_class)


@dp.message(RegisterSchool.child_class)
async def cmd_callbutton1(message: types.Message, state: FSMContext):
    if message.text.isnumeric():
        await state.update_data(child_class1=message.text)
        await message.answer("<b>Necha oy uchun to'lov qila olasiz ❓</b>")
        await state.set_state(RegisterSchool.month_price)
    else:
        await message.answer("<b>Xatolik ❗️, faqat raqamlarda kiritish mumkin ❗️</b>")


@dp.message(RegisterSchool.month_price)
async def cmd_callbutton1(message: types.Message, state: FSMContext, bot: Bot):
    if message.text.isnumeric():
        await state.update_data(month_price1=message.text)
        await state.set_state(RegisterSchool.finish)
        await message.answer("<b>Ma'lumotlar qabul qilindi ✅\nTez orada mutaxasislarimiz aloqaga chiqadi 😊</b>")
        data1 = await state.get_data()
        parents_fullname = data1.get("parents_name", "Unknown")
        child_name1 = data1.get("child_name1", "Unknown")
        child_class1 = data1.get("child_class1", "Unknown")
        month_price1 = data1.get("month_price1", "Unknown")
        msg = f"""<b>
Yangi O'quvchi ❗️
Qayerga: PDP School
Ota yoki onaning to'liq ismi: {parents_fullname}
O'quvchining to'liq ismi: {child_name1}
O'quvchining sinfi: {child_class1}
O'quvchining to'lov qilgan muddati: {month_price1}
       </b> """
        await bot.send_message(chat_id=CHANNEL, text=msg)
    else:
        await message.answer("<b>Faqat raqamlarda kiriting mumkin ❗️\n Qayta urining</b>")


async def main():
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
