import os
from dotenv import load_dotenv
import sys
from os import path

#Trello API constants
TRELLO_ENDPOINT = "https://api.trello.com/1/cards"
TRELLO_HEADERS = {"Accept": "application/json"}
TRELLO_TOKEN="ATTA3bb61958d5b3506b54860df6410561d10f408ed793e46cc60846737fac06cbc07E9CEBB9"
TRELLO_KEY="2c0369eb0c76fbbbf4ecf3094fd31356"
TRELLO_ID_LIST="66db40b0006d1f0947656dec"

GOOGLE_JSON="aftersales-438922-93709469aa37.json"
GOOGLE_WOTKSHEET_ID ="12Vmae8o_54a-pQg7LgqMkWnSkx6s9dy7016tq3i-_Rw"
GOOGLE_SHEET_NAME ="Postventa"


load_dotenv()

if getattr(sys, "frozen", False):
    dirname = path.join(path.dirname(sys.executable), '_internal')
elif __file__:
    dirname = os.path.dirname(__file__)
    
print(f"dirname: {dirname}")

config_file = os.path.join(dirname, "config.yml")
print(f"config_file: {config_file}")

gspread_file = os.path.join(dirname, GOOGLE_JSON)
print(f"gspread_file: {gspread_file}")