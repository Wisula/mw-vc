## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQC_qwiw0U8vWa8mDJFH5lcbQTtzEnEC8ysVG2I_3rI74TUvinjP8RkUbYswV_ulrYCyNd3sd1rRu5nal74yWdZ18pKKG1Dveny-tz2ik3WFAllpiNlYGxsg7KXsTLg779dS7Y7W9QmFxvwjK5f0w6o5v2SkF34msmR8T84Wp-QPAwhQQgtuDUQr_lLFdARebMo33hIspmSbjSwMx27_mM4Q9TiZT9vPzMYfVfpRgMX01nw7Vgp1_Qmb719Eo5E6YGP5kMnvaJggPKoFAp-yQR5h6jIPQwfbEkS5bt2_uIztEB7HXVmpCrrEynGyl_u7Cqg-92kH7bioaiNTgckB-X0eAAAAATiwZVwA")
BOT_TOKEN = getenv("BOT_TOKEN", "5520091624:AAHqDBL3GsJSq2E4Nd7hAbBUTmAzZTNPBRo")
BOT_NAME = getenv("BOT_NAME", "wisula")
API_ID = int(getenv("API_ID", "19795622"))
API_HASH = getenv("API_HASH", "e7708ebb39f90d961479763d716303ab")
OWNER_NAME = getenv("OWNER_NAME", "</Methindu Wisula> [SL]")
OWNER_USERNAME = getenv("OWNER_USERNAME", "wisula4)
ALIVE_NAME = getenv("ALIVE_NAME", "wisula")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
GROUP_SUPPORT = getenv("GROUP_SUPPORT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
