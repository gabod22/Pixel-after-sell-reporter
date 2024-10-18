import os
from dotenv import load_dotenv
import sys

trello_url = "https://api.trello.com/1/cards"

trello_headers = {"Accept": "application/json"}
load_dotenv()

if getattr(sys, "frozen", False):
    dirname = os.path.dirname(sys.executable)
elif __file__:
    dirname = os.path.dirname(__file__)

config_file = os.path.join(dirname, "config.yaml")
gspread_file = os.path.join(dirname, os.getenv('GOOGLE_JSON'))
