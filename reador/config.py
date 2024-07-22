from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN")

AUTH = getenv("AUTH")
AUTH_KEY = getenv("AUTH_KEY")

TABLE = getenv("TABLE")

URL = getenv("URL")

OWNER_ID = int(getenv("OWNER_ID"))
TEXT_CHANNEL = int(getenv("IOPUTS")) # change the variable name to whatever you want i name it after the text channel i want to use it in
DATA_TC = int(getenv("DATA_TC")) # text channel where the data is stored
PRIME_DATA_ID = int(getenv("PRIME_DATA_ID")) # the first data instance
