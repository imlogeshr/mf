class Translation(object):
    START_TEXT = """𝐇𝐢, 𝐓𝐡𝐚𝐧𝐤 𝐘𝐨𝐮 𝐟𝐨𝐫 𝐮𝐬𝐢𝐧𝐠 𝐦𝐞.
/help 𝐭𝐨 𝐤𝐧𝐨𝐰 𝐡𝐨𝐰 𝐭𝐨 𝐮𝐬𝐞 𝐦𝐞. 𝐏𝐥𝐞𝐚𝐬𝐞 𝐒𝐞𝐧𝐝 𝐚 𝐝𝐢𝐫𝐞𝐜𝐭 (𝐯𝐢𝐝𝐞𝐨) 𝐥𝐢𝐧𝐤, 𝐚𝐧𝐝 𝐈 𝐰𝐢𝐥𝐥 𝐭𝐫𝐲 𝐭𝐨 𝐮𝐩𝐥𝐨𝐚𝐝 𝐨𝐧 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦.​
© @AsEnCEO 😍"""
    RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
    ABS_TEXT = " Please don't Misuse."
    UPGRADE_TEXT = "Already your in Premium⭐ "
    FORMAT_SELECTION = "Select the desired format👇 \n\n📄File Name: {}"
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | filename | username | password"""
    NOYES_URL = "@robot URL detected. Please use https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    DOWNLOAD_START = "Inprocess to download 📥"
    UPLOAD_START = "Inprocess to upload 📤"
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    RCHD_TG_API_LIMIT = "📥 Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "📥 Downloaded in {} seconds. \n📤 Uploaded in {} seconds."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "📥 Downloaded in {} seconds. \n📤 Uploaded in {} seconds."
    AFTER_SUCCESSFUL_UPLOAD = "<b>Process Completed Successfully!</b>✅"
    AFTER_SUCCESSFUL_RENAME_MSG = "✅ Rename Process Completed Successfully in {} seconds." 
    NOT_AUTH_USER_TEXT = "Not Authorised. \n PM to admin @AsEnCEO"
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease contact @AsEnCEO"
    SAVED_CUSTOM_THUMB_NAIL = "Thumbnail saved successfully 👍"
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Thumbnail cleared successfully."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared successfully."
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully."
    CUSTOM_CAPTION_UL_FILE = ""
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    NO_VOID_FORMAT_FOUND = "Error\n<b>YouTubeDL</b> said: {}"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    CURENT_PLAN_DETAILS = """Current plan details
--------
Telegram ID: <code>{}</code>
Plan name: Premium⭐
There is No Expire Limit"""
    HELP_USER = """There are multiple things I can perfom:
📌 Url Uploader
1. Send url (Link|New Name with Extension).
2. Select the button.
   SVideo - Give File as video with Screenshots
   DFile  - Give File with Screenshots
   Video  - Give File as video without Screenshots
   File   - Give File without ScreenshotsUpload as file from any HTTP link, with custom thumbnail support</a>
📌 /rename - (Long Press) and Rename Telegram Media
📌 /conv2doc - Convert to Document
📌 /conv2vid - Convert to Streamable Video
📌 /conv2aud - Convert Video Files in Telegram to Telegram Audio
📌 /savethumbnail - save Custom Thumbnail
📌 /viewthumbnail - view Custom Thumbnail
📌 /clearthumbnail - clear saved Custom Thumbnail
📌 /getlink - Get Low Speed Direct Download Link
📌 /savevid - Download media to storage
📌 /trim - (Long Press) and Enter TimeStamp
📌 /storageinfo - Get Info about currently saved Media in storage
📌 /clearvid - Clear stored media from storage
📌 /ffmpeginfo - Get Info
📌 /unzip - Extract Compressed Files, inside Telegram
📌 /generatescss - Generate SCreenShotS of Telegram media"""
    REPLY_TO_DOC_GET_LINK = "Reply to a Telegram media to get High Speed Direct Download Link"
    REPLY_TO_DOC_FOR_C2d = "Reply to a Telegram video to convert"
    REPLY_TO_DOC_FOR_C2V = "Reply to a Telegram media to convert"
    REPLY_TO_DOC_FOR_SCSS = "Reply to a Telegram media to get screenshots"
    REPLY_TO_DOC_FOR_RENAME_FILE = "Reply to a Telegram media to /rename with custom thumbnail support"
    AFTER_GET_DL_LINK = "Direct Link <a href='{}'>Generated</a> valid for {} days.\n© @AsEnCEO"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim HH:MM:SS [HH:MM:SS]"""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "First send /savevid to any media so that it can be downloaded to my local. \nSend /storageinfo to know the media, that is currently downloaded."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video Duration: {}\nSend /clearvid to delete this media, from my storage.\nSend /trim HH:MM:SS [HH:MM:SS] to cu[l]t a small photo / video, from the above media."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "A saved media already exists. Please send /storageinfo to know the current media details."
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Reply to a Telegram media (MKV), to extract embedded streams"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    INVALID_UPLOAD_BOT_URL_FORMAT = "URL format is incorrect. make sure your url starts with either http:// or https://. You can set custom file name using the format link | file_name.extension"
    ABUSIVE_USERS = "You are not allowed to use this bot."
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = ""
    EXTRACT_ZIP_INTRO_ONE = "Send a compressed file first, Then reply /unzip command to the file."
    EXTRACT_ZIP_INTRO_THREE = "Analyzing received file. ⚠️ This might take some time. Please be patient. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Sorry. Errors occurred while processing compressed file. Please check everything again twice, and if the issue persists, report this to <a href='https://telegram.dog/ThankTelegram'>@SpEcHlDe</a>"
    EXTRACT_ZIP_STEP_TWO = """Select file_name to upload from the below options."""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
"""
    SLOW_URL_DECED = "It seems to be a very slow URL. Use @transloader to get fast link"
