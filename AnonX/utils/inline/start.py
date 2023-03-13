from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🤗ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ🤗",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ], 
        [
            InlineKeyboardButton(text="🥳ʜᴇʟᴩ🥳", callback_data="settings_back_helper")
        ],
        [
            InlineKeyboardButton(text="🥀ᴏᴡɴᴇʀ🌹", url="https://t.me/Mr_Yamraj_xd"),
            InlineKeyboardButton(text="🌷sᴜᴘᴘᴏʀᴛ🌿", url=f"https://t.me/Sanki_Official")
        ],
        [
            InlineKeyboardButton(text="🤩ᴜᴘᴅᴀᴛᴇs🤩", url="https://t.me/DEADLY_NETWORK")
        ],
     ]
    return buttons
