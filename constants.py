import os
from dotenv import load_dotenv
import sys
from os import path

START_DATE = "2022-01-01"

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