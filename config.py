import os

from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
ADMIN = int(os.getenv('ADMIN',994851680))
CHANNEL = int(os.getenv('CHANNEL',12345))
API_ID = int(os.getenv("API_ID", "6"))
API_HASH = os.getenv("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
ASSISTANT_NAME = os.getenv("ASSISTANT_NAME", "Vc Video Player")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "Alem_Sohbet")
UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "Universite_Sohbet")
SOURCE_CODE = os.getenv("SOURCE_CODE", "github.com/Ruhsuzbey/VcVideoPlayer")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SESSION_NAME = os.getenv("SESSION_NAME")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
