from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="ðá´á´á´ÉªÉ´ð",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="âá´á´á´Êâ",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="ð¤£ÊÊá´á´á´ÊÉªsá´ð¤£",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ð»ÊÊá´á´á´á´á´sá´ð»",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="ðÉ¢Êá´É´ð",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="ð¥°ÊÊÊÉªá´sð¥°",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ðá´©ÉªÉ´É¢ð",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="â¸á´©Êá´Êâ¸",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="âï¸á´©Êá´ÊÊÉªsá´â¶ï¸",
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ð¥á´ Éªá´á´á´á´Êá´á´sð¥",
                    callback_data="help_callback hb10",
                ),
                InlineKeyboardButton(
                    text="ðsá´á´Êá´ð",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="ð¤­sá´á´á´ð¤­",
                    callback_data="help_callback hb9",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                )
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="Êá´Êá´©",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
