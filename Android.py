
import os

ANDROID_LOCALIZATION_DIR_NAME_EN = "res/values"
ANDROID_LOCALIZATION_DIR_NAME_MASK = "res/values-{0}"
ANDROID_LOCALIZATION_FILE_NAME = "strings.xml"

ANDROID_LOCALIZATION_HEADER = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<resources>\n"
ANDROID_LOCALIZATION_FORMAT = "<string name=\"{0}\">{1}</string>\n"
ANDROID_LOCALIZATION_FOOTER = "</resources>"

def androidGenerateLocalizationFiles(translations, languages):
    for languageId in range(0, len(languages)):
        language = languages[languageId]
        dirName = ANDROID_LOCALIZATION_DIR_NAME_EN
        if (language != "en"):
            dirName = ANDROID_LOCALIZATION_DIR_NAME_MASK.format(language)
        # Create localization directory if it does not exist.
        if (not os.path.exists(dirName)):
            print("Creating directory '{0}'".format(dirName))
            os.makedirs(dirName)
        filePath = dirName + "/" + ANDROID_LOCALIZATION_FILE_NAME
        print("Generating Android localization file '{0}'".format(filePath))
        with open(filePath, "w") as f:
            f.write(androidLocalization(translations, languageId))

def androidLocalization(translations, languageId):
    contents = ANDROID_LOCALIZATION_HEADER
    for tr in translations:
        # Ignore empty keys.
        if (tr.androidKey is None):
            continue
        # TODO: Add comments.
        contents += ANDROID_LOCALIZATION_FORMAT.format(tr.androidKey, tr.translations[languageId])
    contents += ANDROID_LOCALIZATION_FOOTER
    return contents
