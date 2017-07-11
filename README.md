
# Overview

`sheet-localization` generates Android / iOS localization files from single Google Spreadsheet.

# Command line parameters

You generally run `sheet-localization` like this:

`python /path/to/sheet-localization/main.py /path/to/account_credentials.json SpreadSheetName TargetName`

1. `account_credentials.json` is a file you get after registering Google service account
1. `SpreadSheetName` is the name of the spreadsheet to open
   **Note**: Google service account must be given read permission to access the spreadsheet
   by sharing the document with the service account's email
1. `TargetName` is either `android` or `ios`.

# Android generated files

`sheet-localization` generates `res/value-<lang>/strings.xml` hierarchy in the current directory.

# iOS generated files

`sheet-localization` generates `<lang>.lproj/Localizable.strings` hierarchy in the current directory.

The script also generates `LocalizationConstants.h`, `LocalizationConstants.m` files with
translation constants.

# Dependencies

1. Google service account
1. The account must be given read permission to a spreadsheet
1. gspread 

# Step by step guide

## 1. Clone sample Google spreadsheet

![Screenshot](readme/clone-action.png)
![Screenshot](readme/clone-title.png)

Clone [sample spreadsheet](https://goo.gl/41wame) to your Google Drive.

## 2. Create new Google API project

![Screenshot](readme/project-title.png)
![Screenshot](readme/project-created.png)

Go to [Google API console](https://console.developers.google.com) and create a new project.

## 3. Enable Google Drive API

![Screenshot](readme/enable-api-locate.png)
![Screenshot](readme/enable-api-enable.png)
![Screenshot](readme/enable-api-done.png)

Enable Google Drive API.

## 4. Create service account

![Screenshot](readme/credentials-type.png)
![Screenshot](readme/credentials-title.png)
![Screenshot](readme/credentials-json.png)

Create service account credentials for a `Web server` to access `Application data`

Name the service account and give it `Project -> Editor` role.

Upon account creation you should get a special JSON, which contains all necessary credentials.

## 5. Allow service account to read the spreadsheet document

![Screenshot](readme/share.png)

The JSON you downloaded looks like this:
```
{
  "type": "service_account",
  "project_id": "localization-173405",
  "private_key_id": "d37cdb95af7f817a05c",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCO8ACoDvAG0q8R\xg3bQzHYCVrEDBcBFkfJ4d8dfy9FdIS++p3XvmLOWnFyMreQTPh1\njmx7jdmDpEwZHNZrj2dYYf0Xta8A0wxdejqUmNq4CyOBqTzomqCdzu36qBp8szUk\nN1l9G9u+rLcm9J/BlinOeA==\n-----END PRIVATE KEY-----\n",
  "client_email": "localization@localization-173405.iam.gserviceaccount.com",
  "client_id": "1016040",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/localization%40localization-173405.iam.gserviceaccount.com"
}
```

To allow the service account to read your spreadsheet, you need to give `client email`
read permissions to your document. You can do it in sharing settings.

