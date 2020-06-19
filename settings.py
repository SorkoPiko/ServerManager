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