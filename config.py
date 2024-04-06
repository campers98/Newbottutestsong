import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "27957041"))

API_HASH = getenv("API_HASH", "2ae1c9912cd2efdecae7f0208994f0b0")

BOT_TOKEN = getenv("BOT_TOKEN", "6348947600:AAEiVkLjouPBs5_JcPTNegCXTPoGN8rGwFs")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Allsvdgang:Single_1122334455@cluster0001.xrucpqp.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 54000))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "54000")
)

LOGGER_ID = int(getenv("LOGGER_ID", "-1001975251757"))

OWNER_ID = int(getenv("OWNER_ID", "6518634528"))

START_STICKER_ID = getenv("START_STICKER_ID", "CAACAgUAAxkBAAEL29RmEWHZ7dHYKkec_MCXoJSPhBtDQwACkQQAAiQRAVcenyI_tCbFdjQE")

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "songtestbotu")

POWERED_BY = getenv("POWERED_BY", "˹ unknown ˼")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/campers98/Newbottutestsong",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/SVD_Squad_Gamerz")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/SVD_Squad_Gamerz")

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", None))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "True")
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "5400"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe")


PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "300"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))



# Get your pyrogram v2 session from @TBN_StringGeneratorRobot on Telegram
STRING1 = getenv("STRING_SESSION", "BQGqlzEAUAGdK4t1MkzmeG7ivE3ER9AutwZP9YYnXsEdkWnZR9aINO1o7USh8_7vYkLbX51mcAX4Ivrmi56p529gsFojB8YhLn5CypH36b1hLLuIV51oNpp3Rj28lhQ_4f0nFlz9IYH9cfjXtFxS7ec1b918Vjf6EkMNTlEwXg3XKwBkOcVjuJyZM_Rkfoc2sCTzaYa4yMbCWhApz8h4RX6oEFrztnXLVLEgEsZRVeMZbg6Sx6clJhUr_CH9_ITRG3uUUYjbwgbi0HWavPrjgBbDornEGzK2eTMYjFJ_ICqO74ERvxzlIOcdmPexKXTSlOw2X9PtZjllXI7BqiRy-6Cdi_4EewAAAAFXTCi3AA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/4901ceb88125d76898dad.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/30577470793677e5408ee.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/7db32a17b15440fa88f91.jpg"
STATS_IMG_URL = "https://telegra.ph/file/02af26494524244cf83d0.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/fa144f06d6d024877edda.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/fa144f06d6d024877edda.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/03efec694e41e891b29dc.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/b00af14042edff8b71f2e.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/9f3720a8d4ec5ae50977f.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/fa144f06d6d024877edda.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/fa144f06d6d024877edda.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/fa144f06d6d024877edda.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
