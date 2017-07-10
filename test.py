
import sys
import gspread
from oauth2client.service_account import ServiceAccountCredentials

if (len(sys.argv) < 2):
    print("Usage: {0} /path/to/service_account_credentials.json".format(sys.argv[0]))
    sys.exit(1)

credentialsFileName = sys.argv[1]

scope = ["https://spreadsheets.google.com/feeds"]
credentials = ServiceAccountCredentials.from_json_keyfile_name(credentialsFileName, scope)

client = gspread.authorize(credentials)
print(client)

read = False

if (read):
    spreadsheet = client.open("AutomatedTaxiLocalization")
    spreadsheet = client.open_by_url("https://docs.google.com/spreadsheets/d/18k7BoFkuZr03w2pqfR8v4hfzl4HDcZJOR5Vn3ncMc_8/edit?usp=sharing")
    print(spreadsheet)
    sheet1 = spreadsheet.sheet1
    print(sheet1)

create = True

if (create):
    spreadsheet = client.create("NewSpreadsheet")
    spreadsheet.share("taxikiev17@gmail.com", perm_type = "user", role = "writer")
