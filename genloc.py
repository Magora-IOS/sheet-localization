
from Spreadsheet import Spreadsheet

import sys
import gspread
# TODO: oauth2client is deprecated. Use recommended google-auth
from oauth2client.service_account import ServiceAccountCredentials

# Make sure we have credentials and a spreadsheet to operate on.
if (len(sys.argv) < 3):
    print("Usage: {0} /path/to/google_credentials.json SPREADSHEET_NAME".format(sys.argv[0]))
    sys.exit(1)

# Parse command line arguments.
credentialsFileName = sys.argv[1]
documentName = sys.argv[2]

# Create GSpread client.
scope = ["https://spreadsheets.google.com/feeds"]
credentials = ServiceAccountCredentials.from_json_keyfile_name(credentialsFileName, scope)
client = gspread.authorize(credentials)

# Open spread sheet and necessary pages.
spreadsheet = Spreadsheet(client)
spreadsheet.open(documentName)
srcPage = spreadsheet.sheet("SRC")
cfgPage = spreadsheet.sheet("CFG")

