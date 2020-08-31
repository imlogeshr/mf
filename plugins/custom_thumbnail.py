# Copyright (C) 2020 by surlogu@Github, < https://github.com/surlogu>.
#
# This file is part of < https://github.com/surlogu/AsEnDL > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/surlogu/AsEnDL/blob/master/LICENSE >
#
# All rights reserved.

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import numpy
import os
from PIL import Image
import time

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

#from helper_funcs.chat_base import TRChatBase
import helper_funcs.database as sql


@pyrogram.Client.on_message(pyrogram.Filters.command(["savethumbnail"]))
async def savethumbnail(bot, update):
    if update.from_user.id not in Config.AUTH_USERS:
        await bot.delete_messages(
            chat_id=update.chat.id,
            message_ids=update.message_id,
            revoke=True
        )
        return
    if update.reply_to_message.media_group_id is not None:
        # album is sent
        download_location = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + "/" + str(update.reply_to_message.media_group_id) + "/"
        # create download directory, if not exist
        if not os.path.isdir(download_location):
            os.makedirs(download_location)
        await sql.df_thumb(update.from_user.id, update.reply_to_message.message_id)
        await bot.download_media(
            message=update.reply_to_message,
            file_name=download_location
        )
    else:
        # received single photo
        download_location = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + ".jpg"
        await sql.df_thumb(update.from_user.id, update.reply_to_message.message_id)
        await bot.download_media(
            message=update.reply_to_message,
            file_name=download_location
        )
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.SAVED_CUSTOM_THUMB_NAIL,
            reply_to_message_id=update.message_id
        )

@pyrogram.Client.on_message(pyrogram.Filters.photo)
async def save_photo(bot, update):
    if update.from_user.id not in Config.AUTH_USERS:
        await bot.delete_messages(
            chat_id=update.chat.id,
            message_ids=update.message_id,
            revoke=True
        )
        return
    #TRChatBase(update.from_user.id, update.text, "save_photo")
    if update.media_group_id is not None:
        # album is sent
        download_location = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + "/" + str(update.media_group_id) + "/"
        # create download directory, if not exist
        if not os.path.isdir(download_location):
            os.makedirs(download_location)
        await sql.df_thumb(update.from_user.id, update.message_id)
        await bot.download_media(
            message=update,
            file_name=download_location
        )
    else:
        # received single photo
        download_location = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + ".jpg"
        await sql.df_thumb(update.from_user.id, update.message_id)
        await bot.download_media(
            message=update,
            file_name=download_location
        )
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.SAVED_CUSTOM_THUMB_NAIL,
            reply_to_message_id=update.message_id
        )

@pyrogram.Client.on_message(pyrogram.Filters.command(["viewthumbnail"]))
async def view_thumbnail(bot, update):
    if update.from_user.id not in Config.AUTH_USERS:
        await bot.delete_messages(
            chat_id=update.chat.id,
            message_ids=update.message_id,
            revoke=True
        )
        return
    #TRChatBase(update.from_user.id, update.text, "deletethumbnail")
    download_location = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + ".jpg"
    if os.path.exists(download_location):
        await bot.send_photo(
            chat_id=update.chat.id,
            photo=download_location,
            reply_to_message_id=update.message_id
      )
    else:
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.NO_CUSTOM_THUMB_NAIL_FOUND,
            reply_to_message_id=update.message_id
     )

@pyrogram.Client.on_message(pyrogram.Filters.command(["clearthumbnail"]))
async def delete_thumbnail(bot, update):
    if update.from_user.id not in Config.AUTH_USERS:
        await bot.delete_messages(
            chat_id=update.chat.id,
            message_ids=update.message_id,
            revoke=True
        )
        return
    #TRChatBase(update.from_user.id, update.text, "deletethumbnail")
    download_location = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id)
    try:
        await sql.del_thumb(update.from_user.id)
        os.remove(download_location + ".jpg")
        # os.remove(download_location + ".json")
    except:
        pass
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.DEL_ETED_CUSTOM_THUMB_NAIL,
        reply_to_message_id=update.message_id
    )
