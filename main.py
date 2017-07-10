
from Common import *
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

print("Opening spreadsheet")
spreadsheet = Spreadsheet(client)
spreadsheet.open(documentName)

print("Reading configuration page")
cfgPage = spreadsheet.sheet("CFG")
cfg = configurationFromPage(cfgPage)

print("Reading source page")
srcPage = spreadsheet.sheet("SRC")
(languages, translations) = parsePage(srcPage, cfg)
print("Found languages: '{0}'".format(languages))

for tr in translations:
    print("Android key: '{0}'".format(tr.androidKey))
    print("iOS key: '{0}'".format(tr.iosKey))
    print("Translations: '{0}'".format(tr.translations))

#print("Translations: '{0}'".format(translations))

