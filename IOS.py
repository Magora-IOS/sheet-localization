
import os

IOS_LOCALIZATION_DIR_NAME_MASK = "{0}.lproj"
IOS_LOCALIZATION_FILE_NAME = "Localizable.strings"

IOS_LOCALIZATION_FORMAT = "\"{0}\" = \"{1}\";\n"

IOS_CONSTANTS_HEADER_FILE_NAME = "LocalizationConstants.h"
IOS_CONSTANTS_SOURCE_FILE_NAME = "LocalizationConstants.m"

IOS_CONSTANTS_HEADER_CONST_FORMAT = "extern NSString * const {0};\n"
IOS_CONSTANTS_HEADER_DESC_START_FORMAT = "\n/*!\n"
IOS_CONSTANTS_HEADER_DESC_END_FORMAT = "*/\n"
IOS_CONSTANTS_HEADER_COMM_FORMAT = "* {0}\n\n"
IOS_CONSTANTS_HEADER_LANG_FORMAT = "* @b {0}@: {1}\n\n"

IOS_CONSTANTS_SOURCE_HEADER = "import \"LocalizableConstants.h\"\n"
IOS_CONSTANTS_SOURCE_FORMAT = "NSString * const {0} = @\"{1}\";\n"

def iosConstants(translations, languages):
    header = ""
    source = IOS_CONSTANTS_SOURCE_HEADER
    for tr in translations:
        # Ignore empty keys.
        if (not len(tr.iosKey)):
            continue
        # Constant description.
        header += IOS_CONSTANTS_HEADER_DESC_START_FORMAT
        # TODO: Add comments.
        for languageId in range(0, len(languages)):
            language = languages[languageId]
            header += IOS_CONSTANTS_HEADER_LANG_FORMAT.format(language, tr.translations[languageId])
        header += IOS_CONSTANTS_HEADER_DESC_END_FORMAT
        # Constant itself.
        constant = "tr" + tr.iosKey.replace(".", "")
        header += IOS_CONSTANTS_HEADER_CONST_FORMAT.format(constant)
        source += IOS_CONSTANTS_SOURCE_FORMAT.format(constant, tr.iosKey)
    return (header, source)

def iosGenerateConstantsFiles(translations, languages):
    (header, source) = iosConstants(translations, languages)
    headerFileName = IOS_CONSTANTS_HEADER_FILE_NAME
    print("Generating iOS constants file '{0}'".format(headerFileName))
    with open(headerFileName, "w") as f:
        f.write(header)
    sourceFileName = IOS_CONSTANTS_SOURCE_FILE_NAME
    print("Generating iOS constants file '{0}'".format(sourceFileName))
    with open(sourceFileName, "w") as f:
        f.write(source)

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
        # TODO: Add comments.
        contents += IOS_LOCALIZATION_FORMAT.format(tr.iosKey, tr.translations[languageId])
    return contents
