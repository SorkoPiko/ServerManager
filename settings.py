from dotenv import load_dotenv
from pathlib import Path  # python3 only
import os

class myenv(object):
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
    
    token = os.getenv("BOT_TOKEN")
    server = os.getenv("SUPPORT_SERVER")
    prefix = os.getenv("PREFIX")
    owner_id = os.getenv("OWNER_ID")