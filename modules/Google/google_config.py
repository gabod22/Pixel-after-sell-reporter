from globals import dirname
from pathlib import Path
SCOPES = ["https://www.googleapis.com/auth/contacts"]


GOOGLE_JSON="aftersales-438922-93709469aa37.json"
GOOGLE_WOTKSHEET_ID ="1aKE1QKpBkPeb8lEezI4z9IZ559nj4SY0PUOK_emRfu8"
GOOGLE_SHEET_NAME ="Postventa"


gspread_file = Path(dirname)/ GOOGLE_JSON