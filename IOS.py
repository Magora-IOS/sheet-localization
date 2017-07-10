
import os

IOS_LOCALIZATION_DIR_NAME_MASK = "{0}.lproj"
IOS_LOCALIZATION_FILE_NAME = "Localizable.strings"
IOS_CONSTANTS_HEADER_FILE_NAME = "LocalizationConstants.h"
#IOS_CONSTANTS_SOURCE_FILE_NAME = "LocalizationConstants.m"

def iosGenerateLocalizationFiles(translations, languages):
    for languageId in range(0, len(languages)):
        language = languages[languageId]
        dirName = IOS_LOCALIZATION_DIR_NAME_MASK.format(language)
        # Create localization directory if it does not exist.
        if (not os.path.exists(dirName)):
            print("Creating directory '{0}'".format(dirName))
            os.makedirs(dirName)
        filePath = dirName + "/" + IOS_LOCALIZATION_FILE_NAME
        print("Generating iOS localization file '{0}'".format(filePath))
        with open(filePath, "w") as f:
            f.write(iosLocalization(translations, languageId))

def iosLocalization(translations, languageId):
    contents = ""
    for tr in translations:
        # Ignore empty keys.
        if (not len(tr.iosKey)):
            continue
        contents += "\"{0}\" = \"{1}\";\n".format(tr.iosKey, tr.translations[languageId])
    return contents
