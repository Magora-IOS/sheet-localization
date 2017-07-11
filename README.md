
# Overview

`sheet-localization` generates Android / iOS localization files from single Google Spreadsheet.

![Screenshot](readme/android.png)
![Screenshot](readme/ios_run.png)

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

# Installation

The scripts require Python 2.7+.

1. Linux
   TODO

1. Windows
   TODO

1. macOS
   1. Upgrade `six` package

      `sudo easy_install -U six`

   1. Install `pip` package manager

      `sudo easy_install pip`

   1. Install `gspread` and `oauth2client` packages
     
      `sudo -H pip install --upgrade gspread oauth2client`

# Step by step guide

## 1. Clone sample Google spreadsheet

![Screenshot](readme/clone-action.png)
![Screenshot](readme/clone-title.png)

Clone [sample spreadsheet](https://goo.gl/41wame) to your Google Drive.

The sample document contains two mandatory pages:

1. `SRC` contains translations and keys
2. `CFG` contains configurations where keys are located and what row translations start at

These pages are required by the script, so make sure to keep them.

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

## 6. Generate Android localization files

![Screenshot](readme/android.png)

Go to the directory of your choice and
generate Android localization files with the following commands:

`cd /path/to/android/project`

`python /path/to/sheet-localization/main.py /path/to/service_account_credentials.json 'Spreadsheet name' android`

This creates `res/values-<lang>/strings.xml` files with contents like this:

```
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="history">History</string>
<string name="notifications">Notifications</string>
<string name="favorite_places">Favourite places</string>
<string name="about">About</string>
<string name="wait_map_tag">wait_map_tag</string>
<string name="main_title_order"></string>
<string name="order_detail_title"></string>
<string name="action_im_here">I'm here</string>
<string name="action_get_order">Order</string>
</resources>
```

## 7. Generate iOS localization files

![Screenshot](readme/ios_run.png)

Go to the directory of your choice and
generate iOS localization files with the following commands:

`cd /path/to/android/project`

`python /path/to/sheet-localization/main.py /path/to/service_account_credentials.json 'Spreadsheet name' ios`

This creates

1. `<lang>.lproj/Localizable.strings` files with contents like this:
    ```
    "Menu.Item.History" = "History";
    "Menu.Item.Notifications" = "Notifications";
    "Menu.Item.Favourites" = "Favourite places";
    "Menu.Item.About" = "About";
    "Profile.Email.Title" = "Email";
    "Profile.BirthDate.Title" = "Birth date";
    "Profile.ChangeAvatar.Title" = "Another photo";
    "Order.Address.Here" = "I'm here";
    "Details.Order" = "Order";
    ```
1. `LocalizationConstants.h` file with contents:
    ```
    /*!
    * @b en@: History

    * @b ru@: История

    * @b uk@: Історія

    */
    extern NSString * const trMenuItemHistory;

    /*!
    * @b en@: Notifications

    * @b ru@: Уведомления

    * @b uk@: Сповіщення

    */
    extern NSString * const trMenuItemNotifications;
    ```
1. `LocalizationConstants.m` file with contents:
    ```
    import "LocalizableConstants.h"
    NSString * const trMenuItemHistory = @"Menu.Item.History";
    NSString * const trMenuItemNotifications = @"Menu.Item.Notifications";
    NSString * const trMenuItemFavourites = @"Menu.Item.Favourites";
    NSString * const trMenuItemAbout = @"Menu.Item.About";
    NSString * const trProfilePhoneTitle = @"Profile.Phone.Title";
    NSString * const trProfileEmailTitle = @"Profile.Email.Title";
    ```

Localization constants help prevent string typos.

