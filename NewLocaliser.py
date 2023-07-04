from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import pandas as pd
# File Paths
CREDENTIAL_FILE_LOCATION = "/Users/gokulnair/Desktop/LocaliserScript/SSToken.json"
LOCALIZED_FILE_LOCATION = "/Users/gokulnair/Desktop/Localisation.odt"
STRING_NAME_KEYS = ['create_site', 'next_add_team', 'calculate_payables']
SUCCESS_RANGE_NAME = "Project modules"
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
## Gsheet Creds
creds = None
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists(CREDENTIAL_FILE_LOCATION):
    creds = Credentials.from_authorized_user_file(CREDENTIAL_FILE_LOCATION, SCOPES)
# If there are no (valid) credentials available, let the user log in.cr
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            CREDENTIAL_FILE_LOCATION, SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('SSToken.json', 'w') as token:
        token.write(creds.to_json())
service = build('sheets', 'v4', credentials=creds)
### Success Owner
SUCCESS_SPREADSHEET_ID = '1tAXGZO1yRk7wec_lsug107J6UN3Ah2eRnQw6CDbLFig'
# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SUCCESS_SPREADSHEET_ID,
                            range=SUCCESS_RANGE_NAME).execute()
values = result.get('values', [])
data=pd.DataFrame(values)
## Manipulation
data.columns=data.iloc[0]
data=data.drop(data.index[0])
df2 = data.query(f"String_Name in ({STRING_NAME_KEYS})")
myLocalisations = { }
tempLang = ""

# Desired keys for rows and columns
row_keys = ['String_Name']
column_keys = ['English','Hindi',"Tamil","Gujarati","Kannada","Punjabi","Telugu","Bengali","Malayalam"]
for keys in column_keys:
  myLocalisations[keys] = []
# Iterate over rows and columns
for index, row in df2.iterrows():
    row_values = [row[key] for key in row_keys]
    for col_key in column_keys:
        cell_value = row[col_key]
        myLocalisations[col_key].append(f"\"{row_values[0]}\" = \"{cell_value}\"; ")

try:
    with open(LOCALIZED_FILE_LOCATION):
        with open(LOCALIZED_FILE_LOCATION, 'a') as file:
             for lang, localisation in myLocalisations.items():
                for local in localisation:
                    if tempLang != lang:
                        tempLang = lang
                        file.write(f'\n##{lang}\n')
                    file.write(f"{local}")
                    file.write('\n')
except IOError:
    with open (LOCALIZED_FILE_LOCATION, 'w') as file:
        for lang, localisation in myLocalisations.items():
            for local in localisation:
                if tempLang != lang:
                    tempLang = lang
                    file.write(f'\n##{lang}\n')
                file.write(f"{local}")
                file.write('\n')
         