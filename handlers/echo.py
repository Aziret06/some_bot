from aiogram import Router, types

echo_router = Router()


@echo_router.message()
async def echo(message: types.Message):
    # logging.info(message)
    lst = []
    text = message.text.split()[::-1]
    for i in text:
        lst.append(i)
    await message.answer(' '.join(lst))
