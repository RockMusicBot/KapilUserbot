import os
from os import getenv
from dotenv import load_dotenv

# Load .env file if it exists
if os.path.exists(".env"):
    load_dotenv(".env")

# ✅ Required values (raise errors if missing)
try:
    OWNER_ID = int(getenv("OWNER_ID"))
except (TypeError, ValueError):
    raise ValueError("❌ OWNER_ID not found or invalid in environment variables.")

try:
    MONGO_URL = getenv("MONGO_URL")
    if not MONGO_URL:
        raise ValueError
except ValueError:
    raise ValueError("❌ MONGO_URL not found in environment variables.")

try:
    BOT_TOKEN = getenv("BOT_TOKEN")
    if not BOT_TOKEN:
        raise ValueError
except ValueError:
    raise ValueError("❌ BOT_TOKEN not found in environment variables.")

# ✅ Optional values with sensible defaults
API_ID = int(getenv("API_ID", "25440275"))
API_HASH = getenv("API_HASH", "44bb875668b455437ebd2939a2027d6e")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", str(OWNER_ID)).split()))
LOG_GROUP = getenv("LOG_GROUP")
ALIVE_PIC = getenv("ALIVE_PIC", "https://graph.org/file/889eb69b32f94476bc712-9558bff09cbd6faaf6.jpg")
ALIVE_TEXT = getenv("ALIVE_TEXT", "✨ I'm alive, boss!")
PM_LOGGER = getenv("PM_LOGGER", "True")
GIT_TOKEN = getenv("GIT_TOKEN")  # optional
REPO_URL = getenv("REPO_URL", "https://github.com/TEAMPURVI/ALPHA_USERBOT")
BRANCH = getenv("BRANCH", "main")

# ✅ Session strings (optional, can be empty)
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
