
import sys
import gspread
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

# Get spreadsheet.
spreadsheet = None
try:
    spreadsheet = client.open(documentName)
except:
    msg = """
ERROR: Could not find spreadsheet named '{0}'.
Make sure:
* it exists
* you have added the service account email as the document editor in document sharing settings
""".format(documentName)
    print(msg)
    raise

# Get "SRC" page.
srcPage = None
try:
    srcPage = spreadsheet.worksheet("SRC")
except:
    msg = """
ERROR: Could not find sheet named 'SRC'. Make sure it exists
"""
    print(msg)
    raise

