from os import path
import sys

trello_url = "https://api.trello.com/1/cards"

trello_headers = {"Accept": "application/json"}


if getattr(sys, "frozen", False):
    dirname = path.dirname(sys.executable)
elif __file__:
    dirname = path.dirname(__file__)

config_file = path.join(dirname, "config.yaml")
gspread_file = path.join(dirname, "pixel-json.json")
