from globals import getConfig
#Trello API constants
TRELLO_ENDPOINT = "https://api.trello.com/1/cards"
TRELLO_HEADERS = {"Accept": "application/json"}
TRELLO_TOKEN="ATTA3bb61958d5b3506b54860df6410561d10f408ed793e46cc60846737fac06cbc07E9CEBB9"
TRELLO_KEY="2c0369eb0c76fbbbf4ecf3094fd31356"
TRELLO_ID_LIST="66db40b0006d1f0947656dec"

# Load configuration from YAML file


import logging
trello_labels = getConfig()['TRELLO_LABELS']
logging.debug(f"trello_labels: {trello_labels}")

trello_members = getConfig()['MEMBERS']