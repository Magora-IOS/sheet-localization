from Common import *
from IOS import *
from Spreadsheet import Spreadsheet

import sys
import gspread
# TODO: oauth2client is deprecated. Use recommended google-auth
from oauth2client.service_account import ServiceAccountCredentials

IOS_LOCALIZATION_FILE_NAME_MASK = "Localizable-{0}.strings"
IOS_CONSTANTS_HEADER_FILE_NAME = "LocalizationConstants.h"
#IOS_CONSTANTS_SOURCE_FILE_NAME = "LocalizationConstants.m"

USAGE = """
Usage: {0} /path/to/google_credentials.json SPREADSHEET_NAME TARGET
    
    SPREADSHEET_NAME
        If it contains whitespaces, use '' around the name.

    TARGET
        Valid options are: 'android', 'ios'
"""

# Make sure we have all necessary parameters specified at command line.
if (len(sys.argv) < 4):
    print(USAGE.format(sys.argv[0]))
    sys.exit(1)

# Parse command line arguments.
credentialsFileName = sys.argv[1]
documentName = sys.argv[2]
targetName = sys.argv[3]

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

if (targetName == "android"):
    print("TODO: generate Android files")
elif (targetName == "ios"):
    for languageId in range(0, len(languages)):
        fileName = IOS_LOCALIZATION_FILE_NAME_MASK.format(languages[languageId])
        print("Generating iOS localization file '{0}'".format(fileName))
        with open(fileName, "w") as f:
            f.write(iosLocalization(translations, languageId))
else:
    print("ERROR: Unknown target")
    sys.exit(1)


