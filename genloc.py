
import sys
import gspread
from oauth2client.service_account import ServiceAccountCredentials

if (len(sys.argv) < 3):
    print("Usage: {0} /path/to/google_credentials.json SPREADSHEET_NAME".format(sys.argv[0]))
    sys.exit(1)

credentialsFileName = sys.argv[1]
documentName = sys.argv[2]

scope = ["https://spreadsheets.google.com/feeds"]
credentials = ServiceAccountCredentials.from_json_keyfile_name(credentialsFileName, scope)

client = gspread.authorize(credentials)
print(client)

spreadsheet = client.open(documentName)
print(spreadsheet)
sheet1 = spreadsheet.sheet1
print(sheet1)

