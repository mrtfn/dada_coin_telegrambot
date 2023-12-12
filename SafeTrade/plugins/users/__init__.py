from pyrogram.client import Client
from pyrogram import filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from SafeTrade import bot
from SafeTrade.helpers.start_constants import *
from SafeTrade.helpers.decorator import rate_limiter
from SafeTrade.config import OWNER_USERID, SUDO_USERID


@Client.on_callback_query(filters.regex("_TRADE"))  # type: ignore
@rate_limiter
async def tradeCallbacks(_, CallbackQuery: CallbackQuery):
    clicker_user_id = CallbackQuery.from_user.id
    user_id = CallbackQuery.message.reply_to_message.from_user.id

    if CallbackQuery.data == "START_TRADE":
        await CallbackQuery.edit_message_text(
            START_TRADE_CAPTION,
        )
