from dotenv import load_dotenv
from pathlib import Path  # python3 only
import os

class myenv(object):
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
    
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    SUPPORT_SERVER = os.getenv("SUPPORT_SERVER")
    PREFIX = os.getenv("PREFIX")
    OWNER_ID = os.getenv("OWNER_ID")
    EXTRA_COMMAND = os.getenv("EXTRA_COMMAND")
    SWEAR_WORD1 = os.getenv("SWEAR_WORD1")
    SWEAR_WORD2 = os.getenv("SWEAR_WORD2")
    SWEAR_WORD3 = os.getenv("SWEAR_WORD3")
    SWEAR_WORD4 = os.getenv("SWEAR_WORD4")
