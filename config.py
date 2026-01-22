#
# Copyright (C) 2021-2022 by TheAloneteam@Github, < https://github.com/TheAloneTeam >.
#
# This file is part of < https://github.com/TheAloneTeam/TheAloneMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TheAloneTeam/TheAloneMusic/blob/master/LICENSE >
# All rights reserved.

import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("26249286", 0))
API_HASH = getenv("4e3bf0b014fda4ac752e8f4ab854279b")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7978548850:AAHuPm3psGOjpWMoMjBqt-w1FgWkLyJvDW8")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://lollolopp0900:slayersan@cluster0.mge1ngz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

# Set this to true if you want post ads automatically
ADS_MODE = getenv("ADS_MODE", None)

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("-1002745123292"))

DEBUG_IGNORE_LOG = True
# Get this value from  on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 7804917014))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/TheAloneTeam/AloneMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TheAloneTeam")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TheTeamAlone")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", None))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQFNgbsAchUCEzQ3h6sO1Uq4hBTU6_iyk63t3GD6fQHGlkD4UTlqCI-Nyn_XyHb_6Crcus9ypbI6RHBv1cocx6QPCzGDAjLeWmb76-j8w5xBLxvm3XCkETp87AlT8tjv4wXFe_HPJENAfVrijndLXEYuoJFalIAXdLTSUu6nYEcQzN4HW0_PDpA9DKfRV7TdvVvprcn10ETsJD34yGRh6T_-pe6lCXG4F-dGmrLlkCVB0FZF2-lqE_yCux0chGbu55r5xLdUhOamCAh_e8I-2EDS2wuTiVO6mpMMwJLllZKMdSf9uaicOT3gyGMYBYUzxII_YtrG8jwE9H9VIDUv0C62faoQbgAAAAHjB6-9AA")
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


START_IMG_URL = getenv(
    "START_IMG_URL",
    "https://files.catbox.moe/34xlvu.jpg",
)
PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://files.catbox.moe/34xlvu.jpg",
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/34xlvu.jpg"
STATS_IMG_URL = "https://files.catbox.moe/34xlvu.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/34xlvu.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/34xlvu.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/34xlvu.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/34xlvu.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/34xlvu.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/34xlvu.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/34xlvu.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/34xlvu.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


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
